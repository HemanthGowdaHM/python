# # Getters, Setters, MethodOverloading and Overriding, super(), Abstract classes
'''
    --> Getter and Setters are methods that allow controlled access to an object's attributes.
    --> Putpose: They help in validating data, protecting data from accidental modification and providing controlled access.
'''

# class student:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
    
#     def get_name(self):         #Getter
#         return self.__name 
    
#     def get_age(self,age):
#         if isinstance(age, int):
#             self.__age = age
#         else:
#             print("ERROE in input")    
            
#     def set_name(self,name):
#         self.__name = name
    
    
        
# s = student("Hemanth",23)

# print(s.get_name())

# s.set_name("jayanth")

# print(s.get_name())

# # s.get_age(100)
# # s.get_age("2000")



# # Method Overloding
'''
    --> Method overloding is the ability to define multiple methods with the same name but different parameters.
    --> NOTE : python Doesn't support method overloding directly,
                but we can achieve it by using defalut parameter or by handling varying numbers of arguments  with *args and **kwargs .
'''

# class Calculator:
 
#     def add(self,a,b,c=0): # Handles both 2 and 3 parameter cases
#         print(a+b+c)
        
# C = Calculator()
# C.add(1,2)            # Two arguments
# C.add(1,2,3)          # Three arguments

# # Method Overriding
'''
    --> Method Overriding allows a child class to provide a specific implementation for a method athat is already defined in its parent.
    --> Purpose : It enables a child class to alter or extend the behavior of a parent class method.
'''

# class Animal:                               # Parent class
    
#     def make_sound(self):
#         print("Animals make a sound")
    
# class Dog(Animal):                          # Child class
#     def make_sound(self):
#         print("Bark")

# D = Dog()
# D.make_sound()


# # Super() Function
'''
    --> The Super() function is used in child classes to call a method from the parent class,
        enabling access to inhertance methods or attributes.
    --> Purpose : It ensure that the parent class's method is executed alongside any additional functionality added in th child class,
                    useful when overriding methods but still needing to incoprate the parent's behavior.
'''
#
# class Animal:                               # Parent class
#
#     def make_sound(self):
#         print("Animals make a sound")
#
# class Dog(Animal):                          # Child class
#
#     def __init__(self,name):
#         self.name = name
#
#     def make_sound(self):
#         super().make_sound()
#         print(f"{self.name} is Barking")
#
# D = Dog("Doggy")
# D.make_sound()

