"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
#repeat while
while True:
    input_string = raw_input("> ")
    tokens = input_string.split(" ")
    num1 = int(tokens[1])
    num2 = int(tokens[2])
    nums = tokens[1:]

    if tokens[0] == 'q':
        break

    if tokens[0] == "+":
        print add(nums)
        
    if tokens[0] == "-":
        print subtract(num1, num2)

    if tokens[0] == "*":
        print multiply(num1, num2)

    if tokens[0] == "/":
        print divide(num1, num2)

    if tokens[0] == "square":
        print square(num1)

    if tokens[0] == "cube":
        print cube(num1)

    if tokens[0] == "power":
        print power(num1, num2)

    if tokens[0] == "mod":
        print mod(num1, num2)




