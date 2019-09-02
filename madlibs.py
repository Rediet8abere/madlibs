#story from class
story = 'It was a %s, cold November day. I woke up to the %s smell of %s roasting \
in the %s downstairs. I %s down the stairs to see if I could help %s the dinner. \
My mom said, "see if %s needs a fresh %s." So I carried a tray of glasses full of \
 %s into the %s room. When I got there, I could not believe my %s! There were %s \
 %s on the %s!'


# ask user for input
def user_input(parts_of_speech):
    user_value = input("Enter %s: " % (parts_of_speech))
    if user_value.isalpha():
        return user_value
    else:

        # while input is character or while input is number
        # ask the user to re-enter
        ##work on combination of string and character
        while user_value.isalnum():
            print("Please re-enter parts of speech")
            user_value = input("Enter %s: " % (parts_of_speech))
            if user_value.isalpha():
                return user_value
                break


print('It was a %s, cold November day. I woke up to the %s smell of %s roasting \
in the %s downstairs. I %s down the stairs to see if I could help %s the dinner. \
My mom said, "see if %s needs a fresh %s." So I carried a tray of glasses full of \
 %s into the %s room. When I got there, I could not believe my %s! There were %s \
 %s on the %s!' % (user_input("adjective"), user_input("adjective"), user_input("type of bird"),
 user_input("room in a house"), user_input("verb(past tense)"), user_input("verb"),
 user_input("relative name's"), user_input("noun"), user_input("a liquid"),
 user_input("verb ending in -ing"), user_input("part of the body(plural)"), user_input("plural noun"),
 user_input("verb ending in -ing"), user_input("noun")))

def split_story(story):
    words = story.split()
    #print(words)

split_story(story)
