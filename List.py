# LIST
'''-->list are used to store multiple items in a single variable 
   -->list items are ordered, mutable(changeable),and allow a duplicate values 
   -->Ordered(it means that the item have a defined order, and that order will not change)
   -->Changeable(that we can change, add, and remove in a list after it has been created) 
   -->Allow Duplicate items(lists are indexed,list can have items with the same value)
   -->list items can be of any data type string, int and boolean data types'''


# mylist = ["apple","ram","kohli","siraj","rahul",16.02,18,True,"ram"]
# print("my list :",mylist)

# # LIST LENGTH
# # to determine how many items a list has, use the " len()" function
# mylist1 = ["apple","ram","kohli","siraj","rahul",16.02,18,True,"ram"]
# print("length of my list is :",len(mylist1))

# # " type() "
# mylist2 = ["apple","ram","kohli","siraj","rahul",16.02,18,True,"ram"]
# print(type(mylist2))

# # The "list()" constructor
# # it is also possible to use the list() constructor to make list when creating a new list
# my_list = list(("apple","ram","kohli","siraj","rahul"))
# print("my list:",my_list)


# # Access Items 
# # -->List items are indexed and you can access them by referring to the index number.
# # -->first item has index 0.

# mylist = ["apple","ram","kohli","siraj","rahul",16.02,18,True,"ram"]
# print("element with zero th index is :",mylist[0]) 
# print("index:",mylist[8])


# # Negative indexing
# # --> Negative indexing start from the end (-1 refer to the last item , -2 refer to the second last item ).
# mylist = ["apple","ram","kohli","siraj","rahul",16.02,18,True,"ram"]
# print("negative index :",mylist[-1])
# print("negative index :",mylist[-3])


# # Range of Indexes([start:stop:step])
# mylist = ["apple","ram","kohli","siraj","rahul",16.02,18,True,"ram"]
# print("Range of index :",mylist[0:9])
# print("Range of index :",mylist[0:9:2])
# print("Range of index :",mylist[0:9:3])
# print("Range of index :",mylist[-4:-1])


# # check if item Exists
# # -->to determine if specified item is present in a list use the "in" keyword.
# mylist = ["apple","ram","kohli","siraj","rahul",16.02,18,True,"ram"] 
# if "kohli" in mylist:
#    print("yes, kohli is in the mylist")

# # change iten value 
# # --> to cahnge the vaule of a specific item,refer to the index number
# mylist = ["apple","ram","kohli","siraj","rahul",16.02,18,True,"ram"]
# mylist[0]="Abdeviliers"
# print(mylist)

# mylist[1:2]=["gunman"]
# print(mylist)

# # Insert Items 
# # -->to insert a new list item, without replaceing any of the existing values, we can use the "insert()" method.
# mylist = ["apple","ram","kohli","siraj","rahul",16.02,18,True,"ram"]
# mylist.insert(0,90)
# mylist.insert(7,"book")
# print(mylist)


# # Add List item
# # Append items ( to add an item to the end of the list use the "append()" method ).

# my_list = ["apple","ram","kohli","siraj","rahul",16.02,18,True,"ram"]
# my_list.append("Abdevillier")
# print(my_list)

# # Extend List( To append elements from another list to the current list, use the extend() method ).
# my_list = ["apple","ram","kohli","siraj","rahul"]
# my_list1 = [16.02,18,True,"ram"]
# my_list.extend(my_list1)
# print(my_list)


# # Add any Iterable ( the "extend()" method does not have to append lists you can add any iterable object(tuples,sets,dictionaries)).
# my_list = ["apple","ram","kohli","siraj","rahul"]
# my_tuple = (16.02,18,True,"ram")
# my_list.extend(my_tuple)
# print(my_list)

# # Remove List( the "remove(item)" method is used to removes the specified item from the list ).
# my_list = ["apple","ram","kohli","siraj","rahul"]
# my_list.remove("apple")
# print(my_list)

# # Remove specified index ( the "pop(indexvaule)" method removes the specified index).
# # If you do not specify the index the pop() method removes the last item.
# my_list = ["apple","ram","kohli","siraj","rahul"]
# my_list.pop(0)
# print(my_list)
# my_list.pop()
# print(my_list)

# The "del" keyword also removes the spedified index.
# The "del" keyeword can also delete the list compeletely.
# my_list = ["apple","ram","kohli","siraj","rahul"]
# del my_list[0]
# print(my_list)

# my_list10 = ["apple","ram","kohli","siraj","rahul"]
# del my_list10
# print(my_list10)

