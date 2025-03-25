# # python loops
# The while loop repeatedly executes a block of code as long as the condition is true.
'''--> python has two primitive loop commands ( for loops)( while loops)
   --> with the while loop we can executes a set of statements as long as a conditionis true.
   '''

# # print i as long as i is less than 6
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# output 1 2 3 4 5

# # The break statement
'''--> with the brak statement we can stop the loop even is the while condition is true.'''

# exit the loop when i is 3.
# i = 0
# while i < 6:
#     i += 1
#     if i==4:
#         break
#     print(i)

# i = 1
# while i <= 10:
#     print(i)
#     if i == 8:
#         break
#     i += 1 

# # The continue statement we can stop the current iteration, anf continue with the next.
# i = 0
# while i <= 10:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# a = [1,2,3,4,5]
# itr = iter(a)
# tuple(itr)


# is_failed = True
# i = 1              #attempt
# while is_failed and i<=100 :
#    print(f"Try {i}")
#    i += 1
# print("i give up")

# is_failed = True
# i = 1
# while is_failed:
#    if i%2!=0:
#       i = i+1
#       continue
#    print(f"Attempt {i}")
#    i = i+1
#    if i>100:
#       break
# print("i give up")

# i = 0
# while i<=10:
#    x = 0
#    while x<i:
#       print(i*"hemi",end="-")
#       x +=1
#    print("")
#    i +=1

import time
pin = '1234'
# input_pin = input("enter the pin:")
trails = 1
while trails <=3:
   input_pin = input(f"trail-{trails} | enter the pin:")
   trails +=1

   if input_pin == pin:
      print("CORRECT")
      break
   elif trails ==3:
      if input_pin != pin:
         print("wait a sec..!")
         time.sleep(10)
   else:
      print("INCORRECT")

   

# pin = ""
# correct_pin = "1234"
# while pin != correct_pin:
#    pin = input("enter the pin:")
#    if pin != correct_pin:
#       print("enter the correct pin")
# print("PIN accepted , you can proced")

# branch = ""
# branch_ISE ="ISE"
# while branch != branch_ISE:
#    branch = input("enter the branch:").upper()
#    if branch != branch_ISE:
#       print("this is not your branch")
# print("ok, you'r belongs to our branch")

# # write a program taht counts from 1 to 10 using a while loop.
# i = 1
# while i <= 10:
#    print(f"Times{i}",i)
#    i += 1

# # creat a program that prints all odd numbers b/w 1 to 20 using a while loop.
# i = 1
# while i <20:
#    if i%2 !=0:
#       print(i)
#    i = i+1

# # writea program that simulate a bus tucket booking system. the bus has 10 seats.
# # Each time a available seats decrease. when there are no seats left, the loop  stops and display a message saying"All seats are booked".
# available_seats = 10

# while available_seats >0:
#    print(f"{available_seats}available for booking")
#    booking = input("Do you want book seats?(yes/no):").lower()
   
#    if booking == "yes":
#       available_seats -= 1
#       print("seat is booked")
#    else:
#       print("no booking is made")
   
# print("All seats are booked")


# # Write program that counts down from 10 to 1 using a while loop and prints " Happy New Year " after the countdown is over.
# import time
# countdown = 10
# while countdown>0:
#    print(countdown)
#    time.sleep(1)
#    countdown -= 1
# print("Happy New Year..!")   


   

# is_failed=True
# i=0
# while is_failed :
#     if i%2==0:
#         print(f"try{i}")
#     if i>=100:
#         break
#     i+=1
# print("i try the max time")




