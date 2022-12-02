'''
helper_methods.py
Description:
    A module to implement the auxiliary methods to assist main methods.
Author:
    Brandon Niles (180946050)
'''

#Methods

'''
to_num(word)
Converts a string of letters into an array of int such that
each letter is corresponding to its index in the alphabet.
Arguments:
    word -> str: word to convert
Returns:
    word_arr -> array of int: converted word
Outputs:
    None
'''
def to_num(word):
    word_array = []
    for letter in word.lower():
        word_array.append(ord(letter) - 97) #ASCII conversion
    return word_array
    
'''
valid_word(word)
Returns True if a word is valid, False otherwise.
A valid word is a 3 letter word consisting entirely of letters.
Arguments:
    word -> string: word to be evaluated
Returns:
    result -> boolean: whether or not the word is valid
Outputs:
    None
'''
def valid_word(word): #might not end up using this
    if len(word) != 3:
        return False
    return word.isalpha()
