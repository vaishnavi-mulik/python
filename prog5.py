#conditional statements:To validate user input we need conditional statements
'''There are three conditional statements:
1)if
2)if...else
3)if...elif...else

syntax:if

if(test condition):
     block of stmt
'''

pin=123
if(pin==183):
    print("Welcome to SBI service")

num=int(input("Enter a number"))
if(num>0):
    print("It's positive value")


#WAP to check whether the number is positive or not
a=int(input("Enter a number"))

if(a>0):
    print("The entered number is positive")
else:
    print("The number is negative")

#WAP to check whether the number is positive or not

num=int(input("Enter a number"))
if(num%2==0):
    print("Given number is even")
else:
    print("Given number is odd")

#WAP to find greatest number among two
#WAP TO check whether number is divisible by 5 or not
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
