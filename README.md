# AESOTP
A combination of the Advanced Encryption Standard (AES), and what will be referred to as an advanced One-Time Pad (OTP). 

A One-Time Pad is an antiquitated encryption that essentially converts a letter to a numerical value. 

A = 1

B = 2

C = 3

Z = 26

The message "ABC" could be encrypted with a key. Say, the message was "ABC" and also the key was "123". The encrypted message would then become, "246".

If you were to include every available character in the UTF-8 format, which includes characters that are not used by an Englishman, this includes every possible langugage known to man, you now displace the character set by a greater factor. Instead of having a series of 26, we now have a series of 144,516. 

After that being said, this encryption is now thrice fold afterward: We use AES, then we use the proprietary OTP, then we use a method to transmit the code which also encrypts it a third time.

## aesotp-minimodem
This script uses Minimodem for message delivery. Minimodem works essentially like a 56k modem. It turns data into sound, allowing the encrypted message to be passed along using a stereo cable.

## aesotp-stripe
This script uses a free Stripe.com account as its database. It cuts up the message into small chunks and stores them on your Stripe account through fake transactions. A message like "ABC" would look like "$1.37, $2.56, $4.01."


