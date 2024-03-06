#create an empty list
my_list = []

#append elements to the list
#using for-loop
for i in range(10,50,10):
    my_list.append(i)
    print(my_list)
print("\nThe final list is:")
print(my_list)

#use insert() function to add an element to 
#specific index position in the list
print("\nInsert 15 into the second position \nand the list becomes:")
my_list.insert(1,15)
print(my_list)

#extend the list with another list
#using the extend() function
print("\nThe extended list is:")
my_list.extend([50,60,70])
print(my_list)

#remove and element from the list
#using the pop() function
print("\nThe list after its last element is removed:")
my_list.pop()
print(my_list)

#sort the list in ascending order
#using sort() function
print("\nThe list after being sorted in ascending order is:")
my_list.sort()
print(my_list)

#find and print the index of the value 30 in the list
print("\nThe index of 30 in the list is:")
if 30 in my_list:
    print(my_list.index(30))
else:
    print("\nNo such value in the list.")
print("\nTHE END\n:::::::::::::")
