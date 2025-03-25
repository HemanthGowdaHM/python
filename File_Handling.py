# Pytohn has several functions for creating, reading, updating and deleting files.

# File Handling
''' 
    --> The key function for working with files in python is the 'open()' function.
    --> The open() function takes two parameters; filename and mode. 
    
    --> There are four different method(modes) for opening a file.
    
    --> "r" - READ - Default value. opens a file for readng, error if the file does not exist.
    
    --> "a" - Append - opens a file for appending, creates the file if it does not exist.
    
    --> "w" - Write - opens a file for writing, creates the file if ot does not exist.
    
    --> "x" - create - creates the specified file, returns an error if the file is already exists.
    
    # In addition you can specify if the file should be handled as binary or text mode. 
    --> "t" - TEXT - default value. Text mode.
    --> "b" - Binary mode(e.g. image).
    
'''

# # syntax:
# NOTE: Make sure the file exists, or else you will get an Error 
# # To open a file for reading it is enough to specify the name of the file:

# f = open("demofile.txt")

# # The code ablove is the same as:
# # "r" for read and "t" for text are the default values, you don't need to specify them

# f = open("demofile.txt","rt")


# # Open a file on the server
# # demofile.text
'''Hello.! welcome to demo file 
This file is for testing purpose
Good luck!
'''
# # The open() function returns a file object, which has a read() method for reading the content of the file.

# f = open("demofile.txt",'r')
# print(f.read())

# # If the file id located in a different locaiton, you will have to specify the file path, like this.

# # RAW STRNG (r)
# f = open(r"C:\Users\heman\OneDrive\Desktop\welcome.txt.txt",'r')
# print(f.read())

# # DOULBE BACKSLASHES(\\)
# f = open("C:\\Users\\heman\\OneDrive\\Desktop\\welcome.txt.txt",'r')
# print(f.read())

# # FORWARD SLASHES (/)
# f = open(r"C:/Users/heman/OneDrive/Desktop/welcome.txt.txt",'r')
# print(f.read())

# # NOTE : Always remember to close the file after you're done reading fron it using f.close() to free up system resources.

# f.close()

# f = open("demofile.txt",'r')

# # # return the 5 first characters of the file.
# # print(f.read(5))

# # Read Lines 
# print(f.readline())
# print(f.readlines())


# f = open("demofile.txt","r")
# for x in f:
#     print(x)
    
# f.close()


# Python file Write
# write to an existing file
# To write to an existing file, you must add a parameter to the open() function.
'''
    --> "a" -Append - will append to the end of the file.
    --> "w" -write - will overwrite any existing content.
'''
# f = open("demofile.txt","a")
# f.write("\nNow the file has more content")
# f.close()

# f = open("demofile.txt","r")
# print(f.read())

# f = open(r"C:\Users\heman\OneDrive\Desktop\welcome.txt.txt","w")
# f.write("woops.!I have deleted the content! and rewrite the file content ")
# f.close()

# f = open(r"C:\Users\heman\OneDrive\Desktop\welcome.txt.txt","r")
# print(f.read())
# f.close()

# # create a new file
# f = open("demo.txt","x")
# f.close()


# # write the file if the file exist it will overwrite file ....if file does not exist it will create file 
# f = open("demo2.txt","w")
# f.write("This is new file created using function and write the file")
# f = open("demo2.txt","r")
# print(f.read())
# f.close()

# f = open("demo2.txt","a")
# f.write("\tadding the new lines  to file ")
# f = open("demo2.txt","r")
# print(f.read())
# f.close()


# # python Delete file 
# # To delete a file,you must import the OS module, and run it's  os.remove()  function.
# import os 
# os.remove("demo.txt")

# # check if File exist:
# import os 
# if os.path.exists(r"C:\Users\heman\OneDrive\Desktop\welcome.txt.txt"):
#     os.remove(r"C:\Users\heman\OneDrive\Desktop\welcome.txt.txt")
# else:
#     print("The file does not exist")



# import os 
# os.rmdir("mytextfile")