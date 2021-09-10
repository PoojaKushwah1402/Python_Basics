#Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you extract the 
#values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x,'x')
print(y,'y')
print(z,'z')

# Lists are one of 4 built-in data types in Python used to store collections of data, the other
#  3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#To determine how many items a list has, use the len() function:
#Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(len(thislist))
print(type(thislist)) #<class 'list'>
print(thislist[2:5])

#To determine if a specified item is present in a list use the in keyword:
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
print('here')
thislist[1:5] = ['hell','no']
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)#['apple', 'hell', 'watermelon', 'no', 'melon', 'mango']
#To add an item to the end of the list, use the append() method:
# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at the specified index:
#To append elements from another list to the current list, use the extend() method.
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#The remove() method removes the specified item.
thislist.remove("banana")
#The pop() method removes the specified index.
#If you do not specify the index, the pop() method removes the last item.
thislist.pop(1)
#The del keyword also removes the specified index:
del thislist[0]
#The del keyword can also delete the list completely.
del thislist
#The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

