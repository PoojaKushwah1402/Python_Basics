x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#To create a global variable inside a function, you can use the global keyword.
#Also, use the global keyword if you want to change a global variable inside a function.


def myfunc1():
  global k
  k = "fantastic"
  global x
  x = "fantastic11"

myfunc1()
print("Python is " + k)
