# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
a = "Hello, World!"
print(a[1])

# Looping through String
for x in "Praveen Kumar":
  print(x)

# Length
a = "Hello, World!"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print("Slicing Sample output")
print(b[2:5])

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
b = "Hello, World!"
print(b[:5])

# Slice To the End
# By leaving out the end index, the range will go to the end:
b = "Hello, World!"
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:

"""
Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
"""

b = "Hello, World!"
print(b[-5:-2])

"""
Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
The strip() method removes any whitespace from the beginning or the end:
"""

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# But we can combine strings and numbers by using f-strings or the format() method!
age = 36
txt = f"My name is John, I am {age}"
print(txt)

"""
Placeholders and Modifiers
A placeholder can contain variables, operations, functions, and modifiers to format the value.
"""
price = 59
txt = f"The price is {price} dollars"
print(txt)

"""
A placeholder can include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
"""
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)