# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 12:09:35 2019

@author: Chigozirim
"""
def checkTwoEqualNumber(a, b, c):
    # Changing inputs to integer values
    varOne = int(a)
    varTwo = int(b)
    varThree = int(c)
    if (varOne == varTwo or varOne == varThree or varTwo == varThree):
        return True
    else:
        return False

