"""
Initialize a list of words.
Initialize another list to hold the results of the list comprehension.
Print the new list
"""
list_of_words = ["Our", "home", "land", "is", "Kenya"]

odd_num_words = [ word for word in list_of_words if len(word)%2==1]
print(odd_num_words)