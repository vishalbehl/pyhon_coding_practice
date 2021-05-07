#____________________________________________________________________________#
#---------------------------------SETS IN PYTHON-----------------------------#
#1)Set is a Unordered collection of Unique objects/value.
#2)Set is similar to dictionary but without Keys.
#3)Set doesn't support indexing.
#4)Syntax: set={value1,value2,------}
myset={1,2,3,4,5,6,7}
print(myset)
#Add the Value at the end
myset.add(12) 
print(myset)
#Pop the value from the beginning
myset.pop()
print(myset)
#Creating set from a List
list1=[1,2,3,4,5,5]
print(set(list1))

#Finding Function
print(2 in myset)
#Return the length of set
print(len(myset))
#Clear the set
print(myset.clear())
#Converting Set to List
# print(list(myset))
#Copying a Set
newset=myset.copy()
print(newset)
########SOME BUILT-IN FUNCTIONS#########
myset={1,2,3,4,5}
newset={4,5,6,7,8}
# print(myset.difference(newset))
# print(myset.intersection(newset))
# print(myset & newset)
# print(myset.discard(4))
# print(myset)
# print(myset.difference_update(newset))
# print(myset)
# print(myset.isdisjoint(newset))
# print(myset.issubset(newset))
# print(myset.issuperset(newset))
# print(myset.union(newset))
# print(myset | newset)