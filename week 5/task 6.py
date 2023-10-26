# import the module
import shutil

file = input("enter file you want to backup")
# Specify the path of the file you want to copy
file_to_copy = (file)
print('./'+file_to_copy)

# Specify the path of the destination directory you want to copy to
destination_directory = 'F:\python script'

# Use the shutil.copy() method to copy the file to the destination directory
shutil.copy(file_to_copy, destination_directory)