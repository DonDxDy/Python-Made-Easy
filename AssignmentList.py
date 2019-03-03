# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:30:52 2019

@author: Chigozirim
"""
"""Code to submit as fourth assignment 
In order to complete the assignment on Lists """

# Declare the Arrays
myUniqueList = []
myLeftovers = []

# Declare Function addItem
def addItem(item):
# Using the If Statement to arrange the array values
    if item not in myUniqueList:
        myUniqueList.append(item)
        return True
    else:
        myLeftovers.append(item)
        return False

#Adding values
assert (addItem("Car")) is True 
assert (addItem("Horn")) is True 
assert (addItem("Wiper")) is True
assert (addItem("Horn")) is False
assert (addItem(3)) is True 
assert (addItem(2)) is True 
assert (addItem(1)) is True 
assert (addItem(3)) is False 

#Output the values in the various arrays
print('list of Unique Items: ', myUniqueList)
print('list of Duplicated items Rejected: ', myLeftovers)