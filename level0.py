#!/usr/bin/env python3

############
# level 0  #
############

# Hello! Welcome to this CCSE session.
# 
# These examples are programs written in python.
# You can refer back to this if you need to know the
# syntax for if, loops, functions, and stuff.
# 
# Every line starting with '#' is a comment. It 
# doesn't change what happens when the program is run.
#
# The very first line is to make this file work on 
# non-windows computers :)


# --- PRINTING AND VARIABLES ---

# Here is how we output stuff. It's called 'print':
print("Welcomet to level0.")

# Here is how we set a variable
x = "apple"

# And how we print it out:
print("Some fruit:", x)

# There are other variable types, and maths things:
y = 5 * 2
z = 13 + 1
print("y:", y, "and z:", z, "so y plus z?", y + z)

# We can call print without text in quotes:
print(256 / 15)
print(2**8)
print()


# --- IFs and LOOPs ---

# Often you only want to do something if some condition is met:
x = 7
s = "a big furry cat sitting in front of the fire"

if (x == 7) and (y > 9):
    print("x is 7, y is bigger than 9")

if "cat" in s:
    print("s contains a cat!")
else:
    print("No cat found.")

# Really often, you want to loop.
# In python we often use 'for' to do this.
for letter in "courgette":
    print(letter, end="-")

# New lines on demand
print("\n")

# Or using numbers. What will this print?
for i in range(8):
    print("Range 8?", i)


# --- DEFINING FUNCTIONS OF OUR OWN ---

# You can just write your own functions, huzzah.
# They start with 'def' (for "define"), the names
# of the variables in some brackets, and a colon:
def countdown(i):    
    if (i > 50):
        print("Woah. Too big man!")
        # return means 'leave the function with this answer'
        return -1

    # while is like a 'for' loop and an 'if' combined
    while (i > 0):
        print(i)
        i = i - 1

# Then we can call our function. The 'i' in the function
# above gets replaced by '10', then it runs!
print("\nCalling 'countdown' function:")
countdown(10)
print()

# You can stop here if you want to keep things simple :)


###################
# level 0 - bonus #
###################

# --- Inbuilt length checker (len) ---

# len(s) is a built in way of saying "how long is s?"
if len(s) == 44:
    print("s is exactly 44 characters!")

# We can combine loops, with ifs, and len():
# Remember, s is the long string about the cat
countf = 0
for i in range(len(s)):
    # Here we get a particular letter, using
    # i as the 'index' into the string s
    if s[i] == "f":
        countf += 1
print("How many fs did we find?", countf)


# --- IMPORTING STANDARD LIBRARIES ---

# Some extra stuff is available if you import it
# (import lines normally live at the top of a file)
import string
print("Here are lots of letters: {}\n".format(string.ascii_uppercase) )
# The {} got replaced by what was in the format() brackets.

import math
x = (137 / 24)
print("x: ", x)
print("x: ", math.ceil(x), "[ceiling]" )
print("x: ", math.floor(x), "[floor]" )
print()

# --- READING FROM A FILE ---

# How do we open a file? This will look in your current folder for README.md:
with open("README.md", 'r') as f:
     # It's open. Let's get all the lines!
     for line in f:
         if "encryption" in line:
             # We'll run 'strip' to avoid printing two newlines
             print(line.strip())

# Here is a different way, but more familiar to some. Good if sharing code 
# across Windows, Mac, and Linux
from pathlib import Path
f = Path("files/example.txt")
content = f.read_text() # We could also do .read_bytes() if we wanted
print(content)

# --- OTHER THINGS & DOCUMENTATION

# Here's a huge list of stuff you can import: 
# https://docs.python.org/3/library/index.html

# A common one is passing arguments/parameters to your python program
# Imagine we ran: ./level0.py 4567
import sys

# The arguments live in sys.argv, which is a 'list' 
if len(sys.argv) > 1:
    # We have been sent one or more arguments:
    for argument in sys.argv:
        print("{}".format(argument) )
    print()

# If you are using python on the command line, you can
# exit sometimes by pressing ctrl+D, or always by typing:
exit()
