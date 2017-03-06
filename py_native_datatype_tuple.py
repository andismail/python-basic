# In Python programming, a tuple is similar to a list.
# The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas in a list,
# elements can be changed.

# +Advantages of Tuple over List
# Since, tuples are quite similar to lists, both of them are used in similar situations as well.
# 1.We generally use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.
# 2.Since tuple are immutable, iterating through tuple is faster than with list. So there is a slight performance boost.
# 3.Tuples that contain immutable elements can be used as key for a dictionary. With list, this is not possible.
# 4.If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

# +Creating a Tuple
# A tuple can have any number of items and they may be of different types (integer, float, list, string etc.).
# empty tuple
my_tuple = ()
print(my_tuple)  # Output: ()
#
# tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)
#
# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)  # Output: (1, "Hello", 3.4)
#
# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)  # Output: ("mouse", [8, 4, 6], (1, 2, 3))
#
# tuple can be created without parentheses
# also called tuple packing
my_tuple = 3, 4.6, "dog"
print(my_tuple)  # Output: 3, 4.6, "dog"
#
# tuple unpacking is also possible
a, b, c = my_tuple
print(a)  # 3
print(b)  # 4.6
print(c)  # dog
#
# Creating a tuple with one element
# only parentheses is not enough
my_tuple = ("hello")
print(type(my_tuple))  # Output: <class 'str'>
#
# need a comma at the end
my_tuple = ("hello",)
print(type(my_tuple))  # Output: <class 'tuple'>
#
# parentheses is optional
my_tuple = "hello",
print(type(my_tuple))  # Output: <class 'tuple'>

# +Accessing Elements in a Tuple
# 1. Indexing
# We can use the index operator [] to access an item in a tuple where the index starts from 0.
# So, a tuple having 6 elements will have index from 0 to 5. Trying to access an element other that (6, 7,...) will raise an IndexError.
# The index must be an integer, so we cannot use float or other types. This will result into TypeError.
# Likewise, nested tuple are accessed using nested indexing, as shown in the example below.
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])  # Output: 'p'
print(my_tuple[5])  # Output: 't'
# index must be in range
# index must be an integer
#
# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(n_tuple[0][3])  # Output: 's'
print(n_tuple[1][1])  # Output: 4
#
# 2. Negative Indexing
# Python allows negative indexing for its sequences.
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[-1])  # Output: 't'
print(my_tuple[-6])  # Output: 'p'
#
# 3. Slicing
# We can access a range of items in a tuple by using the slicing operator - colon ":".
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# elements 2nd to 4th
print(my_tuple[1:4])  # Output: ('r', 'o', 'g')
# elements beginning to 2nd
print(my_tuple[:-7])  # Output: ('p', 'r')
# elements 8th to end
print(my_tuple[7:])  # Output: ('i', 'z')
# elements beginning to end
print(my_tuple[:])  # Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# +Changing a Tuple
# Unlike lists, tuples are immutable.
# This means that elements of a tuple cannot be changed once it has been assigned. But,
# if the element is itself a mutable datatype like list, its nested items can be changed.
# We can also assign a tuple to different values (reassignment).
my_tuple = (4, 2, 3, [6, 5])
# we cannot change an element
my_tuple[1] = 9  # TypeError: 'tuple' object does not support item assignment
# but item of mutable element can be changed
my_tuple[3][0] = 9
print(my_tuple)  # Output: (4, 2, 3, [9, 5])
# tuples can be reassigned
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)  # Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
#
# We can use + operator to combine two tuples. This is also called concatenation.
# We can also repeat the elements in a tuple for a given number of times using the * operator.
# Both + and * operations result into a new tuple.
# Concatenation
print((1, 2, 3) + (4, 5, 6))  # Output: (1, 2, 3, 4, 5, 6)
# Repeat
print(("Repeat",) * 3)  # Output: ('Repeat', 'Repeat', 'Repeat')

