#  Examples

# for i in range(1,20):
#     if i%3==0:
#         print(i)

# total = 0
# numbers = [10,20,30,40,50]
# for i in numbers:
#     total+=i
# print(total)

# rows =5
# for i in range(1,rows+1):
#     for j in range(i):
#         print("*",end=' ')
#     print()

# row = 5
# for i in range(1,row+1):
#     print("*"*i)
    
# row = 5 
# for i in range(row,0,-1):
#     print("*"*i)
    
# row = 5
# for i in range(row,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(3):
#     print(i)
# else:
#     print("done")
    
# for i in range(2):
#     for j in range(2):
#         print(i,j)
        
# sum=0
# for i in range(1,101):
#     if i%5==0:
#         sum+=i
# print(sum)       

# sum of integers which are divisible by 5 from 1 to 100
# print(sum([i for i in range(5,101,5)]))

# sum of integer which are divisible by 2 from 1 to 50
# print(sum([i for i in range(2,51,2)]))





# # returns the lesser of two given numbers if both numbers are even,but returns the greater if one or both are odd.
# def lesser_of_even(a,b):
#     if a % 2 == 0 and b % 2 == 0:
#         if a<b:
#             result=a
#         else:
#             result=b
#     else:
#         if a>b:
#             result=a
#         else:
#             result=b
#     return result
# # lesser_of_even(2,5)
# print(lesser_of_even(2,3))



# def lesser_of_even(a,b):
#     if a%2==0 and b%2==0:
#         return min(a,b)
#     else:
#         return max(a,b)
# print(lesser_of_even(2,3))

# # takes a two-words string and return true if both words begin with same letter.
# def word_check(string):
#     string1 = string.lower().split()
#     if string1 [0][0] == string1[1][0]:
#         return True
#     else:
#         return False
# print(word_check("Hello Everyone"))


# # given 2 integers, return True if the sum of the integers is 20 or if one of the integers is 20. if not,return false.
# def sum_of_integers(a,b):
#     x=a+b
#     return [ True if x == 20 or a==20 or b==20 else False ]
# print(sum_of_integers(10,10))


# # write function that capitalize the first and fourth letter of a name
# def cap_of_word(word):
#     return word[0].upper()+ word[1:3] + word[3].upper() + word[4:]
# print(cap_of_word("hello"))

# def cap_of_word(word):
#     first_half=word[:3]
#     second_half=word[3:]
#     return first_half.capitalize() + second_half.capitalize()
# print(cap_of_word("abcd"))

# # revers the given sentence
# def reverse_sen(sentence):
#     sentence1 = sentence.split()
#     sentence2 = sentence1[::-1]
#     return ' '.join(sentence2)
# print(reverse_sen("Hi i'm root i i'm"))

# # given a list of ints, True if the array conatins 3 next ot a 3 somewhere.
# # array ([1,2,3,3])  # True   array1([1,2,3,4,3]) # False
# def has_33(nums):
#     for i in range(0,len(nums)-1):
#         if nums[i]==3 and nums[i+1]==3:
#             return True
#     return False
# print(has_33([1,2,3,3]))


# # given string , return a string where for every character in the original there are three characters

# def three_string(text):
#     for i in text:
#         print(i*3,end="")
    
# three_string("Hello Hi")



# def display(row1,row2,row3):
#     print(row1)
#     print(row2)
#     print(row3)
# row1=[1,2,3]
# row2=[4,5,6]
# row3=[7,8,9]
# row2[1]='X'
# display(row1,row3,row2)


