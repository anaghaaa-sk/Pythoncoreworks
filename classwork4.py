#1write a program to find BMI(Body Mass Index)
# BMI= weight in (kg)/ height**2 in (m)
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese

# weight=float(input("enter the weight"))
# height=float(input("enter the height"))
# BMI=weight/height**2
# if BMI<=18.4:
#     print(f"{BMI} underweight")
# elif BMI>=18.5 and BMI<=24.9:
#     print(f"{BMI} Normal")
# elif BMI>=25.0 and BMI<=39.9:
#     print(f"{BMI} overweight")
# else:
#     print(f"{BMI} obese")


#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

# code=int(input("enter the code for product:1-battery based,2-key based,3-electrical:"))
# amount=int(input("enter the order amount:"))
# if code==1:
#        if amount>1000:
#            discount=amount*0.1
#            net_amount=amount-discount
#            print(f"{net_amount} is the net amount")
#        else:
#            print(amount)
# if code==2:
#        if amount>100:
#            discount=amount*0.05
#            net_amount=amount-discount
#            print(f"{net_amount} is the net amount")
#        else:
#            print(amount)
# if code==3:
#        if amount>500:
#            discount=amount*0.1
#            net_amount=amount-discount
#            print(f"{net_amount} is the net amount")
#        else:
#            print(amount)
# else:
#      print("error")

#3 FIZZBUZZ Problem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number

# num=int(input("enter the number:"))
# if num%3==0 and num%5==0:
#     print("FizzBuzz")
# elif num%3==0 and num%5!=0:
#     print("Fizz")
# elif num%5==0 and num%3!=0:
#     print("Buzz")
# else:
#     print(f"{num}")