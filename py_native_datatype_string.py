# +A string is a sequence of characters.
# A character is simply a symbol. For example, the English language has 26 characters.
# Computers do not deal with characters, they deal with numbers (binary). Even though you
# may see characters on your screen, internally it is stored and manipulated as a combination of 0's and 1's.
# This conversion of character to a number is called encoding, and the reverse process is
# decoding. ASCII and Unicode are some of the popular encoding used.
# In Python, string is a sequence of Unicode character. Unicode was introduced to include
# every character in all languages and bring uniformity in encoding. You can learn more about Unicode from here.

# +How to create a string?
my_string = 'Hello'
my_string1 = "Hello"
my_string2 = '''Hello'''
# triple quotes string can extend multiple lines
my_string3 = """Hello, welcome to
           the world of Python"""

# +How to access characters in a string?
# We can access individual characters using indexing and a range of characters using slicing.
str = 'programiz'
print('str = ', str)
print('str[0] = ', str[0])  # first character
print('str[-1] = ', str[-1])  # last character
print('str[1:5] = ', str[1:5])  # slicing 2nd to 5th character
print('str[5:-2] = ', str[5:-2])  # slicing 6th to 2nd last character

# +How to change or delete a string?
# Strings are immutable. This means that elements of a string cannot be changed once it has been assigned.
# But we can simply reassign different strings to the same name.
my_string4 = 'programiz'
my_string4[5] = 'b'  # TypeError: 'str' object does not support item assignment
# We also can't delete or remove characters from a string.
# But deleting the string entirely is possible using the keyword del.
del my_string[1]  # TypeError: 'str' object doesn't support item deletion

# +Python String Operations
# -Concatenation of Two or More Strings
str1 = 'Hello'
str2 = 'World!'
print('str1 + str2 = ', str1 + str2)  # using +
print('str1 * 3 =', str1 * 3)  # using *

# Iterating Through String
count = 0
for letter in 'Hello World':
    if (letter == 'l'):
        count += 1
print(count, 'letters found')

# String Membership Test
is_in = 'a' in 'program'
is_not_in = 'at' not in 'program'

# Built-in functions to Work with Python
# Various built-in functions that work with sequence, works with string as well.
# Some of the commonly used ones are enumerate() and len(). The enumerate() function returns an enumerate object.
# It contains the index and value of all the items in the string as pairs. This can be useful for iteration.
# Similarly, len() returns the length (number of characters) of the string.
str = 'cold'
str_enum = enumerate(str)  # enumerate()
print('list(enumerate(str) = ', list(str_enum))
print('len(str) = ', len(str))  # character count

# +Python String Formatting
# -Escape Sequence(转义序列)
print('He said, "What\'s there?"')
print("He said, \"What's there?\"")
print('''He said, "What's there?"''')
print("This is printed\nin two lines")

# +Raw String to ignore escape sequence(原始字符串)
print("This is \x61 \ngood example")
print(r"This is \x61 \ngood example")

# +The format() Method for Formatting Strings
# default(implicit) order
default_order = "{}, {} and {}".format('John', 'Bill', 'Sean')
print(default_order)  # --- Default Order ---
# order using positional argument
positional_order = "{1}, {0} and {2}".format('John', 'Bill', 'Sean')
print(positional_order)  # --- Positional Order ---
# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John', b='Bill', s='Sean')
print(keyword_order)  # --- Keyword Order ---

# +Specifications format
"Binary representation of {0} is {0:b}".format(12)
'Binary representation of 12 is 1100'
"Exponent representation: {0:e}".format(1566.345)
'Exponent representation: 1.566345e+03'

# +Old format
x = 12.3456789
print('The value of x is %3.2f' % x)  # The value of x is 12.35
print('The value of x is %3.4f' % x)  # The value of x is 12.3457

