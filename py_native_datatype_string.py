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
