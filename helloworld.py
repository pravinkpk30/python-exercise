import sys

print("Hello, World!")

# To identify the python version
print(sys.version)

# Indentation sample
if 5 > 2:
    print("Five is greater than two!!")

# Variables and types determined at runtime
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

"""
Casting
If you want to specify the data type of a variable, this can be done with casting.
"""
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

"""
Get the Type
You can get the data type of a variable with the type() function.
"""
x = 5
y = "John"
print(type(x))
print(type(y))

# String : String variables can be declared either by using single or double quotes
x = "John"
# is the same as
x = 'John'

"""
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking

fruits = ["praveen", "kumar", "k"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Sample
x = 5
y = "John"
# print(x + y) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Function declare and Global Variables
x = "Welcome!!!!"

def test(): # declare and define function
    print("Hello Praveen " + x)

test() # Invoke function

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# global keyword

"""
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""

def myfunc():
  global x
  x = "fantastic"
  print(x)

myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "Praveen"

def myfunc():
  global x
  x = "Kumar"

myfunc()

print("Welcome " + x)

# Complex numbers
x = 3+5j
y = 5j
z = -5j

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

# Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
