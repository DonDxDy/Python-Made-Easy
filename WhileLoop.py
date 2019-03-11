# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:19:53 2019

@author: Chigozirim

Solution for the #6 Homework
"""
# try:
# Import utility to check terminal size 
import shutil

# define row/column parameters:
ROWS = 17
COLUMNS = 17

#  Validate the rows/columns parameters against what is returned by utility 
def pos(rows, cols):
    maxWidth, maxHeight = shutil.get_terminal_size()
    ifValid = True
    if (rows > maxHeight):
        print(rows,' parameter is greater than the max height (',maxHeight,')')
        ifValid = False
    if (cols > maxWidth):
        print(cols, ' parameter is greater than the max width (',maxWidth,')')
        ifValid = False
    return ifValid


def playboard(rows, cols):
    if pos(rows, cols) == False:
        return False
    for row in range (rows):
        if row % 2 == 0:
            # we need to draw the columns
            for col in range (cols):
                if col % 2 == 0:
                    print(" ", end="")
                else:
                    print("|", end="")
        else:
            #  we need to draw the separator
            for col in range (cols):
                print("-", end="")
        print("") 

# execute the function playboard
playboard(ROWS, COLUMNS)