# +String Method
#
'python'.capitalize() # output: Python
# Return a copy of the string with its first character capitalized and the rest lowercased.
#
# str.center(width[, fillchar])
'python'.center(10,'*') # output: '**python**'
# Return centered in a string of length width. Padding is done using the specified fillchar (default is an ASCII space).
# The original string is returned if width is less than or equal to len(s).
#
# str.count(sub[, start[, end]])
'python3.6'.count('3') # output: 1
# Return the number of non-overlapping occurrences of substring sub in the range [start, end].
# Optional arguments start and end are interpreted as in slice notation.
#
#str.startswith(prefix[, start[, end]])
'python3.6'.startswith('t',2)
# Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. 
# With optional start, test string beginning at that position. With optional end, stop comparing string at that position.
#
# str.endswith(suffix[, start[, end]])
'python3.6'.endswith('3',0,-2)
# Return True if the string ends with the specified suffix, otherwise return False. 
# suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position.
# With optional end, stop comparing at that position.
#
# str.find(sub[, start[, end]])
'python3.6'.find('3') # output 6
# Return the lowest index in the string where substring sub is found within the slice s[start:end].
# Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
#
# str.rfind(sub[, start[, end]])
'abacadef'.rfind('a') # output: 4
# Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. 
# Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
#
# str.index(sub[, start[, end]])
'python3.6'.index('3') # output 6 
# Like find(), but raise ValueError when the substring is not found. ValueError: substring not found
#
# str.rindex(sub[, start[, end]])
'abacadef'.rindex('a') # output: 4
# Like rfind() but raises ValueError when the substring sub is not found.
#
# str.isalnum()
'python3.6'.isalnum() # True
# Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.
# A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().
#
# str.isalpha()
'python3.6'.isalpha() # False
# Return true if all characters in the string are alphabetic and there is at least one character, false otherwise. 
#
# str.isdecimal()
'python3.6'.isdecimal() # False
# Return true if all characters in the string are decimal characters and there is at least one character, false otherwise. 10!!
#
# str.isdigit()
'python3.6'.isdigit() # False
# Return true if all characters in the string are digits and there is at least one character, false otherwise. 
# Digits include decimal characters and digits that need special handling, such as the compatibility superscript digits.
#
# str.isidentifier()
# Return true if the string is a valid identifier according to the language definition.
#
# str.islower()
'python3.6'.islower()
# Return true if all cased characters in the string are lowercase and there is at least one cased character, false otherwise.
#
# str.lower()
'PYTHON3.6'.lower() # 'python3.6'
# Return a copy of the string with all the cased characters [4] converted to lowercase.
#
# str.isupper()
'python3.6'.isupper()
# Return true if all cased characters [4] in the string are uppercase and there is at least one cased character, false otherwise.
#
# str.upper()
'python3.6'.isupper()
# Return a copy of the string with all the cased characters [4] converted to uppercase.
# Note that str.upper().isupper() might be False
#
# str.isnumeric()
# Return true if all characters in the string are numeric characters, and there is at least one character, false otherwise.
#
# str.isspace()
'         '.isspace() # True
#
#
# str.istitle()
'I Am A Title'.istitle()
# Return true if the string is a titlecased string and there is at least one character,
# for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return false otherwise.
#
# str.join(iterable)
','.join(['1', '2', '3', '4', '5'])
# Return a string which is the concatenation of the strings in the iterable iterable. A TypeError will be raised if there are any non-string values 
# in iterable, including bytes objects. The separator between elements is the string providing this method.
#
# str.ljust(width[, fillchar])
'python3.6'.ljust(15,'*') # output: 'python3.6******'
# Return the string left justified in a string of length width. Padding is done using the specified
# fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
#
# str.rjust(width[, fillchar])
'python3.6'.rjust(15,'*') # output: '******python3.6'
# Return the string right justified in a string of length width. Padding is done using the specified
# fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
#
# str.partition(sep)
# str.rpartition(sep)
'abcdef'.partition('abc') # output :('', 'abc', 'def')
# Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator,the separator itself,
# and the part after the separator.If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.
#
# str.replace(old, new[, count])
'abacadef'.replace('a','A', 2) # output: 'AbAcadef'
# Return a copy of the string with all occurrences of substring old replaced by new.
# If the optional argument count is given, only the first count occurrences are replaced.
#
# str.split(sep=None, maxsplit=-1)
# str.rsplit(sep=None, maxsplit=-1)
'1,1,1,1,1'.split(',',1) # ['1', '1,1,1,1']
'1,1,1,1,1'.rsplit(',',1) # ['1,1,1,1', '1']
# Return a list of the words in the string, using sep as the delimiter string. 
# If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). 
# If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
#
# str.swapcase()
'Python3.6'.swapcase() # output: 'pYTHON3.6'
# Return a copy of the string with uppercase characters converted to lowercase and vice versa.
# Note that it is not necessarily true that s.swapcase().swapcase() == s.

# Truth Value Testing
# Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below.
# The following values are considered false:
# None
# False
# zero of any numeric type, for example, 0, 0.0, 0j.
# any empty sequence, for example, '', (), [].
# any empty mapping, for example, {}.
# instances of user-defined classes, if the class defines a __bool__() or __len__() method, when that method returns the integer zero or bool value False.

# check string is empty or all whitespace or None
s = 'str'
if not isinstance(s,str) or not s or s.isspace(): print(s + ' is empty or None or all whitespace')
