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
# While a floating point number is accurate up to 15 decimal places.
# 1 is integer, 1.0 is floating point number.
# Complex numbers are written in the form, x + yj, where x is the real part and y is the
# imaginary part. Here are some examples.

# +Number prefix
# Number System	    Prefix
# Binary	        '0b' or '0B'
# Octal	        '0o' or '0O'
# Hexadecimal	'0x' or '0X'
print(0b1101011)  # Output: 107
print(0xFB + 0b10)  # Output: 253 (251 + 2)
print(0o15)  # Output: 13

# +Type Conversion
# We can convert one type of number into another. This is also known as coercion.
# Operations like addition, subtraction coerce integer to float implicitly (automatically), if one of the operand is float.
print(1 + 2.0)  # 3.0
# We can also use built-in functions like int(), float() and complex() to convert between types explicitly.
# These function can even convert from strings.
int(2.3)  # 2
int(-2.3)  # -2
float(2)  # 2

# +Python Decimal
print((1.1 + 2.2) == 3.3)  # False
# It turns out that floating-point numbers are implemented in computer hardware as binary
# fractions, as computer only understands binary (0 and 1). Due to this reason, most of the
# decimal fractions we know, cannot be accurately stored in our computer
# For example:
# We cannot represent the fraction 1/3 as a decimal number. This will give 0.33333333... which is infinitely long,
# and we can only approximate it.
# Turns out decimal fraction 0.1 will result into an infinitely long binary fraction of
# 0.000110011001100110011... and our computer only stores a finite number of it.
# This will only approximate 0.1 but never be equal.
# Hence, it is the limitation of our computer hardware and not an error in Python.
import decimal

print(0.1)  # Output: 0.1
print(decimal.Decimal(0.1))  # AS INT Output: Decimal('0.1000000000000000055511151231257827021181583404541015625')
print(decimal.Decimal('0.1'))  # AS STRING Output: 0.1
from decimal import Decimal as D

print(D('1.1') + D('2.2'))  # Output: Decimal('3.3')
print(D('1.2') * D('2.50'))  # Output: Decimal('3.000')

# +Python Fractions
# Python provides operations involving fractional numbers through its fractions module.
# A fraction has a numerator and a denominator, both of which are integers. This module has
# support for rational number arithmetic.
# We can create Fraction objects in various ways.
import fractions

print(fractions.Fraction(1.5))  # Output: 3/2
print(fractions.Fraction(5))  # Output: 5
print(fractions.Fraction(1, 3))  # Output: 1/3
print(fractions.Fraction(1.1))  # AS FLOAT Output: 2476979795053773/2251799813685248
print(fractions.Fraction('1.1'))  # AS STRING Output: 11/10

# +Python Mathematics
# Python offers modules like math and random to carry out different mathematics like
# trigonometry, logarithms, probability and statistics, etc.
import math

print(math.pi)  # Output: 3.141592653589793
print(math.cos(math.pi))  # Output: -1.0
print(math.exp(10))  # Output: 22026.465794806718
print(math.log10(1000))  # Output: 3.0   对数
print(math.sinh(1))  # Output: 1.1752011936438014
print(math.factorial(6))  # Output: 720  阶乘
#### TO BE CONTINUE ...

# +Python Random
import random

print(random.randrange(10, 20))  # 10 <= x < 20

xx = ['a', 'b', 'c', 'd', 'e']
# Get random choice
print(random.choice(xx))
# Shuffle x
random.shuffle(xx)
print(xx)  # Print the shuffled x

# Print random element
print(random.random())
random.seed(2)

print(random.random())
print(random.random())
print(random.random())
#### TO BE CONTINUE ...
