# A set is an unordered collection of items.
# Every element is unique (no duplicates) and must be immutable (which cannot be changed).
# However, the set itself is mutable. We can add or remove items from it.
# Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.
# 并集，交集，对称差分等操作

# +How to create a set?
# A set is created by placing all the items (elements) inside curly braces {},
# separated by comma or by using the built-in function set().
# It can have any number of items and they may be of different types (integer, float, tuple, string etc.).
# But a set cannot have a mutable element, like list, set or dictionary, as its element.
# set of integers
my_set = {1, 2, 3}
# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
# we can make set from a list
my_set = set([1, 2, 3, 2])
#
# Create an empty set use set() without any argument, cause {} will create an empty dictionary
print(type({}))  # Output: <class 'dict'>
print(type(set()))  # Output: <class 'set'>

# +How to change a set in Python?
# Sets are mutable .But since they are unordered,indexing here have no meaning.
# We cannot access or change an element of set using indexing or slicing. Set does not support it.
# We can add single element using the add() method and multiple elements using the update() method.
# The update() method can take tuples, lists, strings or other sets as its argument. In all cases, duplicates are avoided.
# initialize my_set
my_set = {1, 3}
print(my_set)
# add an element
my_set.add(2)
print(my_set)  # Output: {1, 2, 3}
# add multiple elements
my_set.update([2, 3, 4])
print(my_set)  # Output: {1, 2, 3, 4}
# add list and set
my_set.update([4, 5], {1, 6, 8})
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 8}

# +How to remove elements from a set?
# A particular item can be removed from set using methods, discard() and remove().
# The only difference between the two is that, while using discard() if the item does not exist in the set,it remains unchanged.
# But remove() will raise an error in such condition.
my_set = {1, 3, 4, 5, 6}
# discard an element
my_set.discard(4)
print(my_set)  # Output: {1, 3, 5, 6}
# remove an element
my_set.remove(6)
print(my_set)  # Output: {1, 3, 5}
# discard an element not present in my_set
my_set.discard(2)
print(my_set)  # Output: {1, 3, 5}
# remove an element not present in my_set
my_set.remove(2)  # Output: KeyError: 2
#
# Similarly, we can remove and return an item using the pop() method.
# Set being unordered, there is no way of determining which item will be popped. It is completely arbitrary.
# We can also remove all items from a set using clear().
my_set = set("HelloWorld")
print(my_set)  # Output: set of unique elements
# pop an element
print(my_set.pop())  # Output: random element
# pop another element
my_set.pop()
print(my_set)  # Output: random element
# clear my_set
my_set.clear()
print(my_set)  # Output: set()

# +Python Set Operations
# Sets can be used to carry out mathematical set operations like union, intersection,
# difference and symmetric difference. We can do this with operators or methods
#
# -Set Union
# Union is performed using | operator. Same can be accomplished using the method union().
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use | operator
print(A | B)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
#
# -Set Intersection
# Intersection of A and B is a set of elements that are common in both sets.
# Intersection is performed using & operator. Same can be accomplished using the method intersection().
print(A & B)
print(A.intersection(B))
#
# -Set Difference
# Difference of A and B (A - B) is a set of elements that are only in A but not in B.
# Similarly, B - A is a set of element in B but not in A.
# Difference is performed using - operator. Same can be accomplished using the method difference().
print(A - B)
print(A.difference(B))  # Output: {1, 2, 3}
print(B - A)
print(B.difference(A))  # Output: {6, 7, 8}
#
# -Set Symmetric Difference
# Symmetric Difference of A and B is a set of elements in both A and B except those that are common in both.
# Symmetric difference is performed using ^ operator. Same can be accomplished using the method symmetric_difference().
print(A ^ B)
print(A.symmetric_difference(B))

# +Python Set Methods
# add()	Add an element to a set
# clear()	Remove all elements form a set
# copy()	Return a shallow copy of a set
# difference()	Return the difference of two or more sets as a new set
# difference_update()	Remove all elements of another set from this set
# discard()	Remove an element from set if it is a member. (Do nothing if the element is not in set)
# intersection()	Return the intersection of two sets as a new set
# intersection_update()	Update the set with the intersection of itself and another
# isdisjoint()	Return True if two sets have a null intersection
# issubset()	Return True if another set contains this set
# issuperset()	Return True if this set contains another set
# pop()	Remove and return an arbitary set element. Raise KeyError if the set is empty
# remove()	Remove an element from a set. If the element is not a member, raise a KeyError
# symmetric_difference()	Return the symmetric difference of two sets as a new set
# symmetric_difference_update()	Update a set with the symmetric difference of itself and another
# union()	Return the union of sets in a new set
# update()	Update a set with the union of itself and others

# +Other Set Operations
#
# -Set Membership Test
# We can test if an item exists in a set or not, using the keyword in.
my_set = set("apple")
# check if 'a' is present
print('a' in my_set)  # Output: True
# check if 'p' is present
print('p' not in my_set)  # Output: False
#
# -Iterating Through a Set
for letter in set("apple"):
    print(letter)
#
# -Built-in Functions with Set
# Built-in functions like all(), any(), enumerate(), len(), max(), min(), sorted(), sum() etc.
# are commonly used with set to perform different tasks.
# all()	Return True if all elements of the set are true (or if the set is empty).
# any()	Return True if any element of the set is true. If the set is empty, return False.
# enumerate()	Return an enumerate object. It contains the index and value of all the items of set as a pair.
# len()	Return the length (the number of items) in the set.
# max()	Return the largest item in the set.
# min()	Return the smallest item in the set.
# sorted()	Return a new sorted list from elements in the set(does not sort the set itself).
# sum()	Retrun the sum of all elements in the set.

# +Python Frozenset
# Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned.
# While tuples are immutable lists, frozensets are immutable sets.
# Sets being mutable are unhashable, so they can't be used as dictionary keys.
# On the other hand, frozensets are hashable and can be used as keys to a dictionary.
#
# Frozensets can be created using the function frozenset().
#
# This datatype supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(),
# symmetric_difference() and union().
# Being immutable it does not have method that add or remove elements.
