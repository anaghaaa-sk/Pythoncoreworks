#1.reverse a string using for loop
s='python'
rev=""
for i in s:
    rev=i+rev
print(rev)

#2.print 1-10 using for loop
for i in range(1,11):
    print(i)

#3.print 10-1
for i in range(10,0,-1):
    print(i)

#4.even num from 1-20
for i in range(2,21,2):
    print(i)

#5.multiples of 5 from 5-50
for i in range(5,51,5):
    print(i)

#6.print a word 5 times
s='Hiii'
print(s.split()*5)

for i in range(5):
    print('Hello')

#7.print each character on seperate line
s="python"
for i in s:
    print(i)

#8.sum from 1-10
sum=0
for i in range(1,11):
    sum+=i
print(sum)

#9.sum of even num from 1-20
sum=0
for i in range(2,21,2):
    sum+=i
    print(sum)

#10.multiplication table
n=6
for i in range(1,11):
    print(f"{n} * {i}={n*i}")

#11.count numbers from 1-100 that are divisible by 10
count=0
for i in range(1,101):
    if i%10==0:
        count+=1
print(count)

#12.count characters
s="python"
count=0
for i in s:
    count+=1
print(count)


#13.count vowels
s="python"
vowels="aeiouAEIOU"
count=0
for i in s:
    if i in vowels:
        count+=1
print(count)


#14.print numbers from 1-10 but stop when num reaches 5
for i in range(1,11):
    if i==5:
        break
    print(i)

#15.find num,if num reach 30 stop
num=[10,20,30,40,50]
for i in num:
    if i==30:
        break
    print(i)
