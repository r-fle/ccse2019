#!/usr/bin/env python3
from pathlib import Path
ANSWER = "dunno_yet"

###########
# level 4 #
###########

print("Welcome to Level 4.")
print("Hex? Hex vs ascii. Binary? AND, OR, XOR?!")
print("---\n")

# TASK:
# If you don't know what binary, hex, or bytes are: read this!
# Google is also your friend on this one. Everyone tends to find a different
# explanation that 'sticks' for them - so feel free to look around sometime.
"""
Back to the fundamental computer science concepts: we're going to talk about
binary, and hex. So far, we know what decimal is (right?), and what ascii kinda
is. In decimal there are 10 symbols (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) that we use
for counting. In the english alphabet, we use 26 letters to store meaning.

For hex, we use 16 symbols: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f
In binary, we use just 2:   0, 1

You may have done this in maths, but a decimal number (say 27) can be written 
in hex, known as 'base 16', like so:

       0x10 (this is 16)               <-- the prefix 0x means 'hex'
     + 0x0b (this is 11)
       ----
     = 0x1b

Or we can write it in binary, known as 'base 2':

    0b00011011                         <-- the prefix 0b means 'binary'
          \\ \\___  1 +
           \\ \___  2 +
            \\____  8 +
             \____ 16
                   -- 
                   27

It turns out, that inside computers, everything is binary. Crazy. But it's also
very difficult to 'read' binary, so we use hex to display it to humans, and to
group it together to ship around.

One hex 'letter' (0-9a-f) has sixteen options, which is equal to 4 binary digits.
So two hex letters, is 8 binary digits, or as we say, 8 bits. This is called a
byte. 
"""

# TASK:
# How many possible values are there for one byte?
# HINT: 3 squared in python is: 3**2
print("A single byte (8 bits) could be {} different values".format(ANSWER))

# TASK:
# What is the Hex (raw bytes) representation of "A"?
# Let's check out files/ascii_hex.txt
f = Path(__file__).parent / "files" / "ascii_hex.txt"
print(f.read_text())

# HINT: THere's a built in function called hex() .. You can give it an integer
# and it will conver it to a hexadecimal string for you to read.
print("The hex value of {} is: {}".format("A", ANSWER))

# ----

# TASK:
# What is XOR?
# XOR, or exclusive or, is known as a 'boolean operation'. This is just fancy
# speak for saying it is the result of combining two bits in a particular way.
# Here is a truth table for OR, for AND, and for XOR. Fill it in!

table = """
  x  y  | OR  AND  XOR
 -------+-------------
  0  0  |  0   0    ?
  0  1  |  1   0    ?
  1  0  |  1   0    ?
  1  1  |  1   1    ?   """

print(table)
print()

#TASK: 
# Fill in this truth table
# Why is this XOR thing now obviously handy?
# What is 'y' in this encryption setup, and what is 'x'?

table = """
  x  y  | XOR  Y  | XOR
 -------+---------+-----
  0  0  |  ?   0  |  ?
  0  1  |  ?   1  |  ?
  1  0  |  ?   0  |  ?
  1  1  |  ?   1  |  ?   """

print(table)
print()

# TASK:
# What is 9 in binary? What is 7 in binary? and 8?
# HINT: Here is an easy way to print 8 bits of the number 9
print("9 in binary is: {:08b}".format(9))

# TASK:
# What is 9 XOR 7? What is 9 XOR 8?
# HINT: The python operator for xor is: ^
# Why are they so different?
print("xor(9, 7): {}".format(ANSWER) )
print("xor(9, 8): {}".format(ANSWER) )
print()


###################
# level 4 - bonus #
###################

# TASK:
# Without using python, calculator, google, a computer, or paper:
# What is 81276386128631862836186273 ^ 81276386128631862836186273
# (yes, the two numbers are the same)
print("The crazy large xor is: {}".format(ANSWER))

# TASK:
# Why is XOR useful for encryption?
# HINT: What might be bad about using 'or' to encrypt stuff?
#       What would be bad about using 'and' ?
