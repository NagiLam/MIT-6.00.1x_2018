""" Prolem Set 3 - Problem 4 - The Game

Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. 
This starts up an interactive game of Hangman between the user and the computer. 
Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

Note that if you choose to use the helper functions isWordGuessed, getGuessedWord, or getAvailableLetters, you do not need to paste your definitions in the box. 
We have supplied our implementations of these functions for your use in this part of the problem. If you use additional helper functions, you will need to paste those definitions here.

Your function should include calls to input to get the user's guess.
"""

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

    lettersGuessed = []
    count = 8
    flag = "Sorry, you ran out of guesses. The word was else. "
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-----------")
    
    while (count > 0):
        
        print("You have " + str(count) + " guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        guessLowerCase = guess.lower()
        if guessLowerCase not in lettersGuessed:
            lettersGuessed += guessLowerCase
            if guessLowerCase in secretWord:
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
            elif guessLowerCase not in secretWord:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
                count -= 1
        elif guessLowerCase in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
        if getGuessedWord(secretWord, lettersGuessed) == secretWord:
            flag = "Congratulations, you won!"
            break
    return print(flag)
