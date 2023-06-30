# 2. Dictionary Manipulation: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.

def add_name_age(dictionary, name, age):
    dictionary[name] = age


def update_age(dictionary, name, new_age):
    if name in dictionary:
        dictionary[name] = new_age


def delete_name(dictionary, name):
    if name in dictionary:
        del dictionary[name]


# Example usage
my_dictionary = {}

add_name_age(my_dictionary, "John", 25)
print(my_dictionary)  # Output: {'John': 25}

update_age(my_dictionary, "John", 26)
print(my_dictionary)  # Output: {'John': 26}

delete_name(my_dictionary, "John")
print(my_dictionary)  # Output: {}
