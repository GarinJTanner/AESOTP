# AESOTP
A combination of the Advanced Encryption Standard (AES), and what I would like to call a One-Time Pad (OTP). 

## aesotp-minimodem
This script uses Minimodem for message delivery. Minimodem works essentially like a 56k modem. It turns data into sound, allowing the encrypted message to be passed along using a stereo cable.

## aesotp-stripe
This script uses a free Stripe.com account as its database. It cuts up the message into small chunks and stores them on your Stripe account through **fake** transactions. A message like "ABC" would look like "$1.37, $2.56, $4.01."
