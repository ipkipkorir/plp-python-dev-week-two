"""
Declare an empty dictionary.

"""
person_dict = {}
#
#Ask the user to personal details
fname = input("Enter your first name:")
person_dict["first_name"] = fname

lname = input("Enter your last name:")
person_dict["last_name"] = lname

gender = input("Enter your gender:")
person_dict["gender"] = gender

age = input("Enter your age:")
person_dict["age"] = age

fav_colour = input("What's your favourite colour?")
person_dict["favourite_colour"] = fav_colour

#Print the dictionary
print("\n")
print(person_dict)
print("\n")
