class Student:
    #constructor
    
    def __init__(self,name,sector):
        self.name=name
        self.sector=sector
    def getInfo(self):
        print(self.name)
        print(self.sector)
        print("I am sangeeta Jena with lots of positivity and believes in sky is the limit")

    def display(self):
        print(f" Welcome {self.name} to the {self.sector} sector")

s1=Student("raj","banking")
  #constructor gets called automatically when object is created
s1.display()
s1.getInfo()

#whenever we pass the data to class constructor we need use__init__method

#parameters inside the method is called as local parameters
#(scope is only within the function)
#to get the value from a method in another method one need to save data in class variable

