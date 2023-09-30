print("Hello, from Python!")

# if statement
if 5 > 2:
    print("Five is greater than two!")
    print("second line")
#indentation is crucial in python. have to be at least one space under statement
"""
another type of comment
"""
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# concatenatio 
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# function
def myfunc():
  print("Python is " + x)

myfunc()

# global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# type 
x = 5
print(type(x))