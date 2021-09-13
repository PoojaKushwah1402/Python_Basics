# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
import os

os.remove('demo.txt')

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

if os.path.exists('demo.txt') :
    os.remove('demo.txt')
else :
    print('file not exist')


# To delete an entire folder, use the os.rmdir() method:
# Example
# Remove the folder "myfolder":

# import os
# os.rmdir("myfolder")