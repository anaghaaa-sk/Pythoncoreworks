# #Q1.Define a function that takes 2 numbers and returns their product
# def product(n1,n2):
#     product=n1*n2
#     return product
#
# a=product(4,6)
# print(a)
#
#
# #Q2.Define a function that takes a string and returns number of vowels
# def vowels(s):
#     count = 0
#     v = "aeiouAEIOU"
#
#     for i in s:
#         if i in v:
#             count += 1
#
#     return count
#
# a = vowels("apple")
# print(a)
#
#
# #Q3.Define a function that takes length and breadth and returns area of rectangle
# def area(l,b):
#     area=l*b
#     return area
# a=area(6,6)
# print(a)
#
#
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
#
#
# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
# def sum(digits):
#     new=[]
#     for i in l:
#         sum = 0
#
#         for j in str(i):
#             sum=sum+int(j)
#         new.append(sum)
#     return new
# a=sum(l)
# print(a)
#
#
# #Q6.Define a function that takes a list and returns a new list containing unique elements from the given list
# l=[12,34,78,12,67,34,90,23]
# def unique(elements):
#     new=[]
#     for i in l:
#         if i not in new:
#             new.append(i)
#     return new
# a=unique(l)
# print(a)
#
#
# #Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# new=[]
# def common(list1,list2):
#     for i in list1 :
#         if i in list2:
#             new.append(i)
#     return new
# a=common(list1,list2)
# print(a)

#define a function that takes string as argument and return a new dictionary where keys are words and values are length of each word.call the function and print the dictionary.
# s="python coding is easy and fun"
# def dictionary(s):
#     new = {i: len(i) for i in s.split()}
#     return new
# a=dictionary(s)
# print(a)
#
#   #or
# s="python coding is easy and fun"
# def dictionary(s):
#     new={}
#     for i in s.split():
#         new[i]=len(i)
#     return new
# a=dictionary(s)
# print(a)

#1.positional argument
# def fun(n,a):
#     print("name",n)
#     print("age",a)
# fun("arun",23)
# fun(23,"arun")

#2keyword argument
# def fun(n,a):
#     print("name",n)
#     print("age",a)
# fun(n="arun",a=23)
# fun(a=23,n="arun")
#
# #default argument
# def fun(n,a=25):
#     print("name",n)
#     print("age",a)
# fun("arun",23)
# fun("arun")

#variable length/arbitary
#1(positional)
# def fun(a,b):
#     print(a,b)
# fun(10,20)
# fun(10,20,30)

#2(variable length positional)
# def fun(*args):
#     print(args)
# fun(10,20)
# fun(10,20,30)
#
# #3(variable length keyword)
# def fun(**kwargs):
#     print(kwargs)
# fun(a=10,b=20)
# fun(a=10,b=20,c=30)

#add
# def add(*args):
#      s=sum(args)
#      print(s)
# add(2,3)
# add(2,3,4)
# add(10,20,30,40,50)

#or
def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    print("Sum is",sum)

add(2, 3)
add(2, 3, 4)
add(10, 20, 30, 40, 50)


