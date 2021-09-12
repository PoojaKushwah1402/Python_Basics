# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Person : 
    def __init__ (self, fname, lname) :
        self.name = fname + ' ' + lname
        print('parent')
    
    def printName(self) : 
        print(self.name,' name')
    
# p1 = Person('pooja', 'kushwah')
# p1.printName()

class Bechular(Person) :

    def __init__(self, fname, lname, year) :
        super().__init__(fname, lname)
        self.year = year
        print('here')

    def printEverything(self) :
        super().printName()
        print(self.year,'yaer')

BS1 = Bechular('pooja', 'kushwah', '2019')
BS1.printEverything()

class Student(Person):
  pass

s1 = Student('kush','bub')
s1.printName()

