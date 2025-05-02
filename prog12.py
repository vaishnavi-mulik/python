#wap to get sum of digits (example:234 sum=9)

num=int(input("Enter a number"))
sum1=0
while(num>0):
    rem=num%10
    sum1=sum1+rem
    num=num//10
print("The sum of digit is",sum1)


#wap to check whether the number is armstrong or not
#153=(3)^3+(5)^3+(1)^3=27+125+1=153

arm=0
n=int(input("Enter a number"))
temp=n
while(n>0):
          rem=n%10
          arm=arm+rem*rem*rem
          n=n//10
print("The number addition is armstrong")
if(arm==temp):
    print("The number is armstrong")
else:
    print("The number is not armstrong")
