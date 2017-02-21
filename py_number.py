# Python Variables
# We don't need to declare a variable before using it. In Python, we simply assign a value to
# a variable and it will exist. We don't even have to declare the type of the variable. This is
# handled internally according to the type of value we assign to the variable.
# Any type of value can be assigned to any valid variable.

# Multiple assignments
d, e, f = 5, 3.2, "Hello"
# If we want to assign the same value to multiple variables at once, we can do this as
x = y = z = "same"

# Data types in Python
# Every value in Python has a datatype. Since everything is an object in Python programming,
# data types are actually classes and variables are instance (object) of these classes.

# Python Numbers
# Integers, floating point numbers and complex numbers falls under Python numbers category.
# They are defined as int, float and complex class in Python.
# We can use the type() function to know which class a variable or a value belongs to and
# the isinstance() function to check if an object belongs to a particular class.
a = 5
print(a, "is of type", type(a))

b = 2.0
print(b, "is of type", type(b))

c = 1 + 2j
print(c, "is complex number?", isinstance(1 + 2j, complex))

# Integers can be of any length, it is only limited by the memory available.
# A floating point number is accurate up to 15 decimal places.
# 1 is integer, 1.0 is floating point number.
# Complex numbers are written in the form, x + yj, where x is the real part and y is the
# imaginary part. Here are some examples.
