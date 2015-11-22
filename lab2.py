#!/usr/bin/env python3

""" Graded Lab #2 for Inf1340, Fall 2015 """


"""
Instructions: Add a function to to get input from the user and use that
function in name_that_shape()

The function should prompt the user for input until a legal value is
entered. A legal value is any integer.

"""


def name_that_shape():
    sides = get_user_input()
    if sides == 3:
        print("triangle")
    elif sides == 4:
        print("quadrilateral")
    elif sides == 5:
        print("pentagon")
    elif sides == 6:
        print("hexagon")
    elif sides == 7:
        print("heptagon")
    elif sides == 8:
        print("octagon")
    elif sides == 9:
        print("nonagon")
    elif sides == 10:
        print("decagon")
    else:
        print("Error")


def get_user_input():
    value = ""
    input_is_an_integer = False
    while input_is_an_integer == False:
        value = raw_input("Number of sides:")
        if value.isdigit() == True or value[0] == "-" and value[1:].isdigit() == True:
            value = int(value)
            input_is_an_integer = True
    return value

name_that_shape()
