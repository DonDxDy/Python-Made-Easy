# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:25:42 2019

@author: Chigozirim
"""

songDict = {'Artist' : "Olamide", 'Genre' : "Afro-pop", 'Song' : "Woske", 'DurationInSeconds' : "230", 'ReleaseYear' : "2019", 'RecordLabel' : "YNBL", 'ProducedBy' : "KillerTunes"}


		
# check the guess against the dictionary
def guessSongDetails(keyGuess, valueGuess):
    return keyGuess in songDict and songDict[keyGuess] == valueGuess

# checking the right Key and Key Values
assert guessSongDetails("Artist" , "Olamide") is True, 'Valid Key and Key value'
assert guessSongDetails("Genre", "Afro-pop") is True, 'Valid Key and Key value'
assert guessSongDetails("Song" , "Woske") is True, 'Valid Key and Key value'
assert guessSongDetails("DurationInSeconds", "230") is True, 'Valid Key and Key value'
assert guessSongDetails("ReleaseYear", "2019") is True, 'Valid Key and Key value'
assert guessSongDetails("RecordLabel", "YNBL") is True, 'Valid Key and Key value'
assert guessSongDetails("ProducedBy", "KillerTunes") is True, 'Valid Key and Key value'
# check checking to handle any key or key value wrong
assert guessSongDetails(None, None) is False, 'Wrong Combination of Key and Key Value'

# define the guessing game
def runGuessingGame():
    letsPlay = True
    while (letsPlay):
        keyGuess = input('Type in the "Key" (Note:This is a song categorization and keys are Case Senstive): ')
        valueGuess = input('Type in your "Values" (Note:This is a value relating to the categorization and values are Case Senstive): ')
        if guessSongDetails(keyGuess, valueGuess) == True:
            msg = 'Great! your guess was right!!! '
        else:
            msg = 'Wrong Answer... Do try again'
        print(msg)

        tryAgain = input('Would you want to try again? [y/n] ')
        if (tryAgain == 'n'):
            letsPlay = False
            
#Run the guessing game
runGuessingGame()