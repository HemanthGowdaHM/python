# The "try" blocks lets you test a block of code for errors
# The "except" bloks lets you handle the error
# The "else" block lets you execute code when there is no error.
# The "finally" block lets you execute code, regardless of the result of the "try"  and "except " blocks.

# # Exception Handling
# try:
#     print(x)
# except:
#     print("An error is occurred")

# # Many Exceptions

# try:
#     # x = "HI"
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("something went wrong")


# # Else
# try:
#     x = "HI"

#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except SyntaxError:
#     print("The Invalid syntax in code")
# except:
#     print("something went wrong")
# else:
#     print("Nothing went wrong")


# # Finally

# try:
#     print(x)
# except:
#     print("something went worng")
# finally:
#     print("The 'try except' is finished")






# # Raise an exception : as a python developer you can choose to throw an exception if a condition occurs.
# # to throw(or raise) an exception, use the "raise" keyword.

# x = -1
# if x < 0:
#     raise Exception("sorry, no number below zero")


# x = "Hi"
# if not type(x) is int:
#     raise Exception("Only integer are allowed")