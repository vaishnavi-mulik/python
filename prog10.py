#wap to reverse given number by user
# example:n=123 output:321
rev=0
n=int(input("Enter a number"))
while(n>0):
    rem=n%10
    rev=rev*10+rem  #recursive
    n=n//10   #this will give qutient
    print(rev)
print("The reverse number is",rev)
'''
Dry Run:
n=123
iteration1:123>0 T
       rem=123%10=3
       rev=0*10+3=3
       n=12
iteration2:n=12
12>0 T
rem=12%10=2
rev=3*10+2=32
n=1


iteration3: n=1
1>0 T
rem=1%10=1
rev=32*10+1=321
n=1/10=0

iteration4:n=0 0>0 F
'''
