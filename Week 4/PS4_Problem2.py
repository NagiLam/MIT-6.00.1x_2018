""" Problem Set 4 - Problem 2 - Dealing with Hands

**Please read this problem entirely!!** The majority of this problem consists of learning how to read code, which is an incredibly useful and important skill. At the end, you will implement a short function. 
Be sure to take your time on this problem - it may seem easy, but reading someone else's code can be challenging and this is an important exercise.

Implement the updateHand function. Make sure this function has no side effects: i.e., it must not mutate the hand passed in. Before pasting your function definition here, be sure you've passed the appropriate tests in test_ps4a.py.
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    handCopy = dict(hand)
    for letters in word:
        if letters in handCopy:
            handCopy[letters] -= 1
    return handCopy
