# # "for" loop
'''--> A for loop is used for iterating over a sequence (that is either a list, tuple, a dictionary, a set, or a string).
   --> with the for loop we can execute a set of statements once for each item ina list tuple, set, etc..
   --> The for loop does not require an indexing variable to set beforehand.
'''

# # Print each fruit in a fruits list
# Fruits = ["apple","banana","cherry"]
# for x in Fruits:
#     print(x)
    

# # The Break Stament
'''--> with the break statement we can stop the loop before it has loop thruogh all the items.'''

# # exit the loop when 'x' is "banana"
# Fruits = ["apple","banana","cherry"]
# for x in Fruits:
#     print(x)
#     if x == "banana":
#         break

# # Exit the loop when 'x' is "banana", but thid time the break comes before the print.
# Fruits = ["apple","banana","cherry","orange"]
# for x in Fruits:
#     if x =="cherry":
#       print(f"found {x}")
#       break
#     print(x)


# # Continue statement
'''--> with the continue statement we can stop current iteration of the loop, and continue with the next.'''

# # do not print "banana"  
# Fruits = ["apple","banana","cherry","mango"]
# for x in Fruits:
#     if x == "banana":
#         continue
#     print(x)
        
        
# # The range() function
'''--> to loop through a set of code a specified number of times we can use the range() function.
  --> The range() funstion return a sequence of number, 
      starting from 0 by default, and increments by 1(by default), and ends at a specified number.
'''

# NOTE : That range(10) is not the values of 0 to 10 , but the value 0 to 9.
# Using the range() function
# for x in range(10):
#     print(x)    


# # The range() function.
# The range() function default to increment the sequence by, however it is possible to specify the increment value by adding a third parameter   

# for x in range(2,30,3):   
#     print(x)

# # Else in for loop
'''--> The else keyword in a for loop specifies a blocks of code to be executed when the loop is finished'''   

# print all numbers from 0 to 9 and print a message when the loop has ended.
# for x in range(10):
#     print(x)
# else:
#     print("it is finished")


#  NOTE : The else block will not be executed if the loop is stopped by break statement.
# for x in range(5):
#     if x == 4:break
#     print(x)
# else:
#     print("it is finished")

# # Nested Loops 
'''--> a nested loop is a loop inside a loop.
   --> The "inner loop" will be executed one time for each iteration of the "outer loop".
'''

# # print each adjective for every fruit
# adj = ["red","big","tasty"]
# fruit = ["apple","banana","cherry"]

# for x in adj:
#     for y in fruit:
#         print(x,y)

# bag = ["red","green","blue"]
# for ball in bag:
#    print(ball)


# for i in range(1,11,3):
#    print(i,end=" ")

# name = "HemanthGowdaHM"
# for index,letter in enumerate(name):
#    print((index+1)*letter)

# l = [10,11,12,13,14,15,16,17,18]
# for index,num in enumerate(l):
#    print(f"{num} is in {index}th index")
   
# L=[1,2,3,4,5]
# for index,num in enumerate(L):
#    print(num*index+1)


# n = [1,2,3,4,5]
# for num in n:
#    print(num)
# else:
#    print("all print")
   
# for num in n:
#    print(num)
# print("all print")

# for num in n:
#    print(num)
#    if num==4:
#       break
# else:
#    print("all print")


# d ={"name":"hemi", "age":22,"income":1}
# # print(d.items())
# for key , value in d.items():
#    print(key,value)

# for i in range(1,11):
#    print(f"2x{1}={2*i}")

# for i in range(2,11):
#    for j in range(1,11):
#       print(f"{i}x{j}={i*j}")

# for i in range(1,30):
#    if i%3==0:
#       print(i)


# sum=0
# for i in range(1,11):
#    sum+=i
#    print(sum)
   
# name ="hemi"
# for i in name:
#    print(i)
   
# s = "hi hello everyone"
# i=['a','e','i','o','u','A','E','i','O','U']
# count =0
# for x in s:
#    if x in i:
#       count +=1
# print(count) 

# l =[1,2,3,4,5]
# dl =[]
# for num in l:
#    dl.append(num*2)
# print(dl)

# std_name = ["A","B","C","D"]
# std_marks = [90,89,87,78]
# std = {}
# for index, student in enumerate(std_name):
#    std[student] = std_marks[index]
# print(std) 


# # i=0
# import random
# print(random.randrange(1,30))


# for i in range(1,6):
#    for j in range(1,11):
#       print(f"{i}x{j}={i*j}")
      
# list="hemanthgowdahm"
# vowels=['a','e','i','o','u','A','E','I','O','U']
# count=0
# for i in list:
#    if i in vowels:
#       count=count+1
#       print(count)

# seats=8
# while seats>0:
#    print("book one seats")
#    seats=seats-1
#    print(f"Reamining seats are{seats}")
# print("all seats are booked")
   
# import time  
# i=10
# while i >0:
#    print(i)
#    time.sleep(1)
#    i=i-1
# print("happy new year..!")


# for i in range(3,4):
#    for j in range(1,11):
#       print(f"{i}x{j}={i*j}")

# for i in range(1,11):
#    print(f"3x{i}={3*i}")

# total=0
# for i in range(1,11):
#    total=total+i
#    print(total)

# name="hemi"
# for i in name:
#    print(i)

# s="hi hello i m hemanth gowda H M "
# l=["a","e","i","o","u","A","E","I","O","U"]
# count=0
# for i in s:
#    if i in l:
#       count=count+1
# print(count)

# foods=["idle","poori","dosa","bath"]
# u_foods=[i.upper() for i in foods]

# print(u_foods)
# total=0
# item={"pen":10,"pencil":15,"book":30}
# # for product, price in item.items():
# #       total+=price
# # print(total)
# print(sum[list{item.values()}])

# s=[num**2 for num in range(1,11)]
# print(s)
