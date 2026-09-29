#FUNCTION
#Addition of two numbers.
# def add():
#     n1=int(input("Enter the first number:"))
#     n2=int(input("Enter the second number:"))
#     sum=n1+n2
#     print("Sum is",sum)
#     return
# add()

#define a function to find the count of a specific character in a string.
# def string():
#     count=0
#     s=input("enter the string:")
#     ch=input("enter the character:")
#     for i in s:
#      if i==ch:
#         count+=1
#     return count
# a=string()
# print(a)


# #define a function to find the factorial of a number.
# def fact():
#     num=int(input("enter the number:"))
#     f=1
#     for i in range(1,num+1):
#         f=f*i
#     return f
# a=fact()
# print(a)

#define a function to check whether a number is Armstrong or not
# def arm():
#     n=int(input("enter the number:"))
#     sum=0
#     s=str(n)
#     l=len(s)
#     for i in s:
#         sum=sum+int(i)**l
#     if sum==n:
#        print("armstrong")
#     else:
#         print("not armstrong")
# arm()

#define a function to check whether a number is prime or not
# def prime():
#     num=int(input("enter the number:"))
#     for i in range(2,num):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#             print("prime")
#     return
# prime()

#Q1.Define a function that takes 2 numbers and returns their product.
# def product(n1,n2):
#     product=n1*n2
#     return product
# a=product(6,6)
# print(a)

# #Q2.Define a function that takes a string and returns number of vowels
# def string(s):
#     count=0
#     v="aeiouAEIOU"
#     for i in s:
#      if i in v:
#         count+=1
#     return count
# a=string("apple")
# print(a)

# #Q3.Define a function that takes length and breadth and returns area of rectangle
# def area(l,b):
#     area=l*b
#     return area
# a=area(4,4)
# print(a)


# #Q4.Define a function that takes a list of numbers and creates a new list with even numbers and returns the new list
# l=[45,78,90,12,35]
# def even(l):
#     new=[]
#     for i in l:
#         if i%2==0:
#             new.append(i)
#     return new
# a=even(l)
# print(a)

#Q5.Define a function that takes list of 3 digit numbers and returns a new list where each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
# def sum(digits):
#     new=[]
#     for i in l:
#          sum=0
#          for j in str(i):
#            sum=sum+int(j)
#          new.append(sum)
#     return new
# a=sum(l)
# print(a)


# #Q6.Define a function that takes a list and returns a new list containing unique elements from the given list
# l=[12,34,78,12,67,34,90,23]
# def unique(elements):
#     new=[]
#     for i in l:
#       if i not in new:
#           new.append(i)
#     return new
# a=unique(l)
# print(a)

# #Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# def common(list1,list2):
#     new=[]
#     for i in list1:
#         if i in list2:
#             new.append(i)
#     return new
# a=common(list1,list2)
# print(a)


#1Given a string
# s="I am learning Python"

# find the length of the string
# def length(s):
#     return len(s)
# a=length(s)
# print(a)
#
# # find the reverse of the string
# def length(s):
#     return s[::-1]
# a=length(s)
# print(a)
#
# # find the last character of the strings
# def length(s):
#     return s[-1]
# a=length(s)
# print(a)


#6given a set
# s={10,20,30,40}
# #Add a new number 50 to the set
# def number(s):
#     s.add(50)
#     return s
# a=number(s)
# print(a)

#write a program to check whether the entered numbers are equal or not.
# def equal(n1,n2):
#     if n1==n2:
#      return "equal"
#     else:
#         return "not equal"
# a=equal(6,4)
# print(a)

#write a program to find the maximum of two numbers.
# def maximum(n1,n2):
#     if n1>n2:
#         return "n1 is greater"
#     else:
#         return "n2 is greater"
# a=maximum(6,7)
# print(a)

#write a program to find the greatest of 3 numbers.
# def greatest(n1,n2,n3):
#     if n1>n2 and n1>n3:
#         return "n1 is greatest"
#     elif n2>n1 and n2>n3:
#         return "n2 is greatest"
#     else:
#         return "n3 is greatest"
# a=greatest(9,5,6)
# print(a)

#write a program to check whether the entered string is palindrome or not.
# def palindrome(s):
#     if s==s[::-1]:
#         return "palindrome"
#     else:
#         return "not palindrome"
# a=palindrome("anagha")
# print(a)

# 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5
# def divisible():
#     for i in range(1,101):
#         if i%3==0 or i%5==0:
#             print(i)
#     return
# divisible()

#reverse
# def reverse(n1):
#     rev=""
#     for i in n1:
#         rev=i+rev
#     return rev
# a=reverse('987')
# print(a)

# multiplication table
# def multiplication():
#     n=2
#     for i in range(1,11):
#         p=i*n
#         i+=1
#         print(p)
#     return
# multiplication()

#LAMBDA FUNCTION

# # 3.Filter out all empty strings from a list
# words = ['hello', ' ', 'world', ' ', 'python']
# print(list(filter(lambda x:x.isspace(),words)))
# print(list(filter(lambda x:x.strip(),words)))

#
# n=6
# i=1
# f=1
# while i<=n:
#     f=f*i
#     i=i+1
# print(f)


# n=10
# i=1
# while i<=10:
#     print(f"{i} * {n} = ",i*n)
#     i+=1



# n=2
# i=1
# if n>1:
#  for i in range(2,n):
#       if n%i==0:
#
#           print("not prime")
#           break
#       else:
#           print("prime")
# else:
#     print("neither prime or composite")


n=1234
# print(n)
s=str(n)
# print(int(len(s)))
sum=0
for i in s:
   sum+=1
   print(sum)






