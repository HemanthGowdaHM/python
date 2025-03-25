# # Function in python
'''--> Function in python provide organized, reusable and modular code to perform a set of specific actions.
   --> Functions simplify the coding process, prevent redundant logic, and make the code easer to follow.
   
# Syntax ( function is block of code which only runs when it is called )
   def function_name(parameter):
        statement(s)
        
'''

'''--> Using the " def " statementis the most common way to define a functon in python.
        This statements is a so called single clause compound statement with the syntax.
   --> " function_name " is know aas the identifier of the function.
        Since a function defination is an executable statement its execution binds the function name to the function object which can be called later on using the identifier.
   --> " parameter " is an optional list of identifier that get bound to the values suppplied as arguments when the function is called.
       A function may have an arbitary number of arguments which are separated by commas.
   --> " statement(s) " also know as the function body - are a nonempty sequenceas of statements executed each time the function is called.
       This means a function body cannot be empty, just like any indented block. 
'''
# # creating a function
# def my_function():
#      print("Hello from a function")
# my_function()                           # calling function      
# # output: Hello from a function


# # Arguments
'''--> Infromation can be passed into functions as arguments.
   --> Arguments are specified after the function name, inside the parentheses.you can add as many argument as you want, just separate them witha comma.
'''
# def my_function(fname):
#      print("Hello"+" "+fname)
# my_function("hemi")              # Hello hemi
# my_function("Ram")               # Hello Ram
# my_function("KOHLI")             # Hello KOHLI

# def greet_two(greeting):
#      print(greeting)
# greet_two("Hello my dear friends...!")  # output: Hello my dear friends...!

# def greet(greet="Hiii"):
#      print(greet)
# greet()                       # output: Hiii

# def my_fun(x):
#      if x>0:
#           return "Hello"
#      else:
#           return 0
# print(my_fun(1))
# print(my_fun(-1))
# # output: Hello 
# # output: 0


# def hello():
#      return " Hello world"
# print(hello())

# def do_nothing():
#      pass
# print(do_nothing())  
# # output : None


# # Number of Arguments
'''--> By default, a function must be called with the correct number if arguments.
   --> meaning that if your function expects 2 arguments you have to call the function with 2 arguments not more and not less.
'''
# def my_fun(fname,lname):
#      print(fname+" "+lname)
# my_fun("Virat","Kohli")
# my_fun("Abraham Benjamin","De villiers")
# # output: Virate Kohli , Abraham Benjamin De villiers


# # Arbitrary Arguments, *args
'''--> If you do not know how many arguments that will be passed into your function.
       Add a "*"  before the parameter name in the function definition.
   --> This way the function will receive a tuple of arguments, and can access the items accordingly.
'''

# def my_function(*kids):
#      print("The youngest child is "+kids[2])
# my_function("Ram","Hanuman","shiva")


# # Keyword Arguments
# # you can also send agruments with the key=value syntax
# def my_fun(child1,child2,child3):
#      print("the youngest child is "+ child3)
# my_fun(child1="Ram",child2="Hanuman",child3="shiva")


# # Arbitrary Keyword Arguments. **kwargs
# '''--> if you do not know how many keywords arguments that will be passed into your function, 
#           add two asterisk: ** before the parameter name in the function definition.
#    --> This way the function wil receive a dictionart of arguments , and can access the item accordingly.
# '''
# def my_function(**kid):
#      print("His last name is "+ kid["lname"])
# my_function(fname="raju",lname="Raju")


# # Default Parameter value
# '''--> If we call the function without argument, it uses the default value.'''
# def my_default(country="Inida"):
#      print("I am from "+country)
# my_default()
# my_default("south africa")
# my_default("usa")


# # Passing a List as an Argument
# '''--> you can send any data types if arguments to a function(string, number,list,dictionary etc..),
#           and it will be treated as the same data type inside the function.
# '''
# def food_list(Food):
#      for x in Food:
#           print(x)
# fruits = ["apple","banana","cherry"]
# food_list(fruits)

