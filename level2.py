#!/usr/bin/env python3
import string
ANSWER = "dunno_yet"

###########
# level 2 #
###########

print("Welcome to Level 2.")
print("Caesar cipher: words, sentences, encryption, decryption!")
print("---\n")

""" A caesar cipher is also known as a shift cipher, or a Caesar shift.
Now that we can convert letters to numbers, and back again, we can use
software to add a number to a letter. We just need to somehow wrap around
to the beginning. """

# OVERALL:
# Your task is to implement a caesar cipher encryption and decryption function.
# This might seem hard at first, but we'll get there a piece at a time.
print("Useful letters: ", string.ascii_uppercase)

# TASK:
# Encode this word with the key 3, and print the result.
# I have started the loop for you!
plain = "hello"
crypt = ""
for letter in plain:
    # What is the result of: ord(letter)
    # I need to add 3
    crypt = crypt + "?" # something to do with chr(??)"

print(plain, "encrypted with key 3 is", crypt)
print("Done!")


# TASK:
# Write a general encryption function for the caesar cipher!
# I have included some useful functions at the start
def encrypt(plain, key):
    crypt = ""
    # make sure plain is upper case
    plain = plain.upper()
    for c in plain:
        # I need to transform c by key. Will Y + 3 == B?
        crypt += "encrypted_c"

    # We are fancy and will 'return' the answer, rather than printing it
    return crypt

message = "pizza"
crypt = encrypt(message, 16)
print("Encrypting pizza:   ", crypt )
print("I hope that printed: FYPPQ")


# TASK: 
# Decode this caesar encoded word. The key is 7.
# Hint: You do not need to write a decryption function.
secret_message = "JVUMPKLUAPHS"
print(ANSWER)


###################
# level 2 - bonus #
###################

# TASK: 
# Decode this caesar encoded sentence. I have no idea what the key is.
# You may need to modify your encryption/decryption system to ignore spaces! : )
# eg. if letter == " ":
#         ????
sentence = "BG MAX DLMA VXGMNKRY MAX IXKLHGTE TWOXKMBLXFXGML LXVMBHG BG GXPLITIXKL PHNEW LHFXMBFXL UX NLXW MH XQVATGZX FXLLTZXL XGVKRIMXW NLBGZ LABYMBGZ VBIAXKLA"

# HINT:
# for i in range(26):
#     do_some_decryption(sentence, i)

