# Assignment 27

# 1. Write a python script to create a ArithmeticError

try:
    a = 100 / 0
    print(a)
except ZeroDivisionError:
    print("Zero Division Exception Raised.")
else:
    print("Success, no error!")

# 2. Write a python script to create a ValueError

try:
    print(float('Ineuron'))
except ValueError:
    print('ValueError: could not convert string to float: \'Ineuron\'')
else:
    print('Success, no error!')

# 3. Write a python script to handle the ArithmeticError

try:
    arithmetic = 5/0
    print(arithmetic)
except ArithmeticError:
    print('You have just made an Arithmetic error')

# 4. Write a python script to handle a ValueError

import math

x = int(input('Please enter a positive number:\n'))

try:
    print(f'Square Root of {x} is {math.sqrt(x)}')
except ValueError as ve:
    print(f'You entered {x}, which is not a positive number.')

# 5. Write a python script to handle multiple Exception in one try

string = input()

try:
    num = int(input())
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)

# 6. Write a python script to create a calculator with 4 basic operations, and handle a maximum number of exceptions.

"""
This is program for a basic arithimatic calculator 
"""
loop = 1

choice = 0

while loop == 1:
    # print out the options you have
    print("Welcome to calculator.py")

    print("your options are:")

    print(" ")
    print("1) Addition")
    print("2) Subtraction")

    print("3) Multiplication")

    print("4) Division")
    print("5) Quit calculator.py")
    print(" ")

    choice = input("choose your option: ")
    try:
        if choice == 1:
            add1 = input("add this: ")
            add2 = input("to this: ")
            print(add1, "+", add2, "=", add1 + add2)
        elif choice == 2:
            sub1 = input("Subtract this ")
            sub2 = input("from this")
            print(sub1, "-", sub2, "=", sub1 - sub2)
        elif choice == 3:
            mul1 = input("Multiply this: ")
            mul2 = input("with this: ")
            print(mul1, "x", mul2, "=", mul1 * mul2)
        elif choice == 4:
            div1 = input("Divide this: ")
            div2 = input("by this: ")
            if div2 == 0:
                print("Error! Cannot divide by zero!  You'll destroy the universe! ;")
            else:

                print(div1, "/", div2, "=", div1 * div2)
        elif choice == 5:
            loop = 0
        else:
            print("%d is not valid input. Please enter 1, 2 ,3 ,4 or 5." % choice)

    except ValueError:
        print("%r is not valid input.  Please enter 1, 2, 3, 4 or 5." % choice)

# 7. Write a python script to add a finally block for the above script

loop = 1

choice = 0

while loop == 1:
    # print out the options you have
    print("Welcome to calculator.py")

    print("your options are:")

    print(" ")
    print("1) Addition")
    print("2) Subtraction")

    print("3) Multiplication")

    print("4) Division")
    print("5) Quit calculator.py")
    print(" ")

    choice = input("choose your option: ")
    try:
        if choice == 1:
            add1 = input("add this: ")
            add2 = input("to this: ")
            print(add1, "+", add2, "=", add1 + add2)
        elif choice == 2:
            sub1 = input("Subtract this ")
            sub2 = input("from this")
            print(sub1, "-", sub2, "=", sub1 - sub2)
        elif choice == 3:
            mul1 = input("Multiply this: ")
            mul2 = input("with this: ")
            print(mul1, "x", mul2, "=", mul1 * mul2)
        elif choice == 4:
            div1 = input("Divide this: ")
            div2 = input("by this: ")
            if div2 == 0:
                print("Error! Cannot divide by zero!  You'll destroy the universe! ;")
            else:

                print(div1, "/", div2, "=", div1 * div2)
        elif choice == 5:
            loop = 0
        else:
            print("%d is not valid input. Please enter 1, 2 ,3 ,4 or 5." % choice)

    except ValueError:
        print("%r is not valid input.  Please enter 1, 2, 3, 4 or 5." % choice)
    finally:
        print("Thank you for using calculator.py!")
# 8. Write a python script to implement try except and else block for division


def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)


# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)

# 9. Write a python script to raise a ValueError.


def num_stats(x):
    if x is not int:
        raise TypeError('Work with Numbers Only')
    if x < 0:
        raise ValueError('Work with Positive Numbers Only')

    print(f'{x} square is {x * x}')
    print(f'{x} square root is {math.sqrt(x)}')

# 10. Write a python script to implemented a nested Try Except block


try:
    print("outer try block")
    try:
        print("Inner try block")
    except ZeroDivisionError:
        print("Inner except block")
except:
    print("outer except block")
