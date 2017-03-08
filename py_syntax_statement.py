# Multi-line statement
# In Python, end of a statement is marked by a newline character. But we can make
# a statement extend over multiple lines with the line continuation character (\).
# For example:
a = 1 + 1 + 1 + \
    2 + 2 + 2 + 2 + \
    3 + 3 + 3 + 3 + 3

# Here, the surrounding parentheses ( ) do the line continuation implicitly.
b = (1 + 2 + 3 +
     4 + 5 + 6 +
     7 + 8 + 9)

# Same is the case with [ ] and { }. For example:
c = ['red',
     'blue',
     'green']

# We could also put multiple statements in a single line using semicolons, as follows
d = 1; e = 2; f = 3

# Python Indentation
# Most of the programming languages like C, C++, Java use braces { } to define a block of code.
# Python uses indentation.
if True:
    print('Hello')
    a = 1
# or
if True: print('Hello'); a = 1
# Incorrect indentation will result into IndentationError.

# Multi-line comments
# Another way of doing this is to use triple quotes, either ''' or """.
# These triple quotes are generally used for multi-line strings.
# But they can be used as multi-line comment as well.
# Unless they are not docstrings, they do not generate any extra code.

# Docstring in Python ,Docstring is short for documentation string.
'''docstring in python, docstring is short for documentation string'''
if True:
    '''comment'''
    print('Hello world')

# It is a string that occurs as the first statement in a module, function, class, or method
# definition. We must write what a function/class does in the docstring.
# Triple quotes are used while writing docstrings. For example:
def double(num):
    """Function to double the value"""
    return 2*num
# Docstring is available to us as the attribute __doc__ of the function. Issue the following
# code in shell once you run the above program.
print(double.__doc__)

# +Syntax of pass
# We generally use it as a placeholder.
# Suppose we have a loop or a function that is not implemented yet, but we want to 
# implement it in the future. They cannot have an empty body. The interpreter would 
# complain. So, we use the pass statement to construct a body that does nothing.
def func01(args):
    pass

class example:
    pass
