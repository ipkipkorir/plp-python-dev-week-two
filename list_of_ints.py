"""
Declare an empty list.
Prompt the user for the size of the list, i.e the number of integers to enter.
Accept the size of the list and convert it to integer.
Use the range-function and the for-loop to capture the user input.
Append the user input to the empty list.
Print the final list with a message.
"""
user_input = []

print("\nHow many integers do want list?\n")
n = input()
for i in range(0,int(n)):
    user_input.append(input("\nEnter an integer:\n"))
    print(user_input)
    print("\n")

#Print the final list
print("Here's the final List: \n")
print(user_input)
print("\n")