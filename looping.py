# #print all 3 digit numbers using while loop.
# i=100
# while i<=999:
#     print(i,end=" ")
#     i=i+1
#
# #using for loop
# for i in range (100,1000):
#     print(i)

#given a list of colors
# colors=['red','green','blue','orange','yellow','black']
#print each color
# for i in colors:
#     print(i)

#colors contains letter b.
# for i in colors:
#     if 'b' in i:
#      print(i)

# for i in colors:
#      i=i[0]
#      print(i)


# for i in colors:
#      i=i[-1]
#      print(i)

# for i in colors:
#     if(i[0]=="b"):
#         print(i)
#           break
#
#
# for i in colors:
#     if(i[0]=="b"):
#         print(i)
#           continue


#given a list
#l=[23,45,12,78,90,51,75]
#print all numbers
# for i in l:
#     print(i)

#even numbers
# for i in l:
#     if i%2==0:
#      print(i)
#divisible by 5
# for i in l:
#     if i%5==0:
#      print(i)
#stops the loop if i>50
# for i in l:
#     if i>50:
#         break
#     print(i)

#skip all even numbers
# for i in l:
#     if i%2==0:
#         continue
#     print(i)



 #print the first even number if i>50
# for i in l:
#      if i%2==0 and i>50:
#       print(i)
#       break

#count of all even numbers
#count=0
#i=1
# for i in l:
#     if(i%2==0):
#       count+=1
#  print("Count",count)


#sum of list
# sum=0
# for i in l:
#     sum=sum+i
# print("Sum",sum)

#product
# p=1
# for i in l:
#     if(i%2!=0):
#      p=p*i
# print(p)

#print each digit in a number
# n=1234
# s=str(n)
# for i in s:
#     print(i)

#sum of digits in a number
# n=1234
# s=str(n)
# sum=0
# for i in s:
#      sum=sum+int(i)
# print(sum)

#factors of a number
# n=int(input("enter a number"))
# for i in range(1,n+1):
#     if n%i==0:
#      print(i)

#l=[1,2,3,4]
# #new list
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)

# #new set
# new=set()
# for i in l:
#     new.add(i**2)
# print(new)

#new dictionary
# new={}
# for i in l:
#     new[i]=i**2
# print(new)

# n=1234
# s=str(n)
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)
#
# l=[1,2,3,4]
# sum=0
# new=[]
# for i in l:
#     sum=sum+i
#     new.append(sum)
# print(new)
#
# a=3
# b=7
# sum=0
# for i in range(a,a)

#
# l=[10,20,30,40,50]
# sum=0
# for i in range(0,5,2):# for i in range(0,len(l),2)
#       sum=sum+l[i]
# print(sum)


#write a program to check whether a number is amstrong number.
# n=int(input("enter the number"))
# sum=0
# s=str(n)
# l=len(s)
# for i in s:
#       sum=sum+int(i)**l
#
# if sum==n:
#            print("Armstrong")
# else:
#           print("Not Armstrong")


#for--else

# n=1,2,3,4,5
# for i in range(1,6):
#       print(i)
# else:
#       print("Hello")



# n=1,2,3,4,5
# for i in range(1,6):
#       if(i==4):
#             break
#       print(i)
# else:
#       print("Hello")
#
#
# n=1,2,3,4,5
# for i in range(1,6):
#       if(i==4):
#             continue
#       print(i)
# else:
#       print("Hello")


#check whether a number is prime or not.
#using for--else
# num=int(input("enter a number"))
# if(num>1):#if number is greater than 1
#    for i in range(2,num):#[2,3,...num-1]
#       if(num%i==0):
#             print("not prime")
#             break
#    else:
#       print("prime")
# else:#if num 1,0 or negative
#       print("number is neither prime or composite")

#nested looping
# l=[10,20,30,40,50,60]
# for i in l:
#       for j in range(1,7):
#             print(i,end=" ")
#       print()
#



# for i in range(1,4):
#       for j in range(1,4):
#            print(i,end=" ")
#       print()

#
# for i in range(1,4):
#       for j in range(1,4):
#            print(j,end=" ")
#       print()


# l=[['lion','tiger'],['cat','elephant']]
# for i in l:
#       print("outer loop iteration",i)
#       for j in i:
#             print(j,end=" ")
#       print()

#1
# n=['kelly','alan','jenny']
# #print the pattern
# for i in n:
#       for j in range(1,4):
#             print(i, end=" ")
#       print()

#2
# n=[1,2,3]
# qns=['what','when','why']
# for i in n:
#       print(i)
#       for j in qns:
#             print(j, end=" ")
#       print()

#3
# d=[{'id':101,'name':'arun','age':25},{'id':102,'name':'amal','age':23},{'id':103,'name':'anu','age':24}]
# for i in d:
#     print(i)
#     for j in i.values():
#         print(j,end=" ")
#     print()

#


















