#!/usr/bin/env python3
from pathlib import Path
ANSWER = "dunno_yet"

###########
# level 1 #
###########

print("Welcome to Level 1.")
print("ASCII, encodings. Letters into numbers. Numbers into letters.")
print("---\n")

""" 
A fundamental computer science concept is that of encoding
How do we represent some useful object that we use in the world, inside the computer?
And to decode: how do we take the computer's version and translate it into
a meaningful representation?

Inside the computer, is 'q' stored as a q, or as a number? Or as bits? """

# Let's check out files/ascii.txt
f = Path(__file__).parent / "files" / "ascii.txt"
print(f.read_text())

# What are we going to do with this information?
# Does python use ascii?

# TASK: 
# Print the letter 'k' as a number
# the function ord(c) will take a character c and return the integer representation from the ascii table
print("The letter 'k' is the number: ", ANSWER)

# TASK:
# Print the number 81 as a letter
# the function chr(i) will take an integer i and return the ascii character
print("The number '81' is the letter: ", ANSWER)

# TASK:
# Print the number (integer representation) for each letter in this word
# including the space. I've started the loop for you.
word = "alphabet soup"
for letter in word:
    print("something goes here, right?")


###################
# level 1 - bonus #
###################

# TASK:
# Use the range(start,stop) function to print all the letters represented
# by the numbers 65 to 90. What does this means for how 'stop' works?
print("Here are the letters corresponding to 65 to 90:")
