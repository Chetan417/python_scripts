""" 1 TASK FACTORIAL NUMBER"""
import math

""" this task is th first to factorial of user inter the number and get the factorial of the intered number..."""
n = int(input("Enter a factorial number: "))
def factorial(n):
    if n == 0 :
        return 1
    else:
        return n * factorial(n-1)
result = factorial(n)
print(f"Factorial of {n} is : ",result)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""2 TASK OF MATH MODULE"""

from math import *

number = int(input("Enter a number: "))

Square_root = math.sqrt(number)
Natural_logarithm = math.log(number)
sine = math.sin(number)

print("Square root of the number is : ",Square_root)
print("Natural_logarithm of the number is : ",Natural_logarithm)
print("Sine of the number is : ",sine)
