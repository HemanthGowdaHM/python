# # LAMBDA FUNCTION 
''' --> lambda function is small anonymous function. 
    --> A lambda function can take any number of arguments, but can only have one expersion.    
    --> syntax:  lambda arguments : expresion 
'''
# # ADD 10 to arguments a, and return the result .
# add=lambda a : a + 10 
# print(add(10))

# sub = lambda b : b - 20
# print(sub(30))

# # # Multiple arguments " a " with arguments "b" and return the result.
# multiply = lambda a, b : a * b
# print(multiply(10,10))

# add=lambda a ,b ,c : a+b+c
# print(add(10,20,30))


# # WHY USE LAMBDA FUNCTION
''' ---> The Power of lambda is better when you use them as an anonymous function inside another function.
    ---> say you have a function defination that takes one argument, and that argument will be multiplied with an unknown number.
'''

# def my_fun(n):
#     return lambda a : a * n

# # Use that function definition to make a function that always doubles the number you send in :

# def my_fun(n):
#     return lambda a : a * n
# doubler = my_fun(2)
# print(doubler(10))

# triples = my_fun(3)
# print(triples(20))

# # Using MAP fucntion
# def square(num):
#     return num**2
# print(square(10))
# my_nums = [1,2,3,4,5,6]
# for item in map(square,my_nums):
#     print(item)

# def fun(names):
#     if len(names)%2==0:
#         return "EVEN"
#     else:
#         return names[0]
# name=["Hemi","ram","raju","hi"]
# list1=list(map(fun,name))
# print(list1)



# # FILTER function

# def check_even(num):
#     return num%2==0
# my_nums=[1,2,3,4,5]
# list1=list(filter(check_even,my_nums))
# print(list1)
# for i in my_nums:
#     print(i%2==0)



# num = lambda i:i**2
# print(num(10))


# # LEGB Rules
# # Local - Names assigned any way within a function ( def or lambda) and not declared global in that funciton.
# # Enclosing function locals - Name in th local scope of any and all enclosing function( def or lambda ),from inner to outer.
# # Gobal (module) - name assigned at the top-level of a module file, or declared global in a def within the file.
# # Built-in(Python) - names preassigned in the built-in names module:open,range,syntaxError....


# x = 25
# def num():
#     x = 50
#     return x
# print(num())
# print(x)


# # local variable 
# lambda num:num**2


# # this is global string
# name = "this is a global stirng"
# def greet():
#     # this is a local string
#     name = "hemi"
#     def hello():
#         print("hello "+name)
#     hello()
# greet()

# x = 50 
# def fun():
#     global x
#     print(f'x is {x}')
    
#     # local reassignement a global variable!
#     x = 200
#     print(f" i just locally chnaged x to {x}")
# print(x) 

# fun()


#  # volume of sphere 
# def fun(rad):
#     return (4/3)*(3.14)*(rad**3)
# print(fun(10)) 



# s = " Hi Hello Everyone..!!"
# def upper_lower_count():
    
#     lowercase = 0
#     uppercase = 0
    
#     for char in s:
#         if char.islower():
#             lowercase += 1
#         elif char.isupper():
#             uppercase += 1
#         else:
#             pass
#     print(f"original string: {s}")
#     print(f" lowercase : {lowercase}")
#     print(f" uppercase : { uppercase}")
# upper_lower_count()