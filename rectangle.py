length=float(input("enter the length of the rectangle:"))
width=float(input("enter the width of the rectangle:"))

area=length*width
print("the area of the rectangle is:",area)


import math
radius=float(input("enter the radius of the circle:"))
area=math.pi*radius**2
print("the area of the circle is:",area)


num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
num3=float(input("enter third number:"))
average=(num1+num2+num3)/3
print("the average of the three numbers is:",average)


age=int(input("enter your age:"))
if age>=18:
    print("you are eligible to vote.")
else:
    print("you are not eligible to vote.")



num=int(input("enter a number:"))
if num%5==0:
    print("the number is divisible by 5.")
else:
    print("the number is not divisible by 5.")
