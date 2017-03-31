# The zip() function take iterables (can be zero or more), 
# makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples.
#
# The syntax of zip() is: zip(*iterables)
#
# zip() Parameters
# The zip() function takes:iterables - can be built-in iterables (like: list, string, dict), or user-defined iterables (object that has __iter__ method).
# 
# Return Value from zip()
# The zip() function returns an iterator of tuples based on the iterable object.
# 1.If no parameters are passed, zip() returns an empty iterator
# 2.If a single iterable is passed, zip() returns an iterator of 1-tuples. Meaning, the number of elements in each tuple is 1.
# 3.If multiple iterables are passed, ith tuple contains ith Suppose, two iterables are passed; one iterable containing 3 and other containing 5 elements.#   Then, the returned iterator has 3 tuples. It's because iterator stops when shortest iterable is exhaused.

# Example 1: How zip() works in Python?
numberList = [1, 2, 3]
strList = ['one', 'two', 'three']
#
# No iterables are passed
result = zip()
#
# Converting itertor to list
resultList = list(result)
print(resultList) # output:[]
#
# Two iterables are passed
result = zip(numberList, strList)
#
# Converting itertor to set
resultSet = set(result)
print(resultSet) # output:{(2, 'two'), (3, 'three'), (1, 'one')}

# Example 2: Different Number of Elements in Iterables Passed to zip()
numbersList = [1, 2, 3]
strList = ['one', 'two']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')
#
result = zip(numbersList, numbersTuple)
#
# Converting to set
resultSet = set(result)
print(resultSet) # output: {(2, 'TWO'), (3, 'THREE'), (1, 'ONE')}
#
result = zip(numbersList, strList, numbersTuple)
#
# Converting to set
resultSet = set(result)
print(resultSet) # output: {(2, 'two', 'TWO'), (1, 'one', 'ONE')}

# Example 3: Unzipping the Value Using zip()
# The * operator can be used in conjuncton with zip() to unzip the list. zip(*zippedList)
#
coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]
#
result = zip(coordinate, value)
resultList = list(result)
print(resultList) # output: [('x', 3), ('y', 4), ('z', 5)]
#
c, v =  zip(*resultList)
print('c =', c) # output: c = ('x', 'y', 'z')
print('v =', v) # output: v = (3, 4, 5)
# Notice that, elements 0 and 9 in variable value is not in variable v. It's because the zipped iterables have different number of elements.
