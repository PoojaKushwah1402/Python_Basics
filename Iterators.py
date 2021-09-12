# Python Iterators
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist 
# of the methods __iter__() and __next__().

# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers 
# which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:
#Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(myit)
print(next(myit))
print(next(myit))
print(next(myit)) #string are also iterable

# Create an Iterator
# To create an object/class as an iterator you have to implement the
#  methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called 
# __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return 
# the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.

class iterNum : 
    def __iter__(self) :
        self.num = 1
        return self

    def __next__(self) :
        if self.num <= 3:
            newNum = self.num
            self.num += 1
            return newNum
        else :
            raise StopIteration
    
number = iterNum()
itr1 = iter(number)
# print(next(itr1))
# print(next(itr1))
# print(next(itr1))
# print(next(itr1))
for x in itr1:
  print(x)