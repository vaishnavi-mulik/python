#set: it is a fundamental datastructure which is one of built in
#data type(dictionary,list,tuple,set)
#python provides built-in operations for performing set operations
#such as union,intersection,differences and symmetric difference.
#set is  created using curly bracket{

myset={12,78,34,78}
print(myset)

myset2={76,34,22}
print(myset2)
print(type(myset))

#union of two set using'|' operator
res=myset|myset2
print("The union of both the set",res)

#using union() method
res2=myset.union(myset2)
print("The union of both the sets are",res2)

#intersection of two sets
res=myset & myset2
print(res)

res=myset.intersection(myset2)
print(res)

#set Difference(-)
res=myset-myset2
print("The set difference is",res)

#symmetric set difference ^
res=myset^myset2
print(res)
