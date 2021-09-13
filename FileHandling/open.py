# To open a file for reading it is enough to specify the name of the file:
f = open("demo.txt")
# The code above is the same as:
r = open("demo.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.
# The open() function returns a file object, which has a read() method for reading the content of the file:

#f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read(),'f')
# # By default the read() method returns the whole text, but you can also specify how many 
# #characters you want to return:
# print(r.read(7))

# You can return one line by using the readline() method:
# By calling readline() two times, you can read the two first lines:
print(f.readline())
print(f.readline())

# Close Files
# It is a good practice to always close the file when you are done with it.
f.close()
