# # Abstract Class
'''
--> An Abstract class in python is a class that cannot be instantiated directly 
    it cann have abstract methods, which must be implemented by subclass.
--> Abstract classes provide a blueprint for other classes, 
    enforcing a structure where subclasses must implement certain methods.
--> Use the ABC(Abstract Base Class) module to create abstract classes in python.
'''


# from abc import ABC, abstractmethod

# class vehicle(ABC):
#     @abstractmethod
#     def startEngine(self):
#         pass
    
    
# class Bike(vehicle):
#     def __init__(self,name):
#         self.name = name
        
#     def startEngine(self):
#         print("start Engine")
        
# b = Bike("Royal Enfield")
# print(b.name)



# # HW1 : write a class mobile with attributes brand and price. create two objects of the class and display their attributes using a method
# class mobile:
#     # constructor
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
        
#     # method   
#     def display_brand_price(self):
#         print(f"This { self.brand}  cost is {self.price}")
        
# #objects  
# M1 = mobile("moto",20000)
# M2 = mobile("Iphone",70000)

# # call the method to display the attributes
# M1.display_brand_price()


# # HW2  :
'''--> define a class student with attributes name and marks.
        write a method dipaly_info() that prints the student's name and marks.
        create multiple objects of the student class and call the method on each.
'''
# class student:
    
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def display_info(self):
#         print(f"{self.name} scored {self.marks}")
    
# S1 = student("Hemi",70)
# S2 = student("Ram",90)
# S3 = student("Raj",85)

# S1.display_info()
# S2.display_info()

# # HW3
'''-->  1. Create a class with a Constructor:
            write a class movie with attributs title and rating using the __init__() constructor.
            defie=ne a method to display the movies title and rating
        2.Add Defalut parameters:
            create a class employee with attributes name, designation and salary( default value of salary is 30000).
            write a method that display the details of each employee.
            create multiple employee objects with different values for name and designation, and test default salary behavior.
'''
# # 1 
# class movie:
#     def __init__(self,title,rating):
#         self.title = title
#         self.rating = rating
#     def display_info(self):
#         print(f"{self.title} {self.rating} out of 10")
        
# M1 = movie("Kalki",8.5)   

# M1.display_info() 

# # 2

# class Employee:
    
#     def __init__(self,name,designation,salary=30000):
#         self.name = name
#         self.designation = designation
#         self.salary = salary
    
#     def employee_info(self):
#         print(f"{self.name} and {self.designation} and {self.salary}")

# E1 = Employee("Ram","web deveploer",45000)
# E2 = Employee("raju","CEO")         

# E1.employee_info()
# E2.employee_info()


# # Hw4 : Encapsulation
'''--> create a bankaccount class with private attributes for account_number and balance.
        Add methods to check balance, deposit and withdraw funds.
        try accessing the balance directly and observe the result.
'''

# class BankAccount:
    
#     def __init__(self,account_number,balance):
#         self.__accunt_number = account_number
#         self.__balance = balance
        
#     def check_balance(self):
#         print(f"{self.__balance}") 
        
#     def deposit_funds(self,amount):
#         self.__balance += amount
#         print(f"deposit sucessfull amount {amount} now the avilable balance {self.__balance}")
        
#     def withdraw(self,money):
#         if self.__balance >= money:
#             self.__balance -= money
#             print(f"withdraw sucessfull - balance : {self.__balance}")
#         else:
#             print("insufficent funds")
            
# p1 = BankAccount("KGB3335",505)
# p1.check_balance()
# p1.withdraw(502)
# p1.deposit_funds(502)

# # Inheritance:
# # Create a base class vehicle with a start method. Then create a subclassBije with an additin+onal ride() method
# # Demonstrate how the bike can use both start and ride
# class vehicle:
#     def start(self):
#         print("vehicle is starting")
        
# class Bike(vehicle):
#     def __init__(self,name):
#         self.name = name

#     def ride(self):
#         print("riding")
        
# B1 = Bike("royal enfield")

# B1.start()
# B1.ride()
        
        
# # polymorphism:
# # implement a shape class and derive circle and rectangle class with a method calculate_area . 
# # each class should be calculate area differently based on its shape.
# # create a loop to calculate areas for both circle and rectangle objects.

class shape:
    def calc_area(self):
        print("area calculated")
        
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area_cricle(self):
        print(f" the area of the circle is {(22/7)*self.radius*self.radius}")
class rectangle(shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
        
    def area_rec(self):
        print(f"area of rectangle is {self.l*self.b}")

C = circle(2)
r = rectangle(3,2)

C.area_cricle()
r.area_rec()     