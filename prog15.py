
emp=["Sam","Ram","Shyam","ghanashyam"]
stud=[1,"Ramesh","malad","O Grade"]

print(emp)
print("The list of student record",stud)
#stud(null)
#stud.add(null)
print("the final list of students is:",stud)


#you can access individual value using index
print(emp[0])
print(stud[2])
print(stud[-1])

#updating list
emp[2]="Raghav"
print(emp)
stud.append("9 cgpa")  #adding elements at the end
stud.insert(1,"Suresh")
print(stud)

#remove an element
stud.remove("Ramesh")
print(stud)
stud.pop()
print(stud)
stud.clear()
print(stud)

#create list with five elements and find minimum among it
list=[45,56,23,2,67]

minimum=list[0]

for i in list:
     if i<minimum:
         minimum=i
print("the minimum is",minimum)


#wap to find maximum in a list
l=[65,24,89,37,5]

maxElem=l[1]

for i in l:
    if i>maxElem:
        maxElem=i

print("The maximum element is ",maxElem)



#wap to find minimum in a list