# # Retrun Values ( To let a function return a value, use the return statement.)
# def function(x):
#      return 5*x
# print(function(3))
# print(function(10))


# # The Pass Statement
# '''--> function definitions cannot be empty, but if you for some reason have a funcution definition with on content,
#           put in the " pass " statemnt to avoid getting an error.
# '''
# def my_function():
#      pass


# # Positional Only Arguments
# '''--> You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
#    --> To specifiy that a funciton can have only positional arguments add " , / " after the agurments.
# '''
# def my_function(x,/):
#      print(x)
# my_function(3)

# # without the ", / "you are actually allowed to use keyword argument even if the function expects positional arguments.
# def my_fun(x):
#      print(x)
# my_fun(x=3)

# # but when adding the " , / " you will get an error if you try to send a keyword argument.
# def fun(x,/):
#      print(x)
# fun(x=18)


# # Keyword-Only Arguments
# # TO specify that a function can have only keyword argument add " * ", before the arguments.
def my_function(*,x):
     print(x)
my_function(x=16)
   
# # without the *, you are allowed to use postional arguments even if the function expects keyword argument.
def my_fun(x):
     print(x)
my_fun(2)

# # But with the "*", you will get an error if you try to send a positional argument.
def fun(*,x):
     print(x)
fun(2003)  


# # Combine positional-only and keyword-only
# '''--> you can combine the two arguments types in the same function.
#    --> any agruments before the  /, are positional-only and only argument after the *, are keyword-only
# '''
# def function(a,b,/,*,c,d):
#      print(a+b+c+d)
# function(1,2,c=3,d=5)


# def add(*numbers):
#    return sum(numbers)
# print(add(1,100,1))


# def total_sum(*numbers):
#    result=0
#    for num in numbers:
#       result+=num
#    return result
# print(total_sum(1,2,3,4,5))


## keyword arguements
# def student_info(**details):
#    for key,value in details.items():
#       print(f"{key} : {value}")
# student_info(name="Virat", age="36",course="Cricket",country="India")


# # Lambda Function

# add=lambda a,b:a+b
# print(add(100,100))

# double = lambda a:a*2
# print(double(200))

# student= [ {"name":"Hemi","marks":100},
#           {"name":"Ram","marks":150},
#           {"name":"raju","marks":160}
#           ]
# student.sort(key=lambda x:x["marks"],reverse=True)
# print(student)



# # Recursion : Recursion occurs when a function calls itself.
# # it's used to solve problems that can be broken down into smaller, similar problems.

# def greet():
#    print("Hello")
#    greet()
# greet()

# def factorial(n):
#    if n==1:
#       return 1
#    return n * factorial(n-1)
# print(factorial(3))



# # NESTED FUNCTION
# A nested function is a function defined inside another function. 
# The function is onlt accessible wthini the outer function allowing for more modular and controlled code execution.

# def outer_fun(name):
#    def inner_fun():
#       print(f"Hello, {name}!")
#    inner_fun()
# outer_fun("Hemi")



# def calculate(a,b):
#    def add():
#       print(a+b)
#    def sub():
#       print(a-b)
#    def mul():
#       print(a*b)
#    add()
#    sub()
#    mul()
# calculate(10,2)




# # Home Work

# # 1. Lambda Function: wirte a lambda function that multiplies two numbers.
# multiplies= lambda x,y:x*y
# print(multiplies(20,10)) 

# # 2. Recursive Function:write a recursive function that calculate the sum of the first n numbers
# def sum_n_numbers(n):
#    return n*(n+1)//2

# print(sum_n_numbers(100)  )


# # # 3. Variable-length argumenets:write a function that accepts any numbers of arguments and return their average.
# def average(*n):
#    if len(n)==0:
#       return "no number is provided"
#    total=sum(n)
#    count=len(n)
#    return total/count
# number=range(1,100)
# print(average(*number))
