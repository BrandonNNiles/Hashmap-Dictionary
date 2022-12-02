'''
console.py
Description:
    A module to provide console command implementation.
Author:
    Brandon Niles (180946050)
'''

#Imports
from hash import Hash

#Classes
class Command:
    command_list = []
    def __init__(self, id, description, func, args = []):
        self.__class__.command_list.append(self)
        self.id = id #string: a unique name
        self.description = description #string: a description, only used for help command
        self.func = func #function: code to be executed
        self.args = args #a list of arguments to be provided, only used for help command
    def __lt__(self, other):
        return self.id < other.id

#Globals
running = True
hash = None  

#Methods
'''
start_console(hash)
Starts the console-listening loop for commands.
Arguments:
    hash -> Hash: The hash table to be worked with
Returns:
    None
Outputs:
    command outputs
'''
def start_console(hashtable):
    global hash
    hash = hashtable
    while running:
        inp = input("Enter a command: ")
        if inp and inp != "":
            execute_command(inp)
    print("Exiting program. Goodbye!")

def execute_command(message):
    print()
    console_prefix = "/"
    help_id = "help"

    prefix = message[0]
    message = message[1:].split()
    id = message[0].lower()

    args = {}

    if len(message) > 1:
        args = message[1:] #if arguments exist

    found = False
    for command in Command.command_list:
        if command.id.lower() == id:
            found = True
            if len(args) >= len(command.args) and len(command.args):
                return command.func(args) #args are always passed as a list of args
            elif (args == None and command.args != [None]) or (len(args) < len(command.args)): #args required but not given
                print("Missing {} arguments, required: {}".format(len(command.args) - len(args), command.args))
            else:
                return command.func()
    
    if not found:
        print("Unknown command, type {}{} for a list of commands.".format(console_prefix, help_id))


#Commands

#Creates text into a fixed length string, helper
def f_len(text, length):
    if len(text) > length:
        text = text[:length]
    elif len(text) < length:
        text = (text + " " * (length - len(text)))
    return text

#Help command, displays a formated list of all commands
def cmdHelp():
    #header
    print("Found {} commands:\n".format(len(Command.command_list)))
    print("Command          Arguments                      Description")
    print("-------          ---------                      -----------")

    #body
    listCommands = Command.command_list
    listCommands.sort()
    for command in listCommands:
        #args formatting
        if not len(command.args):
            args = "[None]"
        else:
            args = "[" + command.args[0]
            for arg in command.args[1:]:
                args = args + " " + arg
            args = args + "]"

        row = []
        row.append(f_len("/", 1))
        row.append(f_len(command.id, 15))
        row.append(f_len(args, 30))
        row.append(f_len(command.description, 80))
        
        print("{}{} {} {}".format(*row))

Command("help", 
        "Displays all commands available.",
        cmdHelp)

def cmd_delete(args):
    word = args[0]

    result = hash.delete(word)
    if result == 0:
        print("Successfully deleted {}.".format(word))

Command("delete",
        "Attempts to delete a word from the hashtable.",
        cmd_delete,
        ["Word"]
)

def cmd_insert(args):
    word = args[0]
    definition = args[1:]

    result = hash.insert(word, definition)
    if result == 0:
        print("Successfully inserted {}.".format(word))


Command("insert",
        "Attempts to insert a definition to a word into the hash table.",
        cmd_insert,
        ["Word", "Definition"]
)

def cmd_search(args):
    word = args[0]

    definition = hash.search(word)
    if definition != None:
        print("{}: {}".format(word, definition))


Command("search",
        "Searches for a definitinon in the hash table.",
        cmd_search,
        ["Word"]
)

def cmd_quit():
    global running
    running = False


Command("quit",
        "Ends the process.",
        cmd_quit
)