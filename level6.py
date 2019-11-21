#!/usr/bin/env python3
from pathlib import Path
import binascii
ANSWER = "dunno_yet"

###########
# level 6 #
###########

print("Welcome to Level 6.")
print("Unknown, single byte XOR encrypted data [optional]")
print("---\n")

# TASK
# This is a moderately challenging task, but achievable if you've come this far.
# The file "encrypted.txt" contains a series of lines, with text representations
# of hex data. One of them is a message encrypted with a single byte xor key.
# That means every byte in the line is encrypted the same way.
#
# What is the message?
#
# HINT: Don't forget to use binascii.unhexlify() to turn printed hex into bytes

f = Path(__file__).parent / "files" / "encrypted.txt"
all_lines = f.read_text()

print("Oh god.. how do I do this... but wait!")


###################
# level 6 - bonus #
###################

# TASK
# This is a very challenging task, but achievable if you've come this far.
# The file "secret.enc" is encrypted with a single byte xor cipher. The key
# is unknown, and the file is not a text file, but was created by an Adobe
# software package.

f = Path(__file__).parent / "files" / "secret.enc"
content = f.read_bytes()

print("Are files actually encrypted like this in the world? {}".format(ANSWER))


###################
# Beyond... More? #
###################

print("If you'd like more of this, check out the README.")
