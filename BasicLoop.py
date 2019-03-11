# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:19:53 2019

@author: Chigozirim

This Solution is built for Homework #5 to explain the Fizz Buzz
basic loop steps
"""

def divisibleBy3(nos):
	return nos%3 == 0

def divisibleBy5(nos):
	return nos%5 == 0
	
def primeNo(nos):
	divisor = []
	
	for w in range(1, nos +1):
		if nos % w == 0:
			if len(divisor) > 1:
				return False
			divisor.append(w)
	if len(divisor) == 2:
		return True 
	
def fizzbuzz():
    
    for w in range(1, 101):
        # Checking for prime or not
        if primeNo(w):
            print('prime')
            continue

        
        # Variable used to decide whether print number or not
        printW = True

        if divisibleBy3(w):
            print('Fizz', end='')
            printW = False

        if divisibleBy5(w):
            print('Buzz', end='')
            printW = False

        if printW:
            print(w, end='')

        # We need custom ending in print statements above
        print()
		
fizzbuzz()