# This program is an area calculator where the user enters what shape they want to find the area of, and then they
# enter the dimensions of the shape, and I return the area. The code right now is just a function for getting the
# user's shape and making sure it is actually in the list of shapes


import math
import sys
import time

# here, I am importing the libraries I need for this program to run

# this is done to read the 'shapes' text file in this program
# I also create a list of shapes to check if the user's shape is in the shapes list
file = open("shapes.txt")
shapes = []
for line in file:
    line = line.strip()
    shapes.append(line)

# print the start of the program
print("A R E A  C A L C U L A T O R")
print()


# this function is to get the user's shape and to check if that shape is even in the shape list
def printAndFindWhatShape():
    print("Here are some shapes I can find the area of:")
    allShapes = ', '.join(shapes)
    print(allShapes)
    print()
    # in a while loop that only breaks when the user's shape is valid
    while True:
        print("What shape do you want?", end=" ")
        user_shape = input().lower()
        if user_shape.isdigit() == False and user_shape in allShapes.lower():
            return user_shape
        else:
            print("Please enter a shape from the list above")


printAndFindWhatShape()
