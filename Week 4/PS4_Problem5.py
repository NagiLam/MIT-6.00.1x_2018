""" Problem Set 4 - Problem 5 - Playing a Hand

In ps4a.py, note that in the function playHand, there is a bunch of pseudocode. 
This pseudocode is provided to help guide you in writing your function. 
Check out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode before you start coding your solution.

Note: Do not assume that there will always be 7 letters in a hand! 
The parameter n represents the size of the hand.

Testing: Before testing your code in the answer box, try out your implementation as if you were playing the game. 
"""

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """

    if "chayote" in wordList:
        wordList.remove("chayote")
    totalPoint = 0

    while (calculateHandlen(hand) > 0):
        print("Current Hand: ", end="")
        displayHand(hand)
        userInput = input("Enter word, or a '.' to indicate that you are finished: ")

        if userInput == ".":
            print("Goodbye! Total score: " + str(totalPoint) + " points.")
            break
        else:
            if (userInput not in wordList):
                print("Invalid word, please try again.")
            else:              
                totalPoint += getWordScore(userInput, n)
                print(str(userInput) + " earnd " + str(getWordScore(userInput, n)) + " points. Total: " + str(totalPoint) + " points")            
                hand = updateHand(hand, userInput)
                
    if (calculateHandlen(hand) == 0):
        print("Run out of letters. Total score: " + str(totalPoint) + " points.")

