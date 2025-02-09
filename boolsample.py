"""
Evaluate Values and Variables
The bool() function allows you to evaluate any value, and give you True or False in return,
"""
print(bool("Hello"))
print(bool(15))

"""
Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", 
the number 0, and the value None. And of course the value False evaluates to False.
"""
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))