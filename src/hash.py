'''
hash.py
Description:
    A module to implement the Hash class and its methods
    (Search, Insert, and Delete)
Author:
    Brandon Niles (180946050)
'''

#Imports
from helper_methods import to_num, valid_word

#Classes

#Hash class definition
class Hash:
    def __init__(self, size):
        self.map = [[[None for _ in range(size)] for _ in range(size)] for _ in range(size)] #Initializes the hash to a 26x26x26 array of None

    '''
    insert(word, definition)
    Creates an entry into the hash map given the word
    and the supplied definition
    Arguments:
        word -> string: word to be inserted
        defintiion -> string -> definition to corresponding word
    Returns:
        Error code int
    Outputs:
        Error conditions if applicable
    '''
    def insert(self, word, definition = None):
        if definition == None:
            print("Error: [Hash.insert()]: definition not specified.")
            return 1
        if not valid_word(word):
            print("Error: [Hash.insert()]: invalid 3-letter word! Given: {}".format(word))
            return 2

        if self.exists(word):
            print("Error: [Hash.insert()]: word \"{}\" already exists!".format(word))
            return 3

        word_arr = to_num(word)
        self.map[word_arr[0]][word_arr[1]][word_arr[2]] = definition
        return 0

        '''
    search(word)
    Returns the definition of a word if defined.
    Arguments:
        word -> string: word to be searched
    Returns:
        definition -> string: definition of corresponding word
    Outputs:
        Error conditions if applicable
    '''
    def search(self, word):
        if not valid_word(word):
            print("Error: [Hash.search()]: invalid 3-letter word! Given: {}".format(word))
            return
        if not self.exists(word):
            print("Error: [Hash.search()]: word \"{}\" does not exist!".format(word))
            return
        word_arr = to_num(word)
        definition = self.map[word_arr[0]][word_arr[1]][word_arr[2]]
        return definition

    '''
    delete(word)
    Deletes an entry in the hashmap if it already exists
    Arguments:
        word -> string: word to be deleted
    Returns:
        Error code int
    Outputs:
        Error conditions if applicable
    '''
    def delete(self, word):
        if not valid_word(word):
            print("Error: [Hash.delete()]: invalid 3-letter word! Given: {}".format(word))
            return 1

        if not self.exists(word):
            print("Error: [Hash.delete()]: word \"{}\" does not exist!".format(word))
            return 2

        word_arr = to_num(word)
        self.map[word_arr[0]][word_arr[1]][word_arr[2]] = None
        return 0
    '''
    exists(word)
    Returns True if a word's definition exists yet, false otherwise.
    Arguments:
        word -> string: word to be evaluated
    Returns:
        result -> boolean: whether or not the word is defined
    Outputs:
        None
    '''
    def exists(self, word):
        word_arr = to_num(word)
        definition = self.map[word_arr[0]][word_arr[1]][word_arr[2]]
        return definition != None