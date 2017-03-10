# Python Module
# -Modules refer to a file containing Python statements and definitions.
# A file containing Python code, for e.g.: example.py, is called a module and its module name would be example.
def add(a, b):
   """This program adds two
   numbers and return the result"""

   result = a + b
   return result
# We use modules to break down large programs into small manageable and organized files. Furthermore, modules provide reusability of code.
# We can define our most used functions in a module and import it, instead of copying their definitions into different programs.

# +How to import modules in Python?
# We can import the definitions inside a module to another module or the interactive interpreter in Python.
# We use the import keyword to do this. To import our previously defined module example we type the following in the Python prompt.
import example
# Using the module name we can access the function using dot (.) operation. For example:
example.add(1,2)
# Python has a ton of standard modules available.These files are in the Lib directory inside the location where you installed Python.
# Standard modules can be imported the same way as we import our user-defined modules.
# There are various ways to import modules
# -We can import a module using import statement and access the definitions inside it using the dot operator as described above. Here is an example.
import math
print("The value of pi is", math.pi)
#
# -Import with renaming
# We can import a module by renaming it as follows.
import math as m
print("The value of pi is", m.pi)
# We have renamed the math module as m. This can save us typing time in some cases.
# Note that the name math is not recognized in our scope. Hence, math.pi is invalid, m.pi is the correct implementation.
#
# -Python from...import statement
# We can import specific names form a module without importing the module as a whole. Here is an example.
from math import pi
print("The value of pi is", pi)
# We imported only the attribute pi form the module.
# In such case we don't use the dot operator. We could have imported multiple attributes as follows.
from math import pi, e
#
# -Import all names
# We can import all names(definitions) form a module using the following construct.
# Importing everything with the asterisk (*) symbol is not a good programming practice
from math import *
print("The value of pi is", pi)
# all the above math is invalid.

# +Reloading a module
# The Python interpreter imports a module only once during a session. This makes things more efficient. 
# eg: Suppose we have the following code in a module named my_module.
print("This code got executed")
# Now we see the effect of multiple imports.
import my_module
# print This code got executed
import my_module
import my_module
# We can see that our code got executed only once. This goes to say that our module was imported only once.
# But, Now if our module changed during the course of the program, we would have to reload it.
# One way to do this is to restart the interpreter. But this does not help much.
# Python provides a neat way of doing this. We can use the reload() function inside the imp module to reload a module.
import imp
import my_module
# print This code got executed
import my_module # noting output
imp.reload(my_module)
# print This code got executed

# +The dir() built-in function
# We can use the dir() function to find out names that are defined inside a module.
# For example, we have defined a function add() in the module example that we had in the beginning.
dir(example)
# output ['__builtins__', '__cached__', '__doc__', '__file__', '__initializing__', '__loader__', '__name__', '__package__', 'add']
# All other names that begin with an underscore are default Python attributes associated with the module
#
# All the names defined in our current namespace can be found out using the dir() function without any arguments.
dir() # like a stack
# output ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'jthan']
