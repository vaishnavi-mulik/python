'''
python list methods are built-in functions that allow us
to perform various operations on lists,
such as adding,removing, or modifying elements.

append():adds an element to the end of the list.
copy():returns a shallow copy of the list.
clear():removes all elements from the list.
count():returns the number of times a specified element appears in the list.
extend():adds elements from another list to the end ofthe current list.
index():returns the index of the first occurrence of a specified element.
insert():inserts an element at a specified position.
pop():removes and returns the elements at the specified position(or the last element)
remove():removes the first occurrence of a specified element.
reverse():reverses the order of the elements in the list.
sort():sorts the list in ascending order (by default).
'''

mylist=[45,56,23,45,23]
print("my original list is",mylist) 

mylist.append(35)
print("list with append operation",mylist)

lcount=mylist.count(45)
print("list of items",lcount)





