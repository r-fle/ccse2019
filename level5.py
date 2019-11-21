#!/usr/bin/env python3
import binascii
ANSWER = "dunno_yet"

###########
# level 5 #
###########

print("Welcome to Level 5.")
print("XOR encryption: one byte? one line of hex stuff?")
print("---\n")

"""
Now that we can xor any number against any other number, by seeing that 
we are reallying performing xor on their binary components, it should be clear
that we can xor one byte against any other byte.

Let's try it.
"""

# TASK:
# What is 0x14 ^ 0xf2
x = 0x14
y = 0xf2
print("0x14 ^ 0xf2 is?: {}".format(x ^ y))
print("Why did that not print as hex? {}".format(ANSWER))

# TASK:
# To get the above stored as the bytes e6, not as the string "0xe6" or the int 230,
# we can use one of two methods:
# Option 1: bytes([x ^ y])
# Option 2: (x ^ y).to_bytes(1, 'little')
z = x ^ y
print("z should be b'\\xe6'. Right? {}".format(z))
print("DOH!")

# TASK:
# Use the binascii library to make working with hex easier.
# Can you work out what this is in hex, before you decode it?
familiar = "4142434461626364"
hmm = binascii.unhexlify(familiar)
#print(hmm)
# Let's do it the other way
back_to_hex = binascii.hexlify(hmm)
print(back_to_hex)

# TASK:
# Create your own message, and hexlify it.
# You'll need to make it 'bytes' somehow!
# Option 1: your_message = b"..."
# Option 2: your message =  "...".encode()
# your_message = "What a great message; Hopefully you customised it though?"
# hmm2 = binascii.hexlify(your_message)
# print(hmm2)

# -----

# TASK:
# XOR encryption! message with something the same length
# This could prove challenging, but you can do it! :)
enc = "e3af865eb8f58a955f004221767aae89c85695dd862463c108"
key = "b0dfef3099d5c2f4326d2753575ae8e0ba33b4fdcc510eb129"

# Your task is to xor the key against the encrypted ciphertext (enc).
# For each byte of the first, xor it with the corresopnding byte of the second,
# and save the result as you go.
#
# If you have trouble with this task, scroll down for hints labelled ^^ SPOILER ^^
# Don't forget to unhexlify!

mes = b"" # enc ^ key ??
print("Fully awesome xor decrypted: {}".format(ANSWER))


########################################
# level 5 - bonus but you should do it #
########################################

# TASK:
# What is the value of mes (the decrypted message above) XORed against the key?
# HINT: You may not need a computer.

# TASK:
# This hex string has been XOR encrypted with a single byte key.
# That is, each and every byte of this was XOR'd against the same fixed byte. 
# What is the decrypted string?
# HINT: "ETAOIN SHRDLU", or work our any method you like :)
singlebytexor = "725f43161a4d5255495f1a585f5f541a575f494953545d1a4d534e521a57431a485b5e5355051a6e5253491a5349541d4e1a5b564e5f48545b4e534c5f1a48555951161a534e1d491a595556565f5d5f1a4855595114"






































# ^^ SPOILER ^^
# Your result should be "5370696e212048616d6d657221204669726521204a756d7021" 
