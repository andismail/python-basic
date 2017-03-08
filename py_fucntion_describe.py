# +Build-in functions & User-defined functions
# There are 68 built-in functions defined in Python 3.5.2.
#
# abs()	Return the absolute value of a number.
# all()	Return True if all elements of the iterable are true (or if the iterable is empty).
# any()	Return True if any element of the iterable is true. If the iterable is empty, return False.
# ascii()	Return a string containing a printable representation of an object, but escape the non-ASCII characters.
# bin()	Convert an integer number to a binary string.
# bool()	Convert a value to a Boolean.
# bytearray()	Return a new array of bytes.
# bytes()	Return a new "bytes" object.
# callable()	Return True if the object argument appears callable, False if not.
# chr()	Return the string representing a character.
# classmethod()	Return a class method for the function.
# compile()	Compile the source into a code or AST object.
# complex()	Create a complex number or convert a string or number to a complex number.
# delattr()	Deletes the named attribute of an object.
# dict()	Create a new dictionary.
# dir()	Return the list of names in the current local scope.
# divmod()	Return a pair of numbers consisting of quotient and remainder when using integer division.
# enumerate()	Return an enumerate object.
# eval()	The argument is parsed and evaluated as a Python expression.
# exec()	Dynamic execution of Python code.
# filter()	Construct an iterator from elements of iterable for which function returns true.
# float()	Convert a string or a number to floating point.
# format()	Convert a value to a "formatted" representation.
# frozenset()	Return a new frozenset object.
# getattr()	Return the value of the named attribute of an object.
# globals()	Return a dictionary representing the current global symbol table.
# hasattr()	Return True if the name is one of the object's attributes.
# hash()	Return the hash value of the object.
# help()	Invoke the built-in help system.
# hex()	Convert an integer number to a hexadecimal string.
# id()	Return the "identity" of an object.
# input()	Reads a line from input, converts it to a string (stripping a trailing newline), and returns that.
# int()	Convert a number or string to an integer.
# isinstance()	Return True if the object argument is an instance.
# issubclass()	Return True if class is a subclass.
# iter()	Return an iterator object.
# len()	Return the length (the number of items) of an object.
# list()	Return a list.
# locals()	Update and return a dictionary representing the current local symbol table.
# map()	Return an iterator that applies function to every item of iterable, yielding the results.
# max()	Return the largest item in an iterable.
# memoryview()	Return a "memory view" object created from the given argument.
# min()	Return the smallest item in an iterable.
# next()	Retrieve the next item from the iterator.
# object()	Return a new featureless object.
# oct()	Convert an integer number to an octal string.
# open()	Open file and return a corresponding file object.
# ord()	Return an integer representing the Unicode.
# pow()	Return power raised to a number.
# print()	Print objects to the stream.
# property()	Return a property attribute.
# range()	Return an iterable sequence.
# repr()	Return a string containing a printable representation of an object.
# reversed()	Return a reverse iterator.
# round()	Return the rounded floating point value.
# set()	Return a new set object.
# setattr()	Assigns the value to the attribute.
# slice()	Return a slice object.
# sorted()	Return a new sorted list.
# staticmethod()	Return a static method for function.
# str()	Return a str version of object.
# sum()	Sums the items of an iterable from left to right and returns the total.
# super()	Return a proxy object that delegates method calls to a parent or sibling class.
# tuple()	Return a tuple
# type()	Return the type of an object.
# vars()	Return the __dict__ attribute for a module, class, instance, or any other object.
# zip()	Make an iterator that aggregates elements from each of the iterables.
# __import__()	This function is invoked by the import statement.

# +Function Arguments
# -default arguments
def greet(name, msg = "Good morning!"):
   """
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   """

   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")
# In this function, the parameter name does not have a default value and is required (mandatory) during a call.
# On the other hand, the parameter msg has a default value of "Good morning!". So, it is optional during a call. If a value is provided, it will overwrite the default value.
# Any number of arguments in a function can have a default value. But once we have a default argument, all the arguments to its right must also have default values.
# This means to say, non-default arguments cannot follow default arguments. For example, if we had defined the function header above as:
def greet(msg = "Good morning!", name):
	pass
# SyntaxError: non-default argument follows default argument
#
# -Python Keyword Arguments
# Python allows functions to be called using keyword arguments. When we call functions in this way, the order (position) of the arguments can be changed
greet(name = "Bruce",msg = "How do you do?")
greet(msg = "How do you do?",name = "Bruce") 
greet("Bruce",msg = "How do you do?") 
#
# But we must keep in mind that keyword arguments must follow positional arguments.
# Having a positional argument after keyword arguments will result into errors. 
greet(name="Bruce","How do you do?")
# SyntaxError: non-keyword arg after keyword arg
#
# -Python Arbitrary Arguments
# Sometimes, we do not know in advance the number of arguments that will be passed into 
# a function.Python allows us to handle this kind of situation through function calls with arbitrary number of arguments.
# In the function definition we use an asterisk (*) before the parameter name to denote this kind of argument. Here is an example.
def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")
# Here, we have called the function with multiple arguments. These arguments get wrapped up into a tuple before being passed into the function.
# Inside the function, we use a for loop to retrieve all the arguments back.
