#wap to check whether the no is palindrome or not
n=int(input("Enter a number:"))
temp=n
rev=0
while(n>0):
          rem=n % 10
          rev=rev*10+rem
          n=n//10
if (rev==temp):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