# #  clear the list ( The "clear()" method emptied the list . The list still remains but it has no content.)
# my_list = ["apple","ram","kohli","siraj","rahul"]
# my_list.clear()
# print(my_list)

# # LOOP LISTS
# # you can loop through the list otems by using a "for" loop ( print all items in the list one by one).
# my_list = ["apple","ram","kohli","siraj","rahul"]
# for  i in my_list:
#    print(i)
   
# # Loop Through the index ( you can also loop through the list items by reffering to thier index number)
# # Use the " range() " and "len()" function to create a sutiable iterable.
# my_list = ["apple","ram","kohli","siraj","rahul"]
# for i in range(len(my_list)):
#    print(my_list[i])
   
# my_list = ["apple","ram","kohli","siraj","rahul","rajat","akashdeep"]
# for i in range(5):
#    print(my_list[i])

# #  Using a while Loop ( you can loop through the list items by using a While loop)
# # ( use the "len()" function to determine the length of the list, 
# # then start at 0 and loop your way through the list otemd by refering to thier indexes ).
# my_list = ["apple","ram","kohli","siraj","rahul","rajat","akashdeep"]
# i = 0
# while i < len(my_list):
#    print(my_list[i])
#    i = i+1

# my_list = ["apple","ram","kohli","siraj","rahul","rajat","akashdeep"]
# i = 0
# while i < 5:
#    print(my_list[i])
#    i = i+1


# # LIST Comprehension
''' List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
    Example:
    Based on a list of fruits, you want a new list containing only the fruits with the letter "a" in the name
    without list comprehension you will have to write a for statement with a conditional test inside '''
    
# fruits = ["apple","banana","cherry","kiwi","mango"]
# newlist = []
# newlist = [x for x in fruits]
# for x in fruits:
#    if "a" in x:
#       newlist.append(x)
# print(newlist)

# # syntax " newlist=[expression for item in iterable if condition==True] "
# fruits = ["apple","banana","cherry","kiwi","mango"]
# new_list = [ x for x in fruits if "a" in x]
# newlist = [ x for x in fruits if x != "apple"]
# print(new_list) 
# print(newlist)

# newlist = [x for x in range(10) if x < 5]
# print(newlist)

# fruits = ["apple","banana","cherry","kiwi","mango","banana","orange"]
# newlist=[x.upper() for x in fruits]
# newlist=['hello' for x in fruits]
# newlist=[x if x!="banana" else "orange" for x in fruits]
# print(newlist)


# # SORT LISTS
'''--> List object have a "sort()" method that will sort the list alphanumerically,ascending, by default.
   --> to sort desecending, Use the keyword argument "reverse=True".
   --> By default the sort() is case sensitive, resultiing in all capital letters being sorted before lower case letters.
'''
   
# fruits = ["apple","banana","cherry","kiwi","mango","banana","orange"]
# fruits.sort()
# fruits.sort(reverse=True)
# print(fruits)

# list = [10,20,30,40,50,60,70,80,90.123,90.0123]
# list.sort()
# print(list)

# fruits = ["apple","banana","cherry","Kiwi","Mango","Banana","orange"]
# fruits.sort()
# print(fruits)
# # '''If you want a case-insensitive sort function,use "key=str.lower" as a key function.'''
# fruits.sort(key=str.lower)
# print(fruits)

# # COPY A LIST
'''--> use the "copy()" method
   --> use the "list()" method
   --> use the slice operator
'''
# fruits = ["apple","banana","cherry","Kiwi","Mango","Banana","orange"]
# myfruits = fruits.copy()
# print("myfruits:",myfruits)

# fruits = ["apple","banana","cherry","Kiwi","Mango","Banana","orange"]
# myfruits = list(fruits)
# print("myfruits:",myfruits)

# fruits = ["apple","banana","cherry","Kiwi","Mango","Banana","orange"]
# myfruits = fruits[:]
# print("myfruits:",myfruits)

# # JOIN TWO LISTS
'''--> There are several ways to join or, concantenate, two or more lists in python.
   --> one of the easiest ways are bu using the "+" operator.
   --> using appending all the items from list2 into list1, one by one.
   --> you can use the extend() method 
'''
# list1 = ["a","b","c"]
# list2 = [1,2,3,4]
# list3 = list1 + list2
# print(list3)

# list1 = ["a","b","c"]
# list2 = [1,2,3,4]
# for x in list2:
#     list1.append(x)
# print(list1)

# list1 = ["a","b","c"]
# list2 = [1,2,3,4]
# list1.extend(list2)
# print(list1)
