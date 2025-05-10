"""
Simple Python Calculator

Author: Abinash Prasana

This script allows the user to perform basic arithmetic operations
(+ - * /) between two floating-point numbers entered via the terminal.
It validates the operator and rounds the result to 2 decimal places.
"""

op = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter a 1st number: "))
num2 = float(input("Enter a 2nd number: "))
if op == "+":
    result = num1 + num2
    print(f"The result is {round(result,2)}")
elif op == "-":
    result = num1 - num2
    print(f"The result is {round(result,2)}")
elif op == "*":
    result = num1 * num2
    print(f"The result is {round(result,2)}")
elif op == "/":
    result = num1 / num2
    print(f"The result is {round(result,2)}")
else:
    print("Invalid operator")