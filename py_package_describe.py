# Python Packages
# A directory must contain a file named __init__.py in order for Python to consider it as a package. 
# This file can be left empty but we generally place the initialization code for that package in this file.

# Importing module from a package
# We can import modules from packages using the dot (.) operator.
# import a modules , like import a file just.
import Game.Level.start
# Now if this module contains a function named select_difficulty(), we must use the full name to reference it.
Game.Level.start.select_difficulty(2)
# If this construct seems lengthy, we can import the module without the package prefix as follows.
from Game.Level import start
# We can now call the function simply as follows.
start.select_difficulty(2)
# Yet another way of importing just the required function (or class or variable) form a module within a package would be as follows.
from Game.Level.start import select_difficulty
# Now we can directly call this function.
select_difficulty(2)
# While, Although it seems easier, but this is not recommended. 
# Using the full namespace avoids confusion and prevents two same identifier names from colliding.
#
# While importing packages, Python looks in the list of directories defined in sys.path, similar as for module search path.
