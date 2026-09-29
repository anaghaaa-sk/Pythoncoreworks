
#write a program to calculate electricity bill based on the following criteria.
#units consumed          Rates per unit
#<=100 units                0
#100-200 unit             5 RS/unit
#200-300 unit             10 RS/unit
#Above 300 unit           15 RS/unit

#325 unit
#100-0
#100*5
#100*10
#25*15
#125

# unit=int(input("Enter the number of units consumed"))
# if unit<=100:
#     bill=0
#     print("Bill is",bill)
# elif unit>100 and unit<=200:
#     bill=0+(unit-100)*5
#     print("Bill is", bill)
# elif unit>200 and unit<=300:
#     bill=0+500+(unit-200)*10
#     print("Bill is", bill)
# else:
#     bill=0+500+1000+(unit-300)*15
#     print("Bill is", bill)

#write a program to check whether the user entered number is 2 digit/3digit/4 digit number.
# n=int(input("enter the number"))
# if n>9 and n<100:
#     print(f"{n} is 2 digit")
# elif n>99 and n<1000:
#     print(f"{n} is 3 digit")
# elif n > 999 and n <10000:
#     print(f"{n} is 4 digit")
# else:
#     print(f"{n} is greater than 4 digit")
    #or
#a=input('Enter a number') #input text directly into a number using int(),  a number object has no length property
# if len(a)==2:
#      print(f"{a} is 2 digit")
# elif len(a)==3:
#      print(f"{a} is 3 digit")
# else:
#     print(f"{a} is 4 digit")

#write a basic calculator program to perform arithmetic operations.
#(+,-,*,/,%,//)
# num1=int(input("enter the first number"))
# num2=int(input("enter the second number"))
# op=input("enter the operation")
# if op=='+':
#     print("Answer is",num1+num2)
# elif op=='-':
#     print("Answer is", num1-num2)
# elif op=='*':
#     print("Answer is", num1-num2)
# elif op=='/':
#     print("Answer is", num1/num2)
# elif op=='%':
#     print("Answer is", num1%num2)
# elif op=='//':
#     print("Answer is", num1//num2)
# else:
#     print("error")

#write a program to print the number of days in a month.
# month=input("enter the month")
# l1=['januay','march','may','july','august','october','december']
# l2=['april','june','september','november']
# l3=['february']
# if month in l1:
#     print(f"{month} has 31 days")
# elif month in l2:
#     print(f"{month} has 30 days")
# else:
#     print(f"{month} has 28/29 days")

#write a program to print the grades based on the following criteria.
# 91-100      grade A
# 81-90       grade B
# 71-80       grade C
# 61-70       grade D
# below 61    grade E

n=int(input('Percentage obtained'))
if 91<=n<=100:
    print('Grade A')
elif 81<=n<=90:
    print('Grade B')
elif 71<=n<=80:
    print('Grade C')
elif 61<=n<=70:
    print('Grade D')
else:
    print('Grade E')


