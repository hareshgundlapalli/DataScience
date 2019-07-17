# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:52:37 2019

Python program to validate the user input is numeric and if its odd / even

@author: Haresh
"""
import math

#Sample 1 - Accepts only integers:

value = input("Please enter a number to validate ODD/EVEN : ")
print("You have entered", value, "is in", str(type(value)), "and we are converting it to int.")
try:
    value = int(value)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

if isinstance(value, (int, float, complex)) and not isinstance(value, bool):
    value = int(value)
    if value % 2 == 0:
        print(value, "is even number.")
    elif value % 2 != 0:
        print(value, "is odd number.")
    else:
        print(value, "is not a number.")

# Sample 2 - Accepts float / integer and converts to an integer
        
value = input("Please enter a number to validate ODD/EVEN : ")
print("You have entered", value, "is in", str(type(value)), "and we are converting it to int.")
try:
    value = int(value)
except ValueError:
    try: 
        value = float(value)
    except ValueError:
        print("Invalid input. Please enter a valid Number.")

if isinstance(value, int):
    value = int(value)
    if value % 2 == 0:
        print(value, "is even number.")
    elif value % 2 != 0:
        print(value, "is odd number.")
else:
    if isinstance(value, float):
        value = math.floor(value)
        value = int(value)
        if value % 2 == 0:
            print("Floor value", value, "is even number.")
        elif value % 2 != 0:
            print("Floor value", value, "is odd number.")
    else:
        print(value, "is not a number.")


