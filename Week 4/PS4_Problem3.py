""" Problem Set 4 - Problem 3 - Valid Words

At this point, we have written code to generate a random hand and display that hand to the user. 
We can also ask the user for a word (Python's input) and score the word (using your getWordScore). 
However, at this point we have not written any code to verify that a word given by a player obeys the rules of the game. 

A valid word is in the word list; and it is composed entirely of letters from the current hand. 
Implement the isValidWord function.
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    wordCopy = word[:]
    handCopy = dict(hand)
    flag = False
    checkWord = True
    count = len(word)
    
    for i in wordCopy:
        if i in handCopy:
            handCopy[i] -= 1
            count -= 1
    for j in handCopy:
        if int(handCopy[j]) < 0:
            checkWord = False    
    if wordCopy in wordList and checkWord == True and count == 0:
        flag = True
    return flag
