# ### Problem 1
# Ask the user to enter a number. 
# Using the provided list of numbers, use a for loop to iterate
# the array and print out all the values that are smaller than the user input and print
# out all the values that are larger than the number entered by the user.

# ```
# # Start with this List
list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
# ```
# Example Input/Output if the user enters the number 9:
# ```
# The User entered 9
# 1  2  7 are smaller than 9
# 12  24  34  10 are larger than 9
# ```
#ASK USER FOR NUMBER and turns into an integer
userNumber = int(input("Enter a number"))

# initiates a new array for smaller and larger numbers
smallernumbers = []
largernumbers = []


# compares the value to each number in the original array and adds that value to its respective array (smaller or larger)
for eachnumber in list_of_many_numbers:
    if eachnumber < userNumber:
        smallernumbers.append(eachnumber)

    if eachnumber > userNumber:
        largernumbers.append(eachnumber)
print(f"{smallernumbers} are smaller than {userNumber}")
print(f"{largernumbers} are larger than {userNumber}")
