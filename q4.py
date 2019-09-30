# ### Problem 4
# Write a program that allows users to compare words by their length.
# Implement a function called chk_strings that accepts 2 strings entered by the user and compares them by length
# The function should return true if the first string parameter has more characters (i.e. longer)
# than the second string passed into the function, otherwise, the function should return false.
# DO NOT print the result in the function, print the result using the return value provided by the function. 

# Example Input/Output:
# ```
# Enter the first string: BIRD
# Enter the second string: COW

# BIRD is longer than COW
# ```
def chk_strings(word1, word2):
    if len(word1) > len(word2):
        return True
    if len(word1) < len(word2):
        return False


userWord1 = input("Enter the first string")
userWord2 = input("Enter the second string")

print(chk_strings(userWord1, userWord2))
