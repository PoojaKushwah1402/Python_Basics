# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# f = open('demo.txt','a')
# f.write('now the file has more content')
# f.close()
f = open('demo.txt','w')
f.write('woops')
f.close()

x = open('demo.txt')
print(x.read())


# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

f = open('newFile.txt','x')
f.write('hello there w mode')
f.close()
f = open('newFile.txt')
print(f.read())