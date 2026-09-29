# x = "10"
# y = "20"
#
# print(x + y)  #1020
#
# x = 10
# y = 20
#
# print(x + y)  #30
#
# # x = "10"
# # y = 20
# #
# # print(x + y)  #error
#
# x = 10
# y = 2.5
#
# print(x + y)
# print(type(x + y))   #12.5-float
#
# x = [1, 2, 3]
# y = [4, 5]
#
# print(x + y)   #[1,2,3,4,5]
#
# x = "Python"
# print(x * 3)   #pythonpythonpython
#
# x = True
# y = False
#
# print(type(x))   #bool
# print(type(y))   #bool
#
#
# x = {1, 2, 3, 3, 2}
#
# print(x)   #{1,2,3}


# positive or negative
# num=0
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")


#largest of two numbers
# num1=7
# num2=10
# if num1>num2:
#     print("num1 is greatest")
# else:
#     print("num2 is greatest")


# Question: Calculate the electricity bill based on units:
#
# 0–100 units     → ₹5 per unit
# 101–200 units   → ₹7 per unit
# 201–300 units   → ₹10 per unit
# Above 300       → ₹15 per unit
#
# unit=int(input("enter the unit"))
# if unit<=100:
#     bill=unit*5
#
# elif unit>100 and unit<200:
#     bill=unit*7
#
# elif unit>200 and unit<300:
#     bill=unit*10
#
# else:
#     bill=unit*15
#
# print("electricity bill is ",bill)


# vowels
# ch=input("enter the character:")
# if ch in "aeiouAEIOU":
#     print("vowels")
# elif ch>="0" and ch<="9":
#     print("digit")
# else:
#     print("consonant")


#Loop
#for Loop
# for i in range(1,6):
#     print(i)
# for i in range(5):
#     print(i)
# for i in range(1,10,2):
#     print(i)
# for i in range(2,10,2):
#     print(i)
# for i in range(10,0,-1):
#     print(i)
# for i in range(10,1,-2):
#     print(i)

#in string
# name="python"
# for i in name:
#     print(i)

#in list
#
# l=[1,2,3,4]
# for i in l:
#     print(i)

#while Loop
# i=0
# while i<5:
#     print(i)
#     i+=1

# break
# for i in range(1,10):
#     if i==5:
#         break
#         print(i)

# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)


#even
# for i in range(1,10):
#     if i%2==0:
#         print(i)

#odd
# for i in range(1,10):
#     if i%2!=0:
#         print(i)

# num=int(input("enter the number:"))
# for i in range(1,20):
#     print(num,'*',i,'=',num*i)

# for i in range (1,10):
#     if i==5:
#      print(i)



#
# s = "python is a programming language"
# vowels='aeiouAEIOU'
# count_v=0
# count_c=0
# for i in s:
#     if i in vowels:
#         count_v+=1
#     elif i.isalpha():
#         count_c+=1
# print('count of vowels',count_v)
# print('count of consonants',count_c)

#Define a function that takes a list as an argument and returns the largest odd number in the list.
# l= [12, 7, 18, 25, 10, 13]
# def large_odd(l):
#     largest=0
#     for i in l:
#         if i%2!=0:
#             if i>largest:
#                 largest=i
#     return largest
# l= [12, 7, 18, 25, 10, 13]
# a=large_odd(l)
# print(a)

#Write a program to find the sum of all digits present in a string.
# s="abc123de45"
# sum=0
# for i in s:
#     if i.isdigit():
#         sum=sum+int(i)
# print(sum)

#Write a program to count the number of uppercase letters, lowercase letters, and digits in a string
# l="PyThon123"
# count_u=0
# count_lower=0
# count_d=0
# for i in l:
#     if i.isupper():
#         count_u+=1
#     elif i.islower():
#         count_lower+=1
#     elif i.isdigit():
#         count_d+=1
# print('count of uppercase',count_u)
# print('count of lower',count_lower)
# print('count of digits',count_d)

#Write a program to find the sum of all numbers in a list that are greater than 10.
# l=[5, 12, 8, 20, 15, 3]
# sum=0
# for i in l:
#     if i>10:
#         sum=sum+i
# print(sum)
#
#
# s='python 123'
# vowels='aeiouAEIOU'
# count_v=0
# count_c=0
# count_d=0
# count_s=0
# for i in s:
#     if i in vowels:
#         count_v+=1
#     elif i.isalpha():
#         count_c+=1
#     elif i.isdigit():
#         count_d+=1
#     elif i.isspace():
#         count_s+=1
# print()


#
# l=[5, 12, 8, 20, 15, 3]
# sum=0
# for i in l:
#     if i>10:
#         sum=sum+i
# print(sum)
#
#
#
#
#
# l=[5, 12, 8, 20, 15, 3]
# count=0
# for i in l:
#         count+=i
# print(count)


#PATTERNS
#1.SQUARE
# for i in range(4):
#     for j in range(4):
#         print('*',end=" ")
#     print()

#2.increasing triangle
# for i in range(1,5):
#     for j in range(i):
#         print('*',end=" ")
#     print()

#3.increasing Number pattern
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#4.same number pattern
# for i in range(1,5):
#     for j in range(i):
#         print(i,end=" ")
#     print()

#5.Reverse triangle pattern
# for i in range(4,0,-1):
#     for j in range(i):
#         print('*',end=" ")
#     print()

#6.reverse number pattern
# for i in range(4,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

#7.continuos number triangle pattern
# n=1
# for i in range(1,5):
#     for j in range(i):
#         print(n,end=" ")
#         n+=1
#     print()

#8.space pattern (triangle)
# k=4*2
# for i in range(1,6):
#      for p in range(1,k+1):
#         print(end=" ")
#      for j in range(1,2*i):
#         print('*',end=" ")
#      k=k-2
#      print()

#9.diamond
k=3*2
for i in range(1,5):
     #Code for spacing
     for p in range(1,k+1):
         print(end=' ')


     #for printing stars
     for j in range(1,i+1):
          print('*',end='   ')
     k=k-2
     print()


k=1
for i in range(3,0,-1):
     #Code for spacing
     for p in range(1,k+1):
         print(end='  ')


     #for printing stars
     for j in range(1,i+1):
          print('*',end='   ')
     k=k+1
     print()
#10.
k=3*2
for i in range(1,5):  #rows

    for p in range(1,k+1): #space loop
        print(end='')

    for j in range(1,i+1):  #star loop
         print('*',end='   ')
    k=k-2
    print()

k=3*2
for i in range(3,0,-1):
    for p in range(1,k+1):
       print(end='')


    for j in range(1,i+1):
         print('*',end='   ')
    k=k-2
    print()
#11.
k=3*2
for i in range(1,5):
     #Code for spacing
     for p in range(1,k+1):
         print(end=' ')


     #for printing stars
     for j in range(1,i+1):
          print('*',end=' ')
     k=k-2
     print()


k=2
for i in range(3,0,-1):

    for p in range(1,k+1):
          print(end=' ')

    for j in range(1,i+1):
         print('*',end=' ')
    k=k+2
    print()




