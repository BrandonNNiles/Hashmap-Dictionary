'''
main_methods.py
Description:
    A module to load all entries from an external source into the hashmap.
Author:
    Brandon Niles (180946050)
'''

#Imports
from helper_methods import valid_word

#Classes
#Word class definition
class Word:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition

#Methods

'''
get_words(filename)
Loads and interprets all word - definition pairs.
Returns an array of Word objects.
Arguments:
    filename -> string: filename to examine
Returns:
    word_array -> array of Word: array of Word objects (see Word class)
Outputs:
    None
'''
def get_words(filename):
    word_array = []
    f = open(filename, 'r')

    file_lines = []

    for line in f: #convert iterable into an array
        if line != "\n" and line != "" and line != " ":
            file_lines.append(line.strip())

    i = 0
    while(i < len(file_lines)): #filter out garbage
        line = file_lines[i]
        word = line.split()[0]
        if not (word.isupper() and word.isalpha() and valid_word(word)):
            file_lines[i - 1] = file_lines[i - 1] + " " + file_lines[i]
            del file_lines[i]
        else:
            i = i + 1
    
    for line in file_lines: #add Word objects to return arrays
        line = line.split()
        word = line[0]
        definition = " ".join(line[1:])
        word_array.append(Word(word, definition))


    return word_array
