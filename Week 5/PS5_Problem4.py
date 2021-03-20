""" Problem Set 5 - Problem 4 - Decrypt a Story

For this problem, the graders will use our implementation of the Message, PlaintextMessage, and CiphertextMessage classes, so don't worry if you did not get the previous parts correct.

Now that you have all the pieces to the puzzle, please use them to decode the file story.txt. The file ps6.py contains a helper function get_story_string() that returns the encrypted version of the story as a string. 
Create a CiphertextMessage object using the story string and use decrypt_message to return the appropriate shift value and unencrypted story string.
"""

def decrypt_story():
    """
    loads story from story.txt document, turns into an instance of class CipherTextMessage and decrypts story
    """
    story_string = CiphertextMessage(get_story_string())
    return story_string.decrypt_message()
