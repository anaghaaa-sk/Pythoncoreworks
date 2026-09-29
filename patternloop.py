# for i in range(1,4):
#  for j in range(1,5):
#     print('*',end=" ")
# print()


# for i in range(1,7):
#        for j in range(1,i+1):
#             print('*',end=" ")
#        print()

# 1
# for i in range(2,10,2):
#        for j in range(2,10,2):
#             print(i,end=" ")
#        print()

# 2


# 3
# for i in range(5,0,-1):
#       for j in range(1,i+1):
#             print('*',end=" ")
#       print()

# 4
# for i in range(1,5):
#        for j in range(1,5):
#             print(i,end=" ")
#        print()

# 5
# for i in range(1,5):
#        for j in range(1,5):
#           if(i==j):
#              print(i,end=" ")
#           else:
#              print(0,end=" ")
#        print()

# 6
# for i in range(1,5):
#        for j in range(1,i+1):
#           if(j%2==0):
#              print(0,end=" ")
#           else:
#              print(1,end=" ")
#        print()


# 7
# k=1
# for i in range(1,5):
#       for j in range(1,i+1):
#             print(k,end=" ")
#             k=k+1
#       print()


# squares
# k=1
# for i in range(1,5):
#       for j in range(1,i+1):
#             print(k**2,end=" ")
#             k=k+1
#       print()

# number pattern
# k=1
# for i in range(1,5):
#       for j in range(1,i+1):
#             print(k,end=" ")
#             k=k+2
#       print()


# alphabet ptrn
# k=ord('A')
# for i in range(1,5):
#       for j in range(1,i+1):
#             print(chr(k),end=" ")
#             k=k+1
#       print()


# k=ord('A')
# for i in range(1,5):
#       for j in range(1,i+1):
#             print(chr(k),end=" ")
#       k=k+1
#       print()


# for i in range(1,5):
#       k = ord('A')
#       for j in range(1,i+1):
#               print(chr(k),end=" ")
#               k=k+1
#       print()


#l = [23, 65, 42, 80, 56, 41]
# for i in l:
#     if i%2==0:
#         print(i)


# for i in l:
#    for j in range(2,i):#[2,3,...num-1]
#       if(i%j==0):
#            # print("not prime")
#             break
# else:
#       print(i)

#
# for i in range(1,101):
#     if i>1:
#      for j in range(2,i):
#       if(i%j==0):
#            break
# else:
#       print(i)

# print all armstrong numbers in the range(100,1000)
#
# for i in range(100,1001):
#     s=str(i)
#     l=len(s)
#     sum=0
#     for j in s:
#         sum = sum + int(j) ** l
#     if sum==i:
#            print(i)

# # space pattern
# k = 4 * 2
# for i in range(1,6):
#     for p in range(1,k+1):
#          print(end=" ")
#     for j in range(1,i+1):
#          print('*',end="   ")
#     k=k-2
#     print()


#1
# k=3*2
# for i in range(1,5):  #rows
#
#     for p in range(1,k+1): #space loop
#         print(end='')
#
#     for j in range(1,i+1):  #star loop
#          print('*',end='   ')
#     k=k-2
#     print()
#
# k=3*2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#        print(end='')
#
#
#     for j in range(1,i+1):
#          print('*',end='   ')
#     k=k-2
#     print()
#
#
#
# #2
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
#
# #3
# k=3*2
# for i in range(1,5):
#      #Code for spacing
#      for p in range(1,k+1):
#          print(end=' ')
#
#
#      #for printing stars
#      for j in range(1,i+1):
#           print('*',end='   ')
#      k=k-2
#      print()
#
#
# k=1
# for i in range(3,0,-1):
#      #Code for spacing
#      for p in range(1,k+1):
#          print(end='  ')
#
#
#      #for printing stars
#      for j in range(1,i+1):
#           print('*',end='   ')
#      k=k+1
#      print()

#4
 # E
 # DD
 # CCC
 # BBBB
 # AAAAA

# k=ord('E')
# for i in range(1,5):
#       for j in range(1,i+1):
#             print(chr(k),end=" ")
#       k=k-1
#       print()




# k=3*2
# for i in range(1,5):
#     for j in range(i,0,-1):
#             print(j,end=" ")
#     print()



# k=5
# for i in range(1,6):
#     for j in range(1,i+1):
#             print(k,end=" ")
#     k=k-1
#     print()