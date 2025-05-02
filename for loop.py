#program to print squares of numbers in a given range

#get input from the user
start=int(input("enter the start of the range:"))
end=int(input("enter the end of the range:"))

print(f"\nSquares of numbers from(start) to(end):")
#loop through the range and print squares
for num in range(start,end+1):
    print(f"(num)^2=(num**2)")
