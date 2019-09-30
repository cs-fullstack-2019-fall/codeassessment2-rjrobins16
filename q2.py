# ### Problem 2
# Prompt the user with the message, ‘Is it better to be rude or kind to People?’ 
# Keeping prompting the user to enter an answer until they enter the word kind. 
# Each time they enter something other than kind, print the message,
# ‘That’s not the answer I had hoped to hear. Try again.’ and prompt the user again.
# Once the user enters kind, print, ’Now that’s what I wanted to hear!’ and exit the program.

# prompts user and sets variable
userWord = input("Is it better to be rude or kind to People?")


# condition checks to see if they entered kind, if not it prompts again.

while userWord != "kind":
    print("That’s not the answer I had hoped to hear. Try again.")
    userWord = input("Is it better to be rude or kind to People?")

# once kind is entered they are no longer in the while loop
print("Now that’s what I wanted to hear!")
