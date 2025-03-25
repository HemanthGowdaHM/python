# # Dictionary
'''--> Dictionaries are used to store data values in key:values pairs.
   --> A Dictionary is a collection which is unordered, mutable(changeable) and do not allow duplicates.
   --> Dictionaries are written eith curly brackets, and have keys and values.
   '''
   
# my_dict = {"brand":"Ford","model":"Mustang","year":"1964"}
# print(my_dict)

# # Duplicate not allowed.(Duplicate values will overwrite exisiting values)
# my_dict = {"brand":"Ford","model":"Mustang","year":1964,"year":1964,"model":"electric"}
# print(my_dict)

# #Dictinoary Length
# my_dict = {"brand":"Ford","model":"Mustang","year":"1964"}
# print(len(my_dict))

# # Dictionary Items - data types( any Data types)
# my_dict = {"brand":"Ford","model":"Mustang","year":1964,"color":["red","black","white"],"electric":False}
# print(my_dict)
# print(type(my_dict))

# # The dict() Constructor
# # it is also possible to use the dict() constructor to make a dictionary.
# thisdict = dict(name="virat",age=36,country="India")
# print(thisdict)
# print(type(thisdict))


# # Accessing Items
'''--> you can access the items of a dictionary by referring to its key name, inside square brackets.
   --> there also a method called " get() " that will give you the same result.
'''

# my_dict = {"brand":"Ford","model":"Mustang","year":"1964"}
# x = my_dict["model"]
# print(x)

# print(my_dict["model"])

# print(my_dict.get("models","not found"))   #safe access method is get.


# # Get keys 
'''--> The keys() method will return a list of all the keys in the dictionary.
   -->Add a new item to the original dictionary and see that the keys list gets updated as well.
'''
# cars = {"brand":"Ford","model":"Mustang","year":1964}
# print(cars.keys())

# cars["color"]="red"
# print(cars.values())


# # Get Values 
'''-->The values() method will return a list of all the values in the dictionary.
   -->Make a change in the original dictionary and see that the values list gets updated as well.
'''
# cars = {"brand":"Ford","model":"Mustang","year":1964}
# print(cars.values())

# cars["color"]="red"
# print(cars.values())


# # Get items
'''--> The items() method will return each item in a dictionary, as tuple in a list.
   --> Make a change in the original dictionary and see that the items list gets updated as well.
'''
   
# cars = {"brand":"Ford","model":"Mustang","year":1964}
# print(cars.items()) 

# cars["year"]=2024
# cars["color"] = "red"
# print(cars.items())


# # Check if key exists
'''--> to determine if a sepcified key is present in a dictionary use the " in " keyword.
'''
# cars = {"brand":"Ford","model":"Mustang","year":1964}
# if "model" in cars:
#     print(" yes, model is one if the key in the cars dictionary")


# # Update dictionary
'''--> the update() method will update the dictionary with the items from the given argument.
   --> The update must be a dictionary or an iterable object with key:value pair.
'''

# cars = {"brand":"Ford","model":"Mustang","year":1964}
# cars.update({"year":2024,"brand1":"ford2"})
# print(cars)


# # Remove Dictionary Items
'''--> The pop() method removes the item with the specified key name.
   --> The popitem() method removes the last inserted item.
   --> The del keyword removes the item with the specified key name.
   --> The del keyword can also delete the dictionary completely.
   --> The clear() method empties the dictionary.
'''

# cars = {"brand":"Ford","model":"Mustang","year":1964}
# cars.pop("model")
# print(cars)

# cars = {"brand":"Ford","model":"Mustang","year":1964}
# cars.popitem()
# print(cars)

# cars = {"brand":"Ford","model":"Mustang","year":1964}
# del cars["brand"]
# print(cars)

# cars = {"brand":"Ford","model":"Mustang","year":1964}
# del cars
# print(cars)

# cars = {"brand":"Ford","model":"Mustang","year":1964}
# cars.clear()
# print(cars)


# # Loop Dictionary
'''--> '''

# # Print all key names in the dictionary one by one
# cars = {"brand":"Ford","model":"Mustang","year":1964}
# for x in cars:
#     print(x)

# # you can also use the keys() method to return keys of a dictionary.
# for x in cars.keys():
#     print(x)

# # print all values in the dictionary one by one
# for x in cars:
#     print(cars[x])
    
# # you can also use the values() method to return values of a dictionary.
# for x in cars.values():
#     print(x)
    
# # loop through both keys and values, by using the items() method.
# for x, y in cars.items():
#     print(x, y)


# # Copy Dictionary
'''--> Make a copy of dictionary with the copy() method.'''

# cars = {"brand":"Ford","model":"Mustang","year":1964}
# cars1 = cars.copy()
# print(cars1)

'''--> Another way to make a copy is to use the bulit-in function " dict() ".'''
# cars = {"brand":"Ford","model":"Mustang","year":1964}
# cars1 = dict(cars)
# print(cars1)



# # Nested Dictionaries
'''--> A Dictionary can contain dictionary this is called nested dictionaries.'''

# myfamily = { "child1":{"name":"rajat", "year":2024},
#              "child2":{"name":"siraj","year":2019},
#              "child3":{"name":"dayal","year":2023}}
# print(myfamily)

# child1={"name":"rajat", "year":2024}
# child2={"name":"siraj","year":2019}
# child3={"name":"dayal","year":2023}
# myfamily1={"child1":child1,"child2":child2,"child3":child3}
# print(myfamily1)

# # Access items in nested Dictinoary
# print(myfamily["child2"]["name"])

# # Loop through nested dictionary( you can loop through a dictionary by using the " items()" method. )
# for x, obj in myfamily.items():
#     print(x)

# for x ,obj in myfamily.items():
#     print(f"the {x}:{obj}")
    
   #  for y in obj:
   #      print(y+':',obj[y])
 
# items1 = { 
#           "name":"milk",
#           "weight":1,
#           "price":24
#           }
# items2 = {
#          "name":"sugar",
#           "weight":2,
#           "price":99.9
# }
# print(f"total weight:{items1["weight"]+items2["weight"]}kg")
# print(f"total price:{items1["price"]+items1["price"]}")