#define a function to add two numbers
# def add():
#     "Addition of two Numbers"
#     n1=int(input("enter the first number"))
#     n2=int(input("enter the second number"))
#     s=n1+n2
#     print("Sum",s)
#     return
# add()
# #define a function to display "hello your name"
# def name():
#     "display your name"
#     n=input("Enter the name")
#     print("Hello",n)
#     return
# name()

#define a function to find the count of a specific character in a string
# def string():
#     "character in a string"
#     count=0
#     s=int(input("enter the string"))
#     ch=int(input("enter the character"))
#     for i in s:
#       if i==ch:
#           count+=1
#     print(count)
#     return
# string()


#define a function to find the factorial of a number

# def fact():
#     "factorial"
#     n=int(input("enter the number"))
#     f=1
#     for i in range(1,n+1):
#     f=f*i
#     print("factorial",f)
#     return
# fact()


#define a function to check whether a number is Armstrong or not
# def arm():
#     "find Armstrong"
#     n = int(input("enter the number"))
#     sum=0
#     s=str(n)
#     l=len(s)
#     for i in s:
#           sum=sum+int(i)**l
#
#     if sum==n:
#                print("Armstrong")
#     else:
#               print("Not Armstrong")
#
#     return
# arm()


#define a function to check whether a number is prime or not
# def prime():
#     "find prime or not"
#     num=int(input("enter a number:"))
#     if(num>1):#if number is greater than 1
#        for i in range(2,num):#[2,3,...num-1]
#           if(num%i==0):
#                 print("not prime")
#                 break
#        else:
#           print("prime")
#     else:#if num 1,0 or negative
#           print("number is neither prime or composite")
#           return
# prime()

#define a function to find the factors of a number
# def factor():
#     " find factors"
#     n=int(input("enter a number"))
#     for i in range(1,n+1):
#         if n%i==0:
#          print(i)
#     return
# factor()

# #sum using parameters and arguments
# def add(n1,n2):#parameters
#     sum=n1+n2
#     print("sum",sum)
# add(33,33)  #arguments
#define a function that takes 3 arguments and find the simple interset.
# def simple(p,y,r):
#     si = (p * y * r / 100)
#     print("simple interest", si)
#
# p=int(input("enter the principle amount:")
# y=int(input("enter the num of year:")
# r=int(input("enter the rate:")
# simple(p,y,r)

#define a function that takes string and characters as arguments and print the count.
# def count(s,ch):
#     count=0
#     for i in s:
#         if(ch==i):
#             count+=1
#         print("count",count)
# a=input("enter string")
# ch=input("enter character")
# count(a,ch)


#RETURN STATEMENT
# def add(n1,n2):
#     sum=n1+n2
#     return sum
# a=add(23,34)
# print(a)
#    #or
# def add(n1,n2):
#     sum=n1+n2
#     print("sum",sum)
#     return
# a=add(23,34)
# print(a)

#define a function that takes 3 numbers and return the product as results call the function and print result
def product(n1,n2,n3):
    product=n1*n2*n3
    return product

a=product(1,2,3)
print(a)