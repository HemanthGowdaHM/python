# # Getter and setters :
'''--> create a classs Bankaccount with a private attribute balance:
        write a Getter method to retrive the balance and a setter method to update it, ensuring the balance never goes below zero.
'''

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance 
    
    def set_balance(self,updated_balance):
        if updated_balance < 0:
            print("balance cannot be a negative values")
        return self.__balance 


# # Method Overriding
'''--> create a parent class shape with a method draw() that printd "Drawing shape"
        create a child class that overrides draw() to print " DrawingCricle". 
'''

# class Shape:
#     def draw(self):
#         print("Drawing shape")
        
# class circle(Shape):
#     def draw(self):
#         super().draw()
#         print("Drawing Circle")
        
# C1 = circle()
# C1.draw()
