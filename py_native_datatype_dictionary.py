# Python Dictionary
# Python dictionary is an unordered collection of items.
# While other compound data types have only value as an element, a dictionary has a key: value pair.

# +How to create a dictionary?
# Creating a dictionary is as simple as placing items inside curly braces {} separated by comma.
# An item has a key and the corresponding value expressed as a pair, key: value.
# While values can be of any data type and can repeat,
# keys must be of immutable type (string, number or tuple with immutable elements) and must be unique.
my_dict = {}  # empty dictionary
my_dict = {1: 'apple', 2: 'ball'}  # dictionary with integer keys
my_dict = {'name': 'John', 1: [2, 4, 3]}  # dictionary with mixed keys
my_dict = dict({1: 'apple', 2: 'ball'})  # using dict()
my_dict = dict([(1, 'apple'), (2, 'ball')])  # from sequence having each item as a pair

# +How to access elements from a dictionary?
# Dictionary uses keys. Key can be used either inside square brackets or with the get() method.
# The difference while using get() is that it returns None instead of KeyError, if the key is not found.
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict['name'])  # Output: Jack
print(my_dict.get('age'))  # Output: 26
# Trying to access keys which doesn't exist throws error
my_dict.get('address')  # None
my_dict['address']  # KeyError: 'address'

# +How to change or add elements in a dictionary?
# Dictionary are mutable. We can add new items or change the value of existing items using assignment operator.
# If the key is already present, value gets updated, else a new key: value pair is added to the dictionary.
my_dict = {'name': 'Jack', 'age': 26}
my_dict['age'] = 27  # update value
print(my_dict)  # Output: {'age': 27, 'name': 'Jack'}
my_dict['address'] = 'Downtown'  # add item
print(my_dict)  # Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}

# +How to delete or remove elements from a dictionary?
# We can remove a particular item in a dictionary by using the method pop().
# This method removes as item with the provided key and returns the value.
# The method, popitem() can be used to remove and return an arbitrary item (key, value) form the dictionary.
# All the items can be removed at once using the clear() method.
# We can also use the del keyword to remove individual items or the entire dictionary itself.
#
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}  # create a dictionary
# remove a particular item
print(squares.pop(4))  # Output: 16
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 5: 25}
# remove an arbitrary item
print(squares.popitem())  # Output: (1, 1)
print(squares)  # Output: {2: 4, 3: 9, 5: 25}
# delete a particular item
del squares[5]
print(squares)  # Output: {2: 4, 3: 9}
# remove all items
squares.clear()
print(squares)  # Output: {}
# delete the dictionary itself
del squares
print(squares)  # Throws Error

# +Python Dictionary Methods
# clear()	Remove all items form the dictionary.
# copy()	Return a shallow copy of the dictionary.
# fromkeys(seq[, v])	Return a new dictionary with keys from seq and value equal to v (defaults to None).
# get(key[,d])	Return the value of key. If key doesn't exit, return d (defaults to None).
# items()	Return a new view of the dictionary's items (key, value).
# keys()	Return a new view of the dictionary's keys.
# pop(key[,d])	Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError.
# popitem()	Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.
# setdefault(key[,d])	If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).
# update([other])	Update the dictionary with the key/value pairs from other, overwriting existing keys.
# values()	Return a new view of the dictionary's values
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
print(marks)  # Output: {'English': 0, 'Math': 0, 'Science': 0}
list(sorted(marks.keys()))  # Output: ['English', 'Math', 'Science']

# +Python Dictionary Comprehension
# Dictionary comprehension consists of an expression pair (key: value) followed by for statement inside curly braces {}.
squares = {x: x * x for x in range(6)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

odd_squares = {x: x * x for x in range(11) if x % 2 == 1}
print(odd_squares)  # Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# +Dictionary Membership Test
#
# -We can test if a key is in a dictionary or not using the keyword in.
# Notice that membership test is for keys only, not for values.
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(1 in squares)  # Output: True
print(2 not in squares)  # Output: True
# membership tests for key only not value
print(49 in squares)  # Output: False
#
# -Iterating Through a Dictionary
# Using a for loop we can iterate though each key in a dictionary.
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])
#
# -Built-in Functions with Dictionary
# Built-in functions like all(), any(), len(), cmp(), sorted() etc. are commonly used with dictionary to perform different tasks.
# all()	Return True if all keys of the dictionary are true (or if the dictionary is empty).
# any()	Return True if any key of the dictionary is true. If the dictionary is empty, return False.
# len()	Return the length (the number of items) in the dictionary.
# cmp()	Compares items of two dictionaries.
# sorted()	Return a new sorted list of keys in the dictionary.
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(len(squares))  # Output: 5
print(sorted(squares))  # Output: [1, 3, 5, 7, 9]
