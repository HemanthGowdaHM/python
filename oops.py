# NOTE : what is object-oriented programming.
'''--> oop is a programming paradigm that organizes software design around data, or object, rather than function and logic.
   --> it allows for bettre modularity and code reusability by creating bojects that model realworld entities.
   
# class:
--> A class is a buleprint for creating objects. it defines the attributes and behaviors of the objects created from it.


# object:
--> An object is an instance of a class. each object has its own attributes(data) and can perform actions through methods(functions)

# Attributes:
--> characteristics that defines an objects. for example, in the car class, brand and model are attributes.

# Methods:
--> Function defines inside a class that describe the behaviors of an objects.
'''

# class car:
#     # Attributes
#     def __init__(self,brand ,model):
#         self.brand = brand              # Instance variable
#         self.model = model              # Instance variable
    
#     # method
#     def display_info(self):
#         print(f"car brand : {self.brand} , model :{self.model}")
        
# # creating an object of the class
# my_car = car ("Toyota","corolla")
# my_car.display_info()

''' # car is class.
    # my_car is an object of the car class.
    # brand and model are attributes of the object.
    # display_info is method that display the car's details.
'''


# class Human:
    
#     def __init__(self,name):
#         self.name = name
        
#     def walk(self):
#         print(f"{self.name} is walking")
        
# H1 = Human("Hemi")
# H2 = Human("Jayanth")

# H1.walk()
# H2.walk()        



# class mobile:
#     # define the attributes
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
    
#     # method 
#     def mobile_info(self):
#         print(f"The new brand mobile is {self.brand} and price is {self.price}")

# # creating the objects
# m1 = mobile("moto",21000)
# m2 = mobile("oneplus",18000)

# m1.mobile_info()
# m2.mobile_info()



# NOTE :  Constructors and the selfkeyword

# The __init__() Constructor
''' --> constructor : The constructor __init__() method in python is a method that intializes an objects when it's created.
                      It's called automatically when you created new instance of a class.
    --> purpose : It allows you to set the inital state of the object by defining its attributes.
    
    --> syntax :  class classname:
                        def __init__(self,paramter1,parameter2):
                            self.parameter1 = parameter1
                            self.parameter2 = parameter2
                            
    --> Here , __init__() receives parameters and sets the inital values of objects attributes. 
'''


# NOTE : Using self in class methhods
'''
    --> Self : refers to the instanace of the class itself, allowing you to access attributes and methods within a class.
    --> It is automatically passed as the first arguments to methods within th class.
    --> NOTE : while self is a covention, you can technically use any name (through it's not recommeneded for readability).
    --> Here, self.name and self.age are instance variables.
                introduce() is a method that access the instance varibales using self.
'''
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def person_info(self):
#         print(f"My self {self.name} and  i'm {self.age} year old ")
        
# p1 = person("Hemi",22)        
# p2 = person("Ram",25)


# p1.person_info()
# print(p1.name)
# print(p1.age)


# NOTE : Optional parameter in constructors
'''
    --> Sometimes it's help to have default values for cretain attributes. 
        You can do this by setting default values for parameters in __init__().
'''

class person:
    def __init__(self,name,age,salary=-1):
        self.name = name
        self.age = age
        self.salary = salary
    
    def person_info(self):
        print(f"My self {self.name} and  i'm {self.age} year old ")
        
p1 = person("Hemi",22,5)        
p2 = person("Ram",25)


p1.person_info()
print(p1.name)
print(p1.age)
print(p1.salary)
print(p2.salary)