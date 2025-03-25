# # Polymorphism

'''--> Polymorphism allows objects of different classes to be treated as object of a common superclass, 
        but they can behave differently depending on the object type.
        
    --> Real-worldExample: Think of animals making sounds-both dogs and cats make sounds,
        but each produces a distinct sound.
        They share a common method make_sound(), but the output varies.
'''

# class Animal:
#     def make_sound(self):
#         print("Animal make sound")
    
# class Dog(Animal):
#     def make_sound(self):
#         print("Bark")
# class cat(Animal):
#     def make_sound(self):
#         print("meow")
        
# animals = [Dog(),cat()]
# for animal in animals:
#     animal.make_sound()

class notification:
    def send(self):
        print("notification sent")
class EmailNotification(notification):
    def send(self):
        print("email sent")
class smsnotification(notification):
    def send(self):
        print("sms sent")