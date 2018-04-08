# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    print()
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for c in secretWord:
        if c not in lettersGuessed:
            return False
    return True 



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    
    for c in secretWord:
        if c in lettersGuessed:
            result = result + c + ' '
        else:
            result = result + '_ '
            
    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lettersLeft = string.ascii_lowercase
    
    for c in lettersGuessed:
        lettersLeft = lettersLeft.replace(c, '')
    
    return lettersLeft
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    livesLeft = 8
    lenWord = len(secretWord)
    availableLetters = string.ascii_lowercase
    lettersGuessed = []
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(lenWord) + " letters long.")
    
    while(True):
        print("--------------")
        if livesLeft == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
            return
        elif isWordGuessed(secretWord, lettersGuessed) == True:
            print("Congratulations, you won!")
            return
        else:
            print("You have " + str(livesLeft) + " guesses left.")
            print("Available letters: " + getAvailableLetters(lettersGuessed))
            inputLetter = input("Please guess a letter: ")
            guessLwrcase = inputLetter.lower()
            
            if guessLwrcase in lettersGuessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            elif guessLwrcase not in secretWord:
                lettersGuessed += guessLwrcase
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                availableLetters = availableLetters.replace(guessLwrcase, '')
                livesLeft -= 1
            else:
                lettersGuessed += guessLwrcase
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                availableLetters = availableLetters.replace(guessLwrcase, '')




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
