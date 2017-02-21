# + Python List
# List is an ordered sequence of items. It is one of the most used datatype in Python and is
# very flexible. All the items in a list do not need to be of the same type.
# Lists are mutable, meaning, value of elements of a list can be altered.
a = [1, 2.0, 'python']

# + Nested list are accessed using nested indexing.
n_list = ["Happy", [2, 0, 1, 5]]
''' Output: a'''
print(n_list[0][1])
''' Output: 5'''
print(n_list[1][3])

# + Negative indexing
# Python allows negative indexing for its sequences. The index of -1 refers to the last item,
# -2 to the second last item and so on.
my_list = ['p', 'r', 'o', 'b', 'e']
''' Output: e'''
print(my_list[-1])
''' Output: '''
print(my_list[-5])

# + How to slice lists in Python?
# We can access a range of items in a list by using the slicing operator (colon).
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
''' elements 3rd to 5th, ['o', 'g', 'r']'''
print(my_list[2:5])
''' elements beginning to 4th, ['p', 'r', 'o', 'g']'''
print(my_list[:-5])
''' elements 6th to end, ['a', 'm', 'i', 'z']'''
print(my_list[5:])
''' elements beginning to end'''
print(my_list[:])

# + How to change or add elements to a list?
# List are mutable, meaning, their elements can be changed unlike string or tuple.
''' mistake values'''
odd = [2, 4, 6, 8]
''' change the 1st item'''
odd[0] = 1
''' Output: [1, 4, 6, 8]'''
print(odd)
''' change 2nd to 4th items'''
odd[1:4] = [3, 5, 7]
''' Output: [1, 3, 5, 7]'''
print(odd)

# We can add one item to a list using append() method or add several items using extend() method
odd = [1, 3, 5]
odd.append(7)
''' Output: [1, 3, 5, 7]'''
print(odd)
odd.extend([9, 11, 13])
''' Output: [1, 3, 5, 7, 9, 11, 13]'''
print(odd)
# We can also use + operator to combine two lists. This is also called concatenation.
# The * operator repeats a list for the given number of times.
odd = [1, 3, 5]
''' Output: [1, 3, 5, 9, 7, 5]'''
print(odd + [9, 7, 5])
''' Output: ["re", "re", "re"]'''
print(["re"] * 3)
# Furthermore, we can insert one item at a desired location by using the method insert()
# or insert multiple items by squeezing it into an empty slice of a list.
odd = [1, 9]
odd.insert(1, 3)
''' Output: [1, 3, 9]'''
print(odd)
odd[2:2] = [5, 7]
''' Output: [1, 3, 5, 7, 9]'''
print(odd)

# +How to delete or remove elements from a list?
# We can delete one or more items from a list using the keyword del. It can even delete the list entirely.
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
''' delete one item'''
del my_list[2]
''' Output: ['p', 'r', 'b', 'l', 'e', 'm']'''
print(my_list)
''' delete multiple items'''
del my_list[1:5]
''' Output: ['p', 'm']'''
print(my_list)
''' delete entire list'''
del my_list
'''Error: List not defined'''
print(my_list)

# We can use remove() method to remove the given item or pop() method to remove an item at the given index.
# The pop() method removes and returns the last item if index is not provided.
# This helps us implement lists as stacks (first in, last out data structure).
# We can also use the clear() method to empty a list.
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
my_list.remove('p')
''' Output: ['r', 'o', 'b', 'l', 'e', 'm']'''
print(my_list)
''' Output: 'o' '''
print(my_list.pop(1))
''' Output: ['r', 'b', 'l', 'e', 'm']'''
print(my_list)
''' Output: 'm' '''
print(my_list.pop())
''' Output: ['r', 'b', 'l', 'e']'''
print(my_list)
my_list.clear()
''' Output: []'''
print(my_list)
# Finally, we can also delete items in a list by assigning an empty list to a slice of elements.
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
my_list[2:3] = []
my_list[2:5] = []

# +Python List Methods
# append() - Add an element to the end of the list
# extend() - Add all elements of a list to the another list
# insert() - Insert an item at the defined index
# remove() - Removes an item from the list
# pop() - Removes and returns an element at the given index
# clear() - Removes all items from the list
# index() - Returns the index of the first matched item
# count() - Returns the count of number of items passed as an argument
# sort() - Sort items in a list in ascending order
# reverse() - Reverse the order of items in the list
# copy() - Returns a shallow copy of the list

# +List Comprehension: Elegant way to create new List
# List comprehension is an elegant and concise way to create new list from an existing list in Python.
# List comprehension consists of an expression followed by for statement inside square brackets.
pow2 = [2 ** x for x in range(10)]
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)
# This code is equivalent to
pow2 = []
for x in range(10):
    pow2.append(2 ** x)

# A list comprehension can optionally contain more for or if statements.
# An optional if statement can filter out items for the new list.
pow2 = [2 ** x for x in range(10) if x > 5]
odd = [x for x in range(20) if x % 2 == 1]
xy = [x + y for x in ['Python ', 'C '] for y in ['Language', 'Programming']]

# +List Membership Test
# We can test if an item exists in a list or not, using the keyword in.
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
# Output: True
print('p' in my_list)
# Output: False
print('a' in my_list)
# Output: True
print('c' not in my_list)

# +Iterating Through a List
# Using a for loop we can iterate though each item in a list.
for fruit in ['apple', 'banana', 'mango']:
    print("I like", fruit)

# +Built-in Functions with List
# all()	Return True if all elements of the list are true (or if the list is empty). 0 is false, '0' is true
print(all([0, False]))
# any()	Return True if any element of the list is true. If the list is empty, return False.
print(any([0, False]))
# enumerate() Return an enumerate object. It contains the index and value of all the items of list as a tuple.
# len()	Return the length (the number of items) in the list.
testList = [1, 2, 3]
print(testList, 'length is', len(testList))
# list()	Convert an iterable (tuple, string, set, dictionary) to a list.
# max()	Return the largest item in the list.
print('Maximum is:', max(1, 3, 2, 5, 4))
num = [15, 300, 2700, 821]; num1 = [12, 2]; num2 = [34, 567, 78]
print('Maximum is:', max(num, num1, num2, key=len))
# min()	Return the smallest item in the list
# sorted()	Return a new sorted list (does not sort the list itself).
pyList = ['e', 'a', 'u', 'o', 'i']
print(sorted(pyList))
# sum()	Return the sum of all elements in the list.
numbers = [2.5, 3, 4, -5]
sum(numbers)
sum(numbers, 10)
# If you need to add floating point numbers with exact precision then, you should use math.fsum(iterable) instead
