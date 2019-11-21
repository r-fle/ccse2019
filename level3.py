#!/usr/bin/env python3
from pathlib import Path
import string
ANSWER = "dunno_yet"

###########
# level 3 #
###########

print("Welcome to Level 3.")
print("Caeser cipher from a mysterious text file")
print("---\n")

""" There is text living in: files/mysterious.txt

You've got to try and figure out what the secret message contained in it is. 
The enemy have hidden it in between lots of junk, but one of our operatives 
suspects it may contain references to a computer scientist born in 1815.
"""

# TASK:
# Load the file. Find the hidden message and decrypt it.
# Feel free to copy in any code from previous levels that you need.

# EXAMPLE CODE:
# 1. Tell python where our file is
# 2. Read in the file content
# 3. Split the file content up into lines
f = Path(__file__).parent / "files" / "mysterious.txt"
content = f.read_text()
all_lines = content.split("\n")

# Let's check out the first 5 lines. What's in this file?
for i in range(5):
    print(all_lines[i])
print()

# Time to do some secret message hunting...
for line in all_lines:
    # Something goes here, right?
    print(".", end="")

print("\n")
print("The solution is:", ANSWER)


###################
# level 3 - bonus #
###################

# TASK
# Depending how you accomplished the above, there might have been another solution.
# Did you encrypt first, or decrypt first?

# TASK
# What would you do if you didn't know any of the plaintext content?
# Is there a way to score how likely it is that a given result is correct?
