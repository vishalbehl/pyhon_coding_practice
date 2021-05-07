#____________________________________________________________________________#
#--------------------------------LISTS in PYTHON-----------------------------#
#Syntax: list=[1,2,a,b]         Similar to Array
list=['toy','laptop','car','bike']
print(list)
print(list[0:2])
list[0]='dog'
print(list)
new_list=list           #Assign new list to previous one( Change occure when we change new list)
print(new_list[1:4])
new_list=list[:]        #Only copy the list (No change occure if we change new list )
print(new_list)
#__MATRIX IN PYTHON__#
#Syntax         (Similar to 2-D Arrays)
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][2])
#____________________________________________________________________________#
#----------------------------------List Methods------------------------------#
######_Adding in List_######
basket=[1,2,3,4,5]
basket.append(12)
print(basket)
basket.insert(2,34) 
print(basket)
basket.extend([100,122,233])
print(basket)
######_Removing in List_######
basket.pop()                    #Remove the value at last index
print(basket)   
basket.pop(2)                   ##Remove the value at given index
print(basket)   
print(basket.pop())             #Display the poped out value
print(basket.pop(2))            #Display the poped out value
basket.remove(100)              #Remove the object from the list
print(basket)
basket.clear()                  #Empty the list
print(basket)
######_Search in List_######
cart=[1,23,3,54,'a','d','v','d','b']
print(cart.index(23))                   #Search in the cart for given value
print('d' in cart)          
print('H' in 'Hi my name is Harry')     #Search for value in given sentence
print(cart.count('d'))                  #Count the number of times the value occure in the list
######_Sorting of List_######
cart1=['a','d','f','c','e','b']
#METHOD:1 (This method  modify cart.)
cart1.sort()
print(cart)
#METHOD:2 (This method doesn't modify cart instead create a new copy of basket)
print(sorted(cart1))
######_Reverse the List_######
#METHOD:1
cart1.reverse()
print(cart1)
#METHOD:2 (Using List Slicing)
print(cart1[::-1])
######_List the Range(From,To)_######
# print(list(range(1,23)))
######_List Unpacking_######
a,b,c,*other,d=[1,2,3,4,5,6,7,8,9]
print(a,b,c)
print(other)        ##
print(d)
#____________________________________________________________________________#
#------------------------------TUPLES IN PYTHON------------------------------#
#Tuples are similar to List but cannot be modified once initiallized
# Syntax: my_tuple:('value1','value2',-----)
# We cannot perform reverse,sort etc operation on tuples 
mytuple=(1,2,3,4,3,5,3,3,5,6)
print(mytuple.count(3))         #Count the number of occurance of value 
print((mytuple.index(4)))       #Return the index of the given value
print(len(mytuple))             #Return the length of the Tuple