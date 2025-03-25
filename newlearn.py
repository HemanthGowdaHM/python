# class Book:
#     def __init__(self,name,author,pages):
#         self.name = name
#         self.author = author
#         self.pages = pages
        
#     def __str__(self):
#        return f"{self.name} by {self.author}"
        
#     def __len__(self):
#         return self.pages
        
#     def __del__(self):
#         print("A book objects has been deleted")
        
# A1 = Book("python Rocks "," jose",200)

# print(A1)
# print(str(A1))
# print(len(A1))
# del A1

# class Cylinder:
    
#     pi = 3.14
#     def __init__(self,height=1,radius=1):
#         self.height = height
#         self.radius = radius
        
#     def volume(self):
#         v = self.pi*self.radius**2*self.height
#         print(v)
        
#     def surface_area(self):
#         A = 2*self.pi*self.radius*(self.height + self.radius)
#         return A

# c = Cylinder(2,3)
# c.volume()
# print(c.surface_area())

# import math
# class Line:
    
#     def __init__(self,coor1,coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
        
#     def distance(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2
#         return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
#     def slope(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2
#         m = ((y2-y1)/(x2-x1))
#         return m
# c1 = (3,2)
# c2 = (8,10)

# myline = Line(c1,c2)

# print(myline.distance())

# print(myline.slope())