#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# Imports
##

import ast, base64, cmd, hashlib, os, random, re, stripe
from Crypto.Cipher import AES # pycryptodome version 3.17
from datetime import datetime

##
# Defines character list and special characters
##

character_list = ""
for i in range(32, 0x110000):
    izard = chr(i)
    if izard.isprintable():
        character_list = character_list + izard

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

##
# Enter in your Stripe API key
##

stripe.api_key = "sk_test_ovLyqg8NbkIWoL96q9DGif7h00ceBDGZvJ"

print('\nSUPER SECRET CHAT PROGRAM \n Type help for more info. \n')


class console(cmd.Cmd):
    prompt = '<input> '

    def do_send(self, arg):
        '''Send a message.'''
        msg_in = input("Message: ")
        password = input("Password: ")
        if len(password) <= 8:
            print("Password must be at least 8 characters.")
            console().cmdloop()

        if (regex.search(password) == None):
            print("Password must include special characters.")
            console().cmdloop()

        try:
            key_length = int(input("Key length: "))
        except:
            print("Key length must be an integer and cannot be blank.")
            console().cmdloop()

        hash = ""

        for i in password:
            hash = hash + str(character_list.find(i))

        len1 = len(hash)

        if (len1 % 2) != 0:
            hash = hash + '1'

        print('Converting password to integer: ' + hash + '\n')
        len2 = int(len(hash))

        n1 = int(len2 / 2)
        seed = hash[:n1]
        print('Key seed: ' + seed + '\n')
        char_seed = hash[n1:]
        print('Character seed: ' + char_seed + '\n')

        myList = list(character_list)
        random.seed(char_seed)
        random.shuffle(myList)
        char_list = "".join(str(x) for x in myList)
        # print('Character list: ' + char_list + '\n')

        try:
            random.seed(int(seed))
        except:
            print("Invalid input. Must be integer. \n")
            console().cmdloop()

        password = bytes(password, 'utf-8')
        IV_SIZE = 16  # 128 bit, fixed for the AES algorithm
        KEY_SIZE = 32  # 256 bit meaning AES-256, can also be 128 or 192 bits
        SALT_SIZE = 16  # This size is arbitrary

        salt = os.urandom(SALT_SIZE)
        derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000,
                                      dklen=IV_SIZE + KEY_SIZE)
        iv = derived[0:IV_SIZE]
        key = derived[IV_SIZE:]

        encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(msg_in.encode('utf-8'))
        encrypted = str(encrypted)
        print("Encrypted Message: " + encrypted + '\n')

        message = ""
        key_position = 0

        rndm = str(random.getrandbits(50000))
        key_list = []
        num = 1
        for i in range(0, len(rndm)):
            if num == 10:
                num = 1
            if rndm[i] == str(0):
                num2 = num
                num += 1
            else:
                num2 = rndm[i]
            key_list.append(str(num2))
        rndm = "".join(key_list)

        for i in range(0, len(encrypted)):
            keys = ""
            for i2 in range(0, key_length):
                try:
                    key = rndm[key_position]
                except:
                    print("Key length too excessive. With longer messages, keep the key length around 20 at most.")
                    console().cmdloop()
                keys = keys + key
                key_position += 1

            h1 = int(keys)
            print('keys:' + keys)
            h2 = int(char_list.find(encrypted[i]))
            print('Character position: ' + str(h2))
            h3 = int(h1 + h2 + 100)
            print('Cypher: ' + str(h3))
            print()

            message = message + str(h3)

        year = datetime.now().year + 1
        token = stripe.Token.create(
            card={
                "object": "card",
                "number": "4000000000000259",
                "exp_month": "12",
                "exp_year": year,
            })

        stripe.Customer.create(source=token.id)

        customer = stripe.Customer.list(limit=1)
        customer2 = customer.data
        for i in customer2:
            cus_id = i.id

        stripe.Charge.create(amount=42000, currency="usd", customer=cus_id, description="Charge for john@soandso.com", )

        dispute = stripe.Dispute.list(limit=1)

        dispute_object = dispute.data

        for i in dispute_object:
            dispute_id = i.id

        stripe.Dispute.modify(dispute_id, evidence={"access_activity_log": message})
        print("Message: " + message + '\n')
        console().cmdloop()

    def do_read(self, arg):
        'Read a message.'
        customer = stripe.Customer.list(limit=1)
        customer2 = customer.data
        for i in customer2:
            cus_id = i.id
        password = input("Password: ")
        key_length = int(input("Key length: "))
        hash = ""

        for i in password:
            hash = hash + str(character_list.find(i))

        len1 = len(hash)

        if (len1 % 2) != 0:
            hash = hash + '1'

        len2 = int(len(hash))

        n1 = int(len2 / 2)
        seed = hash[:n1]
        char_seed = hash[n1:]

        print('Converting password to integer: ' + hash + '\n')
        print('Key seed: ' + seed + '\n')
        print('Character seed: ' + char_seed + '\n')

        try:
            random.seed(int(seed))
        except:
            print("Invalid input. Must be integer. \n")
            console().cmdloop()

        rndm = str(random.getrandbits(50000))
        key_list = []

        num = 1
        for i in range(0, len(rndm)):
            if num == 10:
                num = 1
            if rndm[i] == str(0):
                num2 = num
                num += 1
            else:
                num2 = rndm[i]
            key_list.append(str(num2))
        rndm = "".join(key_list)

        dispute = stripe.Dispute.list(limit=1)

        dispute_object = dispute.data

        for i in dispute_object:
            dispute_id = i.id

        dispute_object = stripe.Dispute.retrieve(dispute_id)

        message = dispute_object.evidence["access_activity_log"]

        myList = list(character_list)
        random.seed(char_seed)
        random.shuffle(myList)
        char_list = "".join(str(x) for x in myList)
        # print('\nCharacter list: ' + char_list + '\n')

        msg_out_lst = []

        message2 = ""
        key_start = 0
        key_end = key_length

        for i in range(0, int(len(str(message)) / key_length)):
            keys = ""
            ph = message[key_start:key_end]
            for i2 in range(0, key_length):
                key = rndm[key_start]
                keys = keys + key
                key_start += 1
            try:
                msg_out_lst.append(char_list[int(ph) - 100 - int(keys)])
            except:
                print("Incorrect password or key length.")
                console().cmdloop()

            message2 = message2 + ph

            key_end += key_length

        # print("Message: " + message2)

        msg_out = "".join(msg_out_lst)
        print('\nEncrypted Message: ' + msg_out)

        password = bytes(password, 'utf-8')
        IV_SIZE = 16  # 128 bit, fixed for the AES algorithm
        KEY_SIZE = 32  # 256 bit meaning AES-256, can also be 128 or 192 bits
        SALT_SIZE = 16  # This size is arbitrary

        encrypted = ast.literal_eval(str(msg_out))

        encryptedString = base64.encodebytes(encrypted)
        print()
        print(encryptedString)

        encrypted = base64.decodebytes(encryptedString)  # <- get the bytes back

        salt = encrypted[0:SALT_SIZE]
        derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000,
                                      dklen=IV_SIZE + KEY_SIZE)
        iv = derived[0:IV_SIZE]
        key = derived[IV_SIZE:]
        cleartext = AES.new(key, AES.MODE_CFB, iv).decrypt(encrypted[SALT_SIZE:])
        print()
        print(cleartext)


console().cmdloop()

