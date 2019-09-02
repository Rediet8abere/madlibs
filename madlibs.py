#from colorama import *
story_builder_list = list()

#print(Fore.Red + "Build your own madlibs")

def create_story(word):
    story_builder_list.append(word)
def update_story(index, item):
    story_builder_list[index] = item

def list_all_story():
    index = 0
    for list_item in story_builder_list:
        print("{} {}".format (str(index), list_item))
        index += 1

def display_story():
    for words in story_builder_list:
        print("{}".format (words), end = " ")
    print("\n")

def index_exist(index):
    if index < len(story_builder_list):
        return True
    else:
         print("Index out of bound, please enter a value between %d and %d" % (0, len(story_builder_list)-1))

def proper_input(parts_of_speech):
    if parts_of_speech.isalpha():
        return True
    else:
         print("Improper input, please enter a word or a phrase")
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input part of story: ")
        create_story(input_item)
    # update item
    elif function_code == "U":
        item_index_tobeupdated = user_input("Index Number To be Updated? ")
        input_item_toupdate = user_input("Input item to replace: ")
        if index_exist(int(item_index_tobeupdated)) and proper_input(input_item_toupdate):
            update_story(int(item_index_tobeupdated), input_item_toupdate)
   # Print all items
    elif function_code == "L":
        list_all_story()
    elif function_code == "S":
        display_story()
    # This is where we want to stop our loop
    elif function_code == "Q":
        return False
    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for the user input
    user_input = input(prompt)
    return user_input

def test():
    create_story("It was a")
    create_story("(adjective)")
    create_story(", cold November day. ")
    create_story("I woke up to the")
    create_story("(adjective)")
    create_story("smell of")
    create_story("(type of bird)")
    create_story("roasting in the")
    create_story("(room in a house)")
    create_story("downstairs. I")
    create_story("verb(past tense)")
    create_story("down the stairs to see if I could help")
    create_story("(verb)")
    create_story("the dinner. My mom said, 'see if ")
    create_story("(relative's name)")
    create_story("(needs a fresh")
    create_story("(noun)")
    create_story(".' So I carried a tray of glasses full of")
    create_story("(a liquid)")
    create_story("into the")
    create_story("(verb ending in -ing)")
    create_story("room. When I got there, I couldn't believe my")
    create_story("(part of the body(plural))")
    create_story("! There were")
    create_story("(plural noun)")
    create_story("(verb ending in -ing)")
    create_story("on the")
    create_story("(noun)")
    print(story_builder_list)

    #list_all_story()
    #display_story()
    #update_story(1, "beatuiful")
    #update_story(4, "sweet")
    #update_story(6, "peacok")
    #display_story()
    #select("C")
    #display_story()
    #list_all_story()
    #select("U")
    #display_story()
    #list_all_story()
    #select("P")
test()
running = True
while running:
    selection = user_input("Press C to add Story to the list, S to display story, L to display story as a list, U to update a phrase/ to play and Q quit: ")
    running = select(selection.upper())
