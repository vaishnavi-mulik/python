#WAP to find greatest number among two
#WAP TO check whether number is divisible by 5 or not
num=int(input("Enter a number:"))
if(num%5==0):
    print("Given number is even")
else:
    print("The number is odd")


#WAP to check whether the number is divisible by 5 and 3

num=int(input("Enter number:"))
if(num%5==0 and num%3==0):   #both conditions must true simultaneously
    print(num,"in divisible by 5 and 3")
else:
    print(num,"is not divisible by both 5 and 3")

#WAP to check year is leap yr or not
'''
Note: A year is a leap year if "any one of " the following conditions are satisfied:

The year is multiple of 400.
The year is a multiple of 4 and not a multiple of 100.
'''

#Get input from user
year = int (input("Enter a year:"))
#Leap year check
if(year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year}is a leap year.")
else:
    print(f"{year}is not a leap year.")
