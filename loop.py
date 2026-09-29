#write a program to print first 10 integers.
# i=1  #var for looping is i. starting from 1
# while i<=10: # upto 10
#    # print(i)
#     print(i,end=" ") # to print integers horizontally
#     i+=1
#write a program to print first 10 even numbers.
#
# i=2
# while i<=20:
#    print(i,end=", ")
#    i+=2
# #write a program to print first 10 even numbers.
# i=1
# while i<=19:
#    print(i,end=", ")
#    i+=2

#
# i=1
# while i<=16:
#     print(i,end=", ")
#     i+=3

# i=10
# while i<=80:
#     print(i,end=", ")
#     i+=10

#3,6,9,12,15,18,21
# i=3
# while i<=21:
#     print(i,end=", ")
#     i+=3

#5,4,3,2,1
# i=5
# while i>=1:
#     print(i,end=", ")
#     i-=1

#8,6,4,2,0
# i=8
# while i>=0:
#     print(i,end=", ")
#     i-=2

#100,101,...200
# i=100
# while i<=200:
#     print(i,end=", ")
#     i+=1

#print all 4 digit numbers.
# i=1000
# while i<=9999:
#     print(i,end=",")
#     i+=1

#print those 3 digit numbers that are divisible by 3.
# i=100
# while i<=999:
#     if i%3==0:
#         print(i,end=",")
#     i+=1

#print those 4 digit numbers that contains digit '3'(#in operator sequence)
# i=1000
# while i<=9999:
#     s=str(i)
#     if '3' in s:
#         print(s, end=",")
#     i=i+1

#print those numbers that are divisible by 3 and 5in the range (1,100).
# i=1
# while i<=100:
#     if i%3==0 and i%5==0:
#         print(i, end=",")
#     i+=1

# i=1
# while i<=10:
#     print((i**2), end=", ")
#     i+=1


# i=100
# while i<=999:
#      s=str(i)
#      if '3' in s:
#          print(s, end=",")


#count of those 3 digit numbers that contains digit '3'.
# count=0
# i=100
# while i<=999:
#     s=str(i)
#     if '3' in s:
#         count=count+1
#     i+=1
# print(count)

#count of those numbers that are divisible by 7 or 3 in the range (200,300).
# count=0
# i=200
# while i<=300:
#      if i%7==0 or i%3==0:
#          count=count+1
#      i+=1
# print(count)

#count of odd numbers that are divisible by 5 in the range(1,100).
# count=0
# i=1
# while i<=100:
#      if i%5==0 and i%2!=0:
#          count=count+1
#      i+=1
# print(count)

#count of all palindrome numbers in the range(1,1000).
# count=0
# i=1
# while i<=1000:
#     s=str(i)
#     if(s==s[::-1]):
#         count=count+1
#     i+=1
# print(count)


#count of numbers divisible by 3 in the range of (1,50).
# count=0
# i=1
# while i<=50:
#      if i%3==0:
#          count=count+1
#      i+=1
# print(count)


#sum
#find the sum of first five numbers.
# s=0
# i=1
# while i<=5:
#     s+=i
#     i+=1
# print(s)


#sum of tose numbers that are divisible by 3 in the range(1,50).
# s=0
# i=1
# while i<=50:
#       if i%3==0:
#           s+=i
#       i+=1
# print(s)

#sum of all 3 digit numbers.
# s=0
# i=100
# while i<=999:
#     s+=i
#     i+=1
# print(s)

#sum of first 10 even numbers #(2,,4,6,8,10,12,14,16,18,20)
# s=0
# i=2
# while i<=20:
#     s+=i
#     i+=2
#print(s)

#product
#product of series 1,2,3,4,5.
# product=1
# i=1
# while i<=5:
#     product=product*i
#     i+=1
# print(product)

#product of first 10 odd numbers .
# product=1
# i=1
# while i<=19:
#     product=product*i
#     i+=2
# print(product)

#product of numbers that contains digit '3' in the range (1,50).
# product=1
# i=1
# while i<=50:
#     s=str(i)
#     if '3' in s:
#       product=product*i
#     i+=1
# print(product)

#factorial of a number entered by user.
# n=int(input("Enter the number:"))
# fact=1
# i=1
# while i<=n:
#     fact=fact*i
#     i=i+1
# print(fact)

#multiplication table of a number (upto 10).
n=int(input("Enter the number to print table:"))
i=1
while i<=10:
    #p=p*i
    print(f"{i}  *  {n}  =  {i*n}")
    i=i+1

#sum of digit.
# n=int(input("enter number"))
# s=0
# while n>0:
#     d=n%10
#     s=s+d
#     n=n//10
#
# print(s)