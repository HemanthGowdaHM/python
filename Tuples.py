# # Tuples
'''--> A Tuple is a collection which is ordered and immutable(unchangeable), and allows duplicate values. 
   --> Tuples are written with round brackets "tuple()"
   --> Tuple is one of 4 bulit-in data types in python used to store collections of data, and other 3 are list,set,dictionary.
'''
# #  Example
# my_tuple = ("virat","kohli","king",18,"cheeku")
# print(my_tuple)

# # allow a duplicate values.
# my_tuple = ("virat","kohli","king",18,"cheeku","virat","kohli")
# print(my_tuple)

# # Tuple length
# my_tuple = ("virat","kohli","king",18,"cheeku")
# print(len(my_tuple))

# # Create tuple with one item
''' --> To create a tuple with only one item, you have to add a comma after the item, otherwise python will not recognize it as a tuple.''' 
# my_tuple = ("viratkohli",)
# print(type(my_tuple))

# my_tuple = ("viratkohli")
# print(type(my_tuple))

# # Tuple items - Data types ( tuple item can be of any data type).
# my_tuple = ("virat","kohli","king",18,"cheeku",True,5.11)
# print(my_tuple)

# # The tuple() Constructor( NOTE:Double round bracket).
# my_tuple = tuple(("virat","kohli","king",18,"cheeku"))
# print(my_tuple)


# Change Tuple Values
'''--> since tuple are immutable, they do not have a built-in append(), insert(), remove(), clear(),pop(),del functions,
       but there are other ways ti add items to a tuple.
    --> 1. Convert into a list: Just like the wordround for changing a tuple, you can convert it into a list. Add your item(s), 
           and convert it back into a tuple.
    --> 2. Add tuple to a tuple: you are allowed to add tuples to tuples, so if you want to add one item, (or many), 
           create a new tuple with the item(s), and add it to the existing tuple.'''
# # convert into list:   
# my_tuple = ("virat","kohli","king",18,"hello","hi")
# my_list = list(my_tuple)
# my_list.append('cheeku')
# my_list.remove("hello")
# my_list.insert(5,"Runmachine")
# my_list.pop(4)
# my_list.clear()
# my_tuple = tuple(my_list)
# print(my_tuple)

# # Add tupleto a tuple:
# my_tuple = ("virat","kohli","king",18,"cheeku")
# my_tuple1 = ("Hero",)
# my_tuple += my_tuple1
# print(my_tuple)


# # Unpacking a Tuple
'''--> when we create a tuple, we normally assign values to it, this is called " packing" a tuple:'''
# # Example:
# fruits = ("apple","banana","cherry")

'''--> But, in python we are also allowd to extract the values back into variables,This is called "Unpacking":'''
# # Example:
# fruits = ("apple","banana","cherry")
# (green,yellow,red) = fruits
# print(green)
# print(yellow)
# print(red)
# print(green,yellow,red)

'''NOTE: The number of variables must match the number of values in the tuple , 
        if not you must use as asterisk(*) to collect the remianing values as a list.'''

# # Using Asterisk*
# fruits = ("apple","banana","cherry","strawberry","raspberry")
# (green,yellow,*red) = fruits # or
# (green,*yellow,red) = fruits
# print(green)
# print(yellow)
# print(red)

# Loop Tuples
# fruits = ("apple","banana","cherry","strawberry","raspberry")
# for x in fruits:
#     print(x)

# for x in range(len(fruits)):
#     print(x,fruits[x])

# for x in range(5):
#     print(x,fruits[x])

# i=0
# while i < len(fruits):
#     print(i,fruits[i])
#     i=i+1
    