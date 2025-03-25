# # Inheritance 
'''
    --> Inheritance allows a class to Inherit attributes and methods from another class, facilitating reuse.
    --> Consider human families. characteristics like surname, traditions, or physical features can be passed down from parents to children.
    
'''

# class Family:
#     def __init__(self,surname):
#         self.surname = surname
        
# class child(Family):
#     def __init__(self,surname,name):
#         super().__init__(surname)
#         self.name = name
        

# Child = child("Gowda","Hemi")
# print(f"{Child.surname} {Child.name}")


# class user:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
    
#     def login(self):
#         print(f"{self.username} logged in")


# class Admin(user):
#     def delete_user(self):
#         print("Admin deleted user")
        
        
# a = Admin("Hemi",1234)
# print(a.username)
# print(a.password)
# a.login()
# a.delete_user()


