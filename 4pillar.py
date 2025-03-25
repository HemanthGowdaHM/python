# # Pillars - OOP
''' 1. Abstraction
    2. Encapsulation
    3. Inheritence
    4. polymorphism
'''

# # ABSTRACTION
'''
    --> Abstraction hides the complex inner working of an object,
        exposing only the essenital parts for interaction.
        
    --> Real-worldExample : Think about driving a car. You Use the steering, wheel and pedals to
                            control the car, without needing to know the engine mechanics or 
                            braking systems.
    
'''

# class car:
    
#     def start_engine(self):
#         print("Engine started")
    
#     def accelerate(self):
#         print("car accelerating")
        
#     def brake(self):
#         print("car Stopping")

# car = car()
# car.start_engine()
# car.accelerate()
# car.brake()


# # Encapsulation
''' --> Encapsulation involves wrapping data and methods that operates on that data within one unit, such as class.
        This protects the data from external interference and misuse, improving security and maintainability.
        
    --> Real-world Example : Imagine an ATM machine - you interact with a limited interface 
                                (e.g., withdraw,deposit, check balance) but do not have access 
                                to the inner mechanics or  backend functions
'''

# class ATM:
    
#     def __init__(self,balance):
#         self.__balance = balance          # Private attribute
        
#     def deposit(self,amount):
#         self.__balance += amount
#         print(f" Deposited {amount}. new balance:{self.__balance}")
        
#     def withdraw(self,amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f" withdraw { amount}. new balance: { self.__balance}")
#         else:
#             print("Insfficient balance")
# atm = ATM(1000)
# atm.deposit(500)
# atm.withdraw(300)



# class Database:
#     def __init__(self):
#         # self.storage = {}               # Public attribute
#         # self._storage = {}              # protected
#         self.__storage = {}             # private
    
#     def write(self,key,value):
#         self.__storage[key] = value
        
#     def read(self,key):
#         if key in self.__storage:
#             print(self.__storage[key])
#         else:
#             print("Key is not found in database")

# db = Database()
# db.write("Hemi",23)
# db.read("Hemi")
# db.write("name","hello")
# # print(db.storage)

# db.read("name")

# # Encapsulation : restricting direct access to some data and methods to prevent accidental modification.
# class BankAccount:
#     def __init__(self,Account_number,balance):
#         self.__Account_number = Account_number
#         self.__balance = balance
    
#     def check_balance(self):
#         print(f"the balance is {self.__balance}")
    
#     def deposit(self,amount):
#         self.__balance += amount
#         print(f"The Deposited ammount is {amount} new balance is {self.__balance}")
    
#     def withdraw_funds(self,amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f" The balance after withdraw {amount} the avilable balance is {self.__balance}")
#         else:
#             print("Insufficent balance")
# account = BankAccount("1234",1000)
# account.check_balance()
# account.deposit(500)
# # account.__balance()     # o/p : "BankAccount" object has no attribute '__balance'.