# +Deleting a Tuple
# As discussed above, we cannot change the elements in a tuple.
# That also means we cannot delete or remove items from a tuple.
# But deleting a tuple entirely is possible using the keyword del.
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# can delete entire tuple
del my_tuple
my_tuple  # NameError: name 'my_tuple' is not defined

# +Python Tuple Methods
# Methods that add items or remove items are not available with tuple. Only the following two methods are available.
# count(x)	Return the number of items that is equal to x
# index(x)	Return index of first item that is equal to x
my_tuple = ('a', 'p', 'p', 'l', 'e',)
# Count
print(my_tuple.count('p'))  # Output: 2
# Index
print(my_tuple.index('l'))  # Output: 3

# +Other Tuple Operations
# 1. Tuple Membership Test
# We can test if an item exists in a tuple or not, using the keyword in.
my_tuple = ('a', 'p', 'p', 'l', 'e',)
# In operation
print('a' in my_tuple)  # Output: True
print('b' in my_tuple)  # Output: False
# Not in operation
print('g' not in my_tuple)  # Output: True
# 2. Iterating Through a Tuple
# Using a for loop we can iterate though each item in a tuple.
for name in ('John', 'Kate'):
    print("Hello", name)

# +Built-in Functions with Tuple
# Built-in functions like all(), any(), enumerate(), len(), max(), min(), sorted(),
# tuple() etc. are commonly used with tuple to perform different tasks.
#
# all()	Return True if all elements of the tuple are true (or if the tuple is empty).
# any()	Return True if any element of the tuple is true. If the tuple is empty, return False.
# enumerate()	Return an enumerate object. It contains the index and value of all the items of tuple as pairs.
# len()	Return the length (the number of items) in the tuple.
# max()	Return the largest item in the tuple.
# min()	Return the smallest item in the tuple
# sorted()	Take elements in the tuple and return a new sorted list (does not sort the tuple itself).
# sum()	Return the sum of all elements in the tuple.
# tuple()	Convert an iterable (list, string, set, dictionary) to a tuple.

# +About tuple
# tuple more like a entity model not only the data struts
# 1.Tuples are used for grouping data
year_born = ("Paris Hilton", 1981)
# This is an example of a data structure — a mechanism for grouping and organizing data to make it easier to use.
# a tuple can be used to group any number of items into a single compound value
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# Tuples are useful for representing what other languages often call records — some related information that belongs together, like your student record.
# There is no description of what each of these fields means, but we can guess.
# A tuple lets us “chunk” together related information and use it as a single thing.
#
# To construct the new tuple, it is convenient that we can slice parts of the old tuple and join up the bits to make the new tuple.
# So if julia has a new recent film, we could change her variable to reference a new tuple that used some information from the old one:
julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
#
# 2.Tuple assignment
# Python has a very powerful tuple assignment feature that allows a tuple of variables on the left of an assignment to be assigned values from a tuple on the right of the assignment.
(name, surname, b_year, movie, m_year, profession, b_place) = julia
# This does the equivalent of seven assignment statements, all on one easy line.
# One requirement is that the number of variables on the left must match the number of elements in the tuple.
#
# Once in a while, it is useful to swap the values of two variables.
(a, b) = (b, a)
#
# 3.Tuples as return values
# we could write a function that returns both the area and the circumference of a circle of radius r:
def f(r):
    '''Return (circumference, area) of a circle of radius r '''
    c = 3.14 * r * 2
    a = 3.14 * r ** 2
    return (c, a)
#
# 4.Composability of Data Structures(数据结构的可组合性)
julia_more_info = (("Julia", "Roberts"), (8, "October", 1967), "Actress", ("Atlanta", "Georgia"),
                   [("Duplicity", 2009),
                    ("Notting Hill", 1999),
                    ("Pretty Woman", 1990),
                    ("Erin Brockovich", 2000),
                    ("Eat Pray Love", 2010),
                    ("Mona Lisa Smile", 2003),
                    ("Oceans Twelve", 2004)])
