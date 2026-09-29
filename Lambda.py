#define a function that takes a number as argument and returns its square
# def fun():
#     n=int(input("enter the number:"))
#     s=n**2
#     print(s)
#     return
# fun()
# #or
# def square(n):
#     return n*n
# a=square(5)
# print(a)
#by using lambda
s=lambda n:n**2
print(s(5))

#define a lambda function to find the cube of a number
s=lambda n:n**3
print(s(5))

#sum of 2 numbers
s= lambda a,b:a+b
print(s(2,3))

#product of 3 numbers
s=lambda a,b,c:a*b*c
print(s(1,2,3))

#length of a string
s=lambda n:len(n)
print(s("hello"))

#square root of a
s=lambda a,b:a**0.5
print(s(2,3))

#first letter of a string
s=lambda n:n[0]
print(s("red"))

#last letter of a string
s=lambda n:n[-1]
print(s("red"))

#name value from dictionary
s=lambda a:a.get('name')
d={'name':'arun','age':26,'salary':10000}
print(s(d))

#salary value from dictionary
s=lambda a:a.get('salary')
d={'name':'arun','age':26,'salary':10000}
print(s(d))

#add 10 to a number
s=lambda n:n+10
print(s(56))

#MAP
l=[1,2,3,4]
#create a new list of squares
#map(function,sequence)
print(list(map(lambda x:x**2,l)))
print(set(map(lambda x:x**2,l)))
print(tuple(map(lambda x:x**2,l)))

#create a new list of cubes.
print(list(map(lambda x:x**3,l)))

#create  a new list of square roots.
l=[25,36,81,100]
print(list(map(lambda x:x**0.5,l)))

#create a new list of lengths.
colors=['red','green','blue','yellow','black']


#create a new list of lengths
print(list(map(lambda x:len(x),colors)))

#create a new list of first characters
print(list(map(lambda x:x[0],colors)))

#create a new list of last characters
print(list(map(lambda x:x[-1],colors)))

#create a new list of reverse of each element
print(list(map(lambda x:x[::-1],colors)))

        ##################################

#Given a list
l=[23,78,12,56]

#Add 10 to each element in the given sequence
print(list(map(lambda x:x+10,l)))

               ############################################

##given a list of dictionaries
l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
   {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
   {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
#
# # create a new list of emails

print(list(map(lambda x: x['email'], l)))



    ###########################################

####  filter
l=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x%2==0,l)))


#Given list
l=[23,65,89,12,20,33,85,40]

# filter elements grater than 50
print(list(filter(lambda x: x > 50, l)))


#filter even values less than 50
print(list(filter(lambda x: x < 50 and x % 2 == 0, l)))

        ############################
#Given a list
fruits=["apple","orange","pinapple","grapes","avagado"]

#filter elements whose length is greater than 5
print(list(filter(lambda x: len(x) > 5, fruits)))




                 #############################

#### reduce()
#sum of a list
l=[1,2,3,4]
import functools
print(functools.reduce(lambda a,b:a+b,l,0)) # 0 is optional

#product of a list
l=[1,2,3,4]
import functools
print(functools.reduce(lambda a,b:a*b,l,1)) # 1 is optional

        #####################################

