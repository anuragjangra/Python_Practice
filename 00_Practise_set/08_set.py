"""
-File I/O in Python
-Read, Write, and Append Files
-OS and Shutil Modules in Python
-Creating Command Line Utilities
"""

# Answer to question 1 of practise set 8 (File I/O in Python)

# f = open("notes.txt", "w") # "w" is used to write in the file, if the file does not exist it will create a new file, if it already exists it will overwrite the existing file.
# f.write("This is a practise set for file handling in Python.")
# f.close()

# Answer to question 2 of practise set 8 (Read, Write, and Append Files)
# f = open("notes.txt", "r") # "r" is used to read the file, if the file does not exist it will raise an error.
# content = f.read()
# print(content)
# f.close()

# Answer to question 3 of practise set 8 (Read, Write, and Append Files)
# with open("task.txt","w") as f:
#     f.write("""This is a task file for practise set 8.It contains some tasks for you to complete.
#     Thank you for using this file.""")

# # append to the file
# with open("task.txt","a") as f:   # with statement is used to open the file and it will automatically close the file after the block of code is executed, "a" is used to append to the file, if the file does not exist it will create a new file.
#     f.write("\nTask Completed.")


# with line by line reading
# with open("task.txt","r") as f:
#     for line in f:
#         print(line)

# Answer to question 4 of practise set 8 (OS and Shutil Modules in Python)
# import os
# print(os.getcwd()) # get the current working directory
# print(os.listdir()) # list all the files and directories in the current working directory
# os.mkdir("my_folder") # create a new directory


# import shutil
# shutil.move("task.txt", "my_folder/") # move a file from one location to another
# shutil.copy("notes.txt", "my_folder/") # copy a file from one location to another
# shutil.rmtree("my_folder") # remove a directory and all its contents

# Answer to question 5 of practise set 8 (Creating Command Line Utilities) for reading a file and counting the number of lines in it.
import argparse
# parser = argparse.ArgumentParser(description="A simple command line utility to Count the number of lines in a file.")
# parser.add_argument("filename", help="The file to count lines in")
# args = parser.parse_args()

# with open(args.filename, "r") as f:
#     lines = f.readlines()
#     print(f"The number of lines in the file is: {len(lines)}")

# Answer to question 6 of practise set 8 (Creating Command Line Utilities) for reading a file and counting the number of words in it.
# parser = argparse.ArgumentParser(description="A simple command line utility to Count the number of words in a file.")
# parser.add_argument("filename", help="The file to count words in")
# parser.add_argument("word", help="The word to count")
# args = parser.parse_args()

# with open(args.filename, "r") as f:
#     content = f.read()
#     words = content.split()
#     # print(f"The number of words in the file is: {len(words)}")
#     count = words.count(args.word)
#     print(f"The number of times the word '{args.word}' appears in the file is: {count}")



# Bonus Question of practise set 8 (for reading a file and converting its content to uppercase and writing it to a new file.)
# with open("notes.txt", "r") as f:
#     content = f.read()
#     new_content = content.upper() # convert the content to uppercase
#     with open("notes_uppercase.txt","w") as f2:
#         f2.write(new_content) # write the new content to a new file