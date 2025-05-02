class Rect:
    def __init__(self,l,b):
        self.l=1
        self.b=b
    def area(self):
        return self.l*self.b

r=Rect(30,5)
ans=r.area()
print("the area of rectangle is",ans)





#area of rectangle
class Rect:
    def __init__(self,l,b):
        self.l=1
        self.b=b
    def area(self):
        return self.l*self.b
num1=int(input("enter length:"))
num2=int(input("enter breadth:"))
r=Rect(num1,num2)
ans=r.area()
print("the area of rectangle is",ans)
         
