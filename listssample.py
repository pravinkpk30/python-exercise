thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[0])
print(thislist[2])

# Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List DataTypes
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
print(type(list1))

# List constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Access Items - List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

"""
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.
Note: The search will start at index 2 (included) and end at index 5 (not included).
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

"""
Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the list:
This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

"""
Check if Item Exists
To determine if a specified item is present in a list use the in keyword:
"""
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

"""
Change Item Value
To change the value of a specific item, refer to the index number:
"""
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

"""
Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

"""
Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index:

Insert Items
To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:
"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

"""
Append Items
To add an item to the end of the list, use the append() method:
"""
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

"""
Extend List
To append elements from another list to the current list, use the extend() method.
"""
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

"""
Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
"""
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

"""
Remove Specified Item
The remove() method removes the specified item.
"""
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# If there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

"""
Remove Specified Index
The pop() method removes the specified index.
"""
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

"""
Clear the List
The clear() method empties the list.

The list still remains, but it has no content.
"""
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

"""
Loop Through a List
You can loop through the list items by using a for loop:
"""
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

"""
Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.
"""
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

"""
Customize Sort Function
You can also customize your own function by using the keyword argument key = function.
The function will return a number that will be used to sort the list (the lowest number first):
Sort the list based on how close the number is to 50:
"""
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

"""
Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# So if you want a case-insensitive sort function, use str.lower as a key function
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)