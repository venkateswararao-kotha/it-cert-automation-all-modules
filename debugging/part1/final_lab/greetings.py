#!/usr/bin/env python3
'''
When we look at the code, we can see that there are two different data types used, string and int.
The variable name takes
string values and the variable number stores integer (int) values.

So, the print statement within the script concatenates both string and integer values,
which is causing the error.

print("hello " + name + ", your random number is " + number)

So, we can conclude that the root cause of the issue is within the print statement,
which is trying to concatenate two different data types (i.e., string and int).
'''
import random

def greeting():
  name = input("Hello!, What's your name?")
  number = random.randint(1,101)
  #print("hello " + name + ", your random number is " + number)
  print("hello " + name + ", your random number is " + str(number))  # This line is the fix for above line

greeting()