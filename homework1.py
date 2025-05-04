num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
 if num1>num2:
     print(f"{num1}is greater than{num2}.")
 elif num2>num1:
     print(f"{num2} is greater than {num1}.")
 else:
     print("both numbers are equal.")


age=int(input("enter your age:"))
if age>=18:
    print("you are eligible to vote.")
else:
    print("you are not eligible to vote.")



num=int(input("'enter a number:"))

    if num%2 == 0;
        print(f"{num}is an even number.")
    else:
        print(f"{num}is not an even number.")

    
basic_salary=float(input("enter the basic salary:"))
da=0
hra=0
if basic_salary>50000:
    da=0.10*basic_salary
    hra=0.12*basic_salary

total_salary=basic_salary*da*hra
print(f"basic salary:{basic_salary}")
print(f"da(10%):{da}")
print(f"hra(12%):{hra}")
print(f"total salary:{total_salary}")
