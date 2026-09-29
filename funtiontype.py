# #write a program to find the position of a specific character in a string.
# s="hello world"
# ch='l'
# if ch in s:
#  print("The position of",ch,"is",s.index(ch))
#
# #write a program to find the count of a specific character in a string.
# s="hello world"
# ch='l'
# print("The count of specific character",ch,"is",s.count(ch))
#
# #write a program to create a new dictionary where keys are letters and values are the count of each letter.
# s="hello world"
# new={}
# for i in s:
#     new[i]=s.count(i)
# print(new)
#
#
# # write a program to create a  new list with 5 random 3 digit numbers.
# import random
# new=[]
# for i in range(5):
#     num=random.randint(100,1000)
#     new.append(num)
# print(new)
#
#
# # write a program to create a 5 digit otp number.
# print(random.randint(10000,99999))
#
# #write a program to find the count of letters,spaces and digits in a string.
# s="hello world"
# count_l=0
# count_d=0
# count_s=0
# for i in s:
#     if i.isalpha():
#         count_l+=1
#     elif i.isspace():
#         count_s+=1
#     elif i.isdigit():
#         count_d+=1
#     print("letter count is",count_l)
#     print("space count is",count_s)
#     print("digit count is",count_d)



#given a list
# l=[1,1,2,3,4,5,5,5,6,7]
# # create a new dictionary where keys are numbers and value are count of each number.
# new={}
# for i in l:
#     new[i]=l.count(i)
# print(new)

#given a list
# l=[34,12,56,89,90,11]
# find the largest element.
# print("largest is",max(l))
# # find the second largest element.
# #find the largest element
# a=max(l)
# print(a)

#find the second largest element
# largest=l.copy()
# largest.remove(a)
# second_largest=max(largest)
# print(second_largest)
# print("largest is",l.sort())
 #or
#
# print("maximum",max(l))
# print("minimum",min(l))
# l.sort()
# print("sorted",l)
# print("second largest",l[-2])


# find the smallest element.
# print("largest is",min(l))
# find the second smallest element.
# l.sort()
# print("sorted",l)
# print("second smallest",l[1])

# l=[
#     ["arun",23,40000],
#     ["amal",24,50000],
#     ["anu",27,30000]
#    ]

#create  a new list of salary
# new=[i[2] for i in l]
# print(new)
#find the maximum salary
# max(l)
# print(l)
# new=[max(l) for i in l]
# print(new)
# create a new list ages
# new=[i[1] for i in l]
# print(new)

#find the minimum salary
# min(l)
# print(l)

#
# # Given a list
# l=[1,1,1,2,3,3,4,5]
#
# # remove duplicates from list
# l=list(set(l))
# print(l)
#
#
# # 2.Given a list
# l=[1,1,1,2,3,3,4,5]
#
# #remove duplicates without set()
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)
#
#
# # 3.Given two lists
#
# l1=[23,45,78,90,12,74]
# l2=[45,89,23,56,34]

# print common elelments
# new=[]
# for i in l1:
#     if i in l2:
#         new.append(i)
# print(new)

#or
# s1=set(l1)
# s2=set(l2)
# print("common elements",s1.intersection(s2))

#define a function that takes a list of numbers as arguments and print the count of even numbers,odd numbers and numbers whose value greater than 50.
l=[23,56,12,78,98,89,31,67]
def count_num(l):
    odd=0
    even=0
    greater50=0
    for i in l:
        if(i%2==0):
            even+=1

        else:
            odd+=1
        if(i>50):
            greater50+=1

    print("ODD",odd)
    print("EVEN",even)
    print("GREATER50",greater50)
count_num(l)

#define a function that takes a list of words as argument and returns a new list of lengths.
l=["red","green","orange","yellow","blue"]
def length(l):
    new=[]
    for i in l:
        new.append(len(i))
    return new
r=length(l)
print(r)




































