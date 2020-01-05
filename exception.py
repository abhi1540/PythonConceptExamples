# def factorial(n):
#     # n! can also be defined as n * (n-1)!
#     """ calculates n! recursively """
#     if n <= 1:
#         return 1
#     else:
#         print(n/0)
#         return n * factorial(n-1)
#
# try:
#     print(factorial(900))
# except (RecursionError, OverflowError):
#     print("This program cannot calculate factorials that large")
# except ZeroDivisionError:
#     print("Division by zero")
#
#
# print("Program terminating")

import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(1)


first_number = getint("Please enter first number ")
second_number = getint("Please enter second number ")






try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)



# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()

print("Congratulations! You guessed it correctly.")