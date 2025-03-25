# # SETS
''' --> Set items are unordered, unchangeable, and do not allow a duplicate items or values.
    ---> Unordered : the items in a set do not have a defined order.
        set items can appear in a different order every time you use them, and cannot be referred to by index or key.
    --> Unchangeable : set item are unchangeable , meaning that cannot change the item after the set has been created.
    --> Dupliate not allowed : sets cannot two items with the same value
NOTE : Once a set is created, you cannot change its items, but you can remove items add new items
NOTE : The values "True" and "1" are considered the same value in set and are treated as duplicates.
NOTE : The values "False" and "0" are considered the same value in set and are treated as duplicates
'''
# # set
# my_set = { "apple","banana","cherry"}
# print(my_set)

# # To add ine item to set use the add() method 
# my_set = { "apple","banana","cherry"}
# my_set.add("orange")
# print(my_set)

# # To add items from another set into the current set, use the update() method.
# my_set1 = { "pineapple","mango","papaya"}
# my_set.update(my_set1)
# print(my_set)

# # Add Any Iterable ( The object in the update() method does not have to be a set, it can be any iterable object(tuples,list,dictionaiesy))
# my_set = { "apple","banana","cherry"}
# mylist = ["kiwi","strawberry"]
# my_set.update(mylist)
# print(my_set)

# mytuples = ("hello","hi")
# my_set.update(mytuples)
# print(my_set)

# mydict = {"fruit":"Guva",}
# my_set.update(mydict)
# print(my_set)

# # Remove Item ( to remve an item in a set, use the remove() or the discard() method ).
''' NOTE : If the item to remove does not exist, remove() will raise an error.
    NOTE : If the item to remove does not exist, discard() will NOT raise an error.
    NOTE : you can also use the pop() method to remove an item,
            but this method will remove a random item, so you cannot be sure what item that gets removed from the set.
'''
            
# my_set = { "apple","banana","cherry"}
# my_set.remove("apple")
# print(my_set)

# # my_set.remove("apple")
# # print(my_set)

# my_set.discard("banana")
# print(my_set)

# my_set.discard("apple")
# print(my_set)

# my_set = { "apple","banana","cherry"}
# my_set.pop()
# print(my_set)
# my_set.pop()
# print(my_set)

# my_set = { "apple","banana","cherry"}
# my_set.clear()
# print(my_set)

# my_set = { "apple","banana","cherry"}
# del my_set
# print(my_set)


# # The values ("True" and "1") and("False" and "0") are considered the same value in set and are treated as duplicates
# my_set = { "apple","banana","cherry",True,0,1,False}
# print(my_set)

# # length os set
# my_set = { "apple","banana","cherry",True,0,1,False}
# print(len(my_set))

# # Type() of set
# my_set = { "apple","banana","cherry",True,0,1,False}
# print(type(my_set))

# # The set() constructor
# my_set = set(( "apple","banana","cherry",True,0,1,False))
# print(my_set)
# print(type(my_set))

# # Access Set items by using Loops
# my_set = { "apple","banana","cherry",True,0,1,False}
# for i in my_set:
#     print(i)

# # # check if "banana" present in the set return True else print False.
# print("if banana is present in the set:","banana" in my_set)
# print("if banana is present in the set:","banana" not in my_set)
    