'''
tests.py
Description:
    A module to test the requirements of A3.
Author:
    Brandon Niles (180946050)
'''

#Methods

'''
test_hash(hash)
Tests the various conditions of A3.
Arguments:
    hash -> Hash: Hash object to refer to
Returns:
    None
Outputs:
    Test output
'''
def test_hash(hash):
    temp_definition = "Test definition"
    #Test insert
    print("Testing hash.insert():\n")
    print("insert(aaa) - expected: valid")
    hash.insert("aaa", temp_definition)
    print("insert(bBb) - expected: valid")
    hash.insert("bBb", temp_definition) #valid word, capitalization handled internally
    print("insert(bbb) - expected: error: word already exists")
    hash.insert("bbb", temp_definition) #expected error, word already exists (capitalization handled internally)
    print("insert(aaa) - expected: error: word already exists")
    hash.insert("aaa", temp_definition) #expected error, word already exists
    print("insert(aaaa) - expected: error: invalid word (length > 3)")
    hash.insert("aaaa", temp_definition)
    print("insert(a!c) - expected: error: invalid word (non-alphabetic)")
    hash.insert("a!c", temp_definition)
    print("insert(bcb) without definition - expected: error: no definition")
    hash.insert("bcb")

    #Test delete
    print("\nTesting hash.delete():\n")
    print("delete(aaa) - expected: valid")
    hash.delete("aaa")
    print("delete(aaa) - expected: error: word does not exist")
    hash.delete("aaa")
    print("delete(aaaa) - expected: error: invalid word")
    hash.delete("aaaa")

    #Test search
    print("\nTesting hash.search():\n")
    print("search(mmm) - expected: error: word does not exist")
    print(hash.search("mmm"))
    print("Inserting mmm with definition.")
    hash.insert("mmm", temp_definition)
    print("search(mmm) - expected: valid: definition is shown")
    print(hash.search("mmm"))
    print("Deleting mmm.")
    hash.delete("mmm")
    print("search(mmm) - expected: error: word does not exist")
    print(hash.search("mmm"))
    print("search(mmmm) - expected: error: invalid word, output: None")
    print(hash.search("mmmm"))
    
    #Delete all useless test entries
    hash.delete("bbb")
