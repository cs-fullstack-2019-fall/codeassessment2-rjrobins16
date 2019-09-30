# ### Problem 3
# Given 2 lists of claim numbers, write the code to merge the 2
# lists provided to produce a new list by alternating values between the 2 lists. Once
# the merge has been completed, print the new list of claim numbers (DO NOT just print the array variable!)
# ```
# # Start with these lists
list_of_claim_nums_1 = [2, 4, 6, 8, 10]
list_of_claim_nums_2 = [1, 3, 5, 7, 9]

# ```
# Example Output:
# ```
# The newly created list contains:     2  1  4  3  6  5  8  7  10  9
# ```

new_claim_list = []
starter = 0
second = 0
# while 1 != 2:
#     for x in list_of_claim_nums_1:
#         x = starter
#     for eachnum in list_of_claim_nums_2:
#         eachnum = second
#     new_claim_list.append(starter)
#     new_claim_list.append(second)
#
#     print(new_claim_list)

for index in list_of_claim_nums_1:
    new_claim_list.append(index)


print(new_claim_list)