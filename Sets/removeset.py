# To remove an item in a set, use the remove(), or the discard() method.
# Note: If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Remove "banana" by using the discard() method:
# Note: If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# You can also use the pop() method to remove an item, but this method will remove the last item.
#  Remember that sets are unordered, so you will not know what item that gets removed.
# The return value of the pop() method is the removed item.

x = thisset.pop()

# The clear() method empties the set:
# The del keyword will delete the set completely:


