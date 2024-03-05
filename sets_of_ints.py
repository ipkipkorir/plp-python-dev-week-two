"""
Initialize two empty sets.
Use the for-loop and the add() function to:
 - Ask the user to enter the first set of integers.
 - Ask the user to enter the second set of integers.
Use the update() function to combine the two sets to make one set.
Print the final set of integers.
"""

set1 = set()
set2 = set()

#populate the first set of integers
n1 = int(input("\nHow many integers do you need for the FIRST set?"))
for i in range(0, n1):
    set1.add(input("Enter an integer:"))
print("\nFirst set of integers:")
print(set1)

#populate the second set of integers
n2 = int(input("\nHow many integers do you need for the SECOND set?"))
for i in range(0, n2):
    set2.add(input("Enter an integer:"))
print("\nSecond set of integers:")
print(set2)

#create the final set of integers
print("\nCombine final set:")
set2.update(set1)
final_set = set2
print(final_set)
print("\n")
