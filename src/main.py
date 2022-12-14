'''
main.py
Description:
    Main executable module.
Author:
    Brandon Niles (180946050)
'''

#imports
from hash import Hash
from mass_load import get_words
from console import start_console

#Constants
filename = "../data/words.txt" #file to access stored word defintions

def start_dictionary():
    hash = Hash(26)

    loaded_words = get_words(filename)

    for word in loaded_words:
        hash.insert(word.word, word.definition)
    
    start_console(hash)



#Driver code
start_dictionary()
