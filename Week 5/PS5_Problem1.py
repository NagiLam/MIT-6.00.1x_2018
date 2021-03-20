""" Problem Set 5 - Problem 1 - Build the Shift Dictionary and Apply Shift

The Message class contains methods that could be used to apply a cipher to a string, either to encrypt or to decrypt a message (since for Caesar codes this is the same action).
In the next two questions, you will fill in the methods of the Message class found in ps6.py according to the specifications in the docstrings. 

In this problem, you will fill in two methods:

1. Fill in the build_shift_dict(self, shift) method of the Message class. 
Be sure that your dictionary includes both lower and upper case letters, but that the shifted character for a lower case letter and its uppercase version are lower and upper case instances of the same letter. 
What this means is that if the original letter is "a" and its shifted value is "c", the letter "A" should shift to the letter "C".

2. Fill in the apply_shift(self, shift) method of the Message class. You may find it easier to use build_shift_dict(self, shift). 
Remember that spaces and punctuation should not be changed by the cipher.
"""

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        self.dictionaryResult = {}
        lowerCase = string.ascii_lowercase
        upperCase = string.ascii_uppercase
        for letters in lowerCase:
            self.dictionaryResult.update({letters : lowerCase[((lowerCase.index(letters) + shift) % 26)]})
        for letters in upperCase:
            self.dictionaryResult.update({letters : upperCase[((upperCase.index(letters) + shift) % 26)]})
        return self.dictionaryResult

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shiftedResult = ""
        for letters in self.get_message_text():
            if letters in self.build_shift_dict(shift):
                shiftedResult += self.build_shift_dict(shift).get(letters)
            else:
                shiftedResult += letters
        return shiftedResult
