# #string
# s="hello"
# for i in s:
#     print(i)
#
# #list
# l=[1,2,3,4,]
# for i in l:
#     print(i)
#
# #tuple
# t=(1,2,3,4)
# for i in t:
#     print(i)
#
# #set
# s={1,2,3,4,5}
# for i in s:
#     print(i)
#
# #even numbers in set
# s={1,2,3,4,5}
# for i in s:
#     if i%2==0:
#      print(i)

#print each colors,colors=['red','green','blue']
# colors=['red','green','blue']
# for i in colors:
#     print(i)

#d={'a':10,'b':20,'c':30}
# d={'a':10,'b':20,'c':30}
# for i in d:
#     print(i)
   #or

# d={'a':10,'b':20,'c':30}
# for i in d:
#     print(i,":",d[i])

#print each number,t=(12,78,34,50)
# t=(12,78,34,50)
# for i in t:
#     print(i)

#print sum of numbers in list,l=[56,89,34,10]
# l=[56,89,34,10]
# s=0
# for i in l:
#     s+=i
# print(s)

#Range() method.
# for i in range(1,10):
#  print(i)
#
# for i in range(10,0,-2):
#     print(i)

#reverse
# s="hello"
# rev=" "
# for i in s:
#     rev=i+rev
# print(rev)
# if s==rev:
#     print("is palindrome")
# else:
#     print("is not palindrome")

#s=input("enter a string")
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)
# if s==rev:
#     print("is palindrome")
# else:
#     print("is not palindrome")

# n=1034
# rev=""
# s=str(n)
# for i in s:
#     rev=i+rev
# print(rev)


#l=[12,34,56,45,89,16,69,33]
# #print each number in a list
# for i in l:
#    print(i)

#print even values
# for i in l:
#    if i%2==0:
#      print(i)

#print those numbers that are divisible by 5.
# for i in l:
#   if i%5==0:
#     print(i)

#print those numbers that contains digit '3'
# for i in l:
#     if '3' in str(i):
#         print(i)
#     else:
#         print()

#sum of list
# s=0
# for i in l:
#     s+=i
# print(s)

#count of even numbers in a list
# count=0
# i=1
# for i in l:
#      count=count+1
# print(count)

#product of list
# p=1
# for i in l:
#     p=p*i
# print(p)

#print squares of each number
# for i in l:
#     i=i**2
#     print(i)

#l=[12,4.5,6.8,30,"arun","hello"]
#print only float point values
# for i in l:
#     if type(i)==float:
#         print(i)

#string values
# for i in l:
#  if type(i)=="str":
#     print(i)

#numbers
# for i in l:
#     if type(i)==int:
#         print(i)

#d={'a':23,'b':25,'c':28,'d':30,'e':22}
#even values
# for i in d.values():
#     if i%2==0:
#       print(i)

#colors=['red','green','blue','orange','black']
#starting letter
# for i in colors:
#       i=i[0]
#       print(i)

# #last letter
# for i in colors:
#      i=i[-1]
#      print(i)
#reverse
# for i in colors:
#      i=i[::-1]
#      print(i)

# s="hello"
# for i in s:
#     if i=='l':
#         break
#     print(i)

# s="hello"
# for i in s:
#     if i=='l':
#         continue
#     print(i)

# s="hello"
# for i in s:
#     if i=='l':
#         pass
#     print(i)

