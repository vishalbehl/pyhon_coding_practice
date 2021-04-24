#_____________##################_PYTHON NOTES_##################_____________#
#_____________________________Author: Vishal Behl____________________________#
#____________________________________________________________________________#
#-------------------------Basic Mathematics Functions------------------------#
print(2+3)                  #ADD
print(2-3)                  #SUB
print(2*3)                  #MULTIPLY
print(2/3)                  #DIVIDE
print(6%5)                  #MODE(REMINDER)
print(type(1.22))           #Gives Data Type of the value
print(2**3)                 #Power Operation
print(16//2)                #Double Divide
print(round(2.3))           #Round the Number
print(abs(-23))             #Gives Absolute value of number
print(bin(23))              #Print Binary number of the given number
print(int('0b0100',2))      #Returns the integer value of given Binary Number
#____________________________________________________________________________#
#----------------------------Operator Precedence-----------------------------#
#1) ()
#2) **
#3) * /
#4) + -
#____________________________________________________________________________#
#-----------------------------Variables in Python----------------------------#
_private=23         #Declaring a Private variable
print(_private)     #Accessing the Variable
a,b,c=1,2,4         #Assigning values to variables simuntaneously
print(a,b,c)
#____________________________________________________________________________#
#-----------------------------------Strings----------------------------------#
#METHOD:1
print("Hello World!")
#METHOD:2
a='Hey'
print(a)
#METHOD:3
#Printing Multiple Line at once using '''_____'''
long_string='''
THIS IS A TEST LINE.
THIS IS A TEST LINE.
THIS IS A TEST LINE.
THIS IS A TEST LINE.
'''
print(long_string)
#METHOD:4   (STRING CONCATENATION)
first_name="Vishal"
last_name="Behl"
fullname=first_name+' '+last_name
print(fullname)
#____________________________________________________________________________#
#------------------------------TYPE CONVERSION-------------------------------#
a=str(100)
b=int(a)
c=type(b)
print(c)
print(type(int(str(100))))
#____________________________________________________________________________#
#-------------------------------ESCAPE SEQUENCE------------------------------#
string='\t\'Hello World\'\n This is a Test'
print(string)
#____________________________________________________________________________#
#------------------------------FORMATTED STRINGS-----------------------------#
name='John'
age='23'
print('Hi! '+name+'. Your age is '+age+' year old.')
#In Python3     (Here f denotes the Formatted String)
print(f'Hi! {name}. Your age is {age} year old.')
print('Hi! {}. Your age is {} year old.'.format('John','23'))
print('Hi! {1}. Your age is {0} year old.'.format('John','23'))
print('Hi! {name}. Your age is {age} year old.'.format(name='John',age='23'))
#____________________________________________________________________________#
#-------------------------------STRING INDEXING------------------------------#
string='ABCDEFGEH'   
#indexing:(0)(1)(2)(3)(4)(5)(6)(7)
#Value[start_index:stop_index:stepover]    (Method is known as String Slicing)
print(string[0:8:2])        
print(string[0:])
print(string+'23')
#Reverse Indexing:(-7)(-6)(-5)(-4)(-3)(-2)(-1)
print(string[::-1])     #Reverse the String
# IMMUTABILITY: Strings in Python are Immutable i.e. they cannot be changed.
# Such that we cannot reassign the value on a specific index in string.     
# Eg:string[2]='7' is not possible but string='2323' is possible.
#____________________________________________________________________________#
#-----------------------------Some Built-in Function-------------------------#
print(len('Vishal Behl'))       #Gives Length of String
string='hey how are you?'
print(string.upper())           #Capitalize the String
print(string.capitalize())      #Capitalize first Alphabet of String
print(string.find('how'))       #Find the First occurance of the word at index
print(string.replace('how','who'))  #Replace Function 
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
#---------------------------DICTIONARY IN PYTHON-----------------------------#
#SYNNTAX:
# dictionary={
#     'key': value,
#     'key': value
# }
dictionary={
    'Tree':'plant',
    'Python':'Very Useful',
    'a':True,
    'b':[1,2,3,4,5,6]
}
print(dictionary['Python'])
print(dictionary)
print(dictionary['b'])
print(dictionary.get('a'))
print(dictionary.get('d', 23))   #Set value of 'd':23 if not exist
#Create a new empty dictionary(Not Preffered)
print(dict(name='Vishal'))     
#Finding in dictionary  
print('a' in dictionary)
print('plant' in dictionary.values())
#print the dictionary items
print(dictionary.items())
#Copy the Dictionary
dic2=dictionary.copy()
print(dic2)
#Remove the given key
print(dictionary.pop('Tree')) 
print(dictionary)      
#Remove from the end
print(dictionary.popitem())         
print(dictionary)
#Update the dictionary
print(dictionary.update({'s':False}))   
print(dictionary)
#Clear the Dictionary
print(dictionary.clear())
#____________________________________________________________________________#
#------------------------------TUPLES IN PYTHON------------------------------#
#Tuples are similar to List but cannot be modified once initiallized
# Syntax: my_tuple:('value1','value2',-----)
# We cannot perform reverse,sort etc operation on tuples 
mytuple=(1,2,3,4,3,5,3,3,5,6)
print(mytuple.count(3))         #Count the number of occurance of value 
print((mytuple.index(4)))       #Return the index of the given value
print(len(mytuple))             #Return the length of the Tuple
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
#____________________________________________________________________________#
#------------------------CONDITIONAL STATEMENT IN PYTHON---------------------#
#1)If-else Statement
#Syntax:
value=12
if(value==30):
    print("Yes")
elif(value==12):
    print("Hmmmm")
else:
    print("No")
#2)Ternary Operator
#Syntax: (do_this) if 'condition' else (do_that)
a,b=32,32
print("Equal" if a==b else "not equal") 
a, b = 170, 20  
print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")
#and/or 
a,b=20,30
if(a==20 or a>b):
    print("IT IS TRUE!")
else:
    print("NOT TRUE")
#____________________________________________________________________________#
#-------------------------------LOOPS IN PYTHON------------------------------#
#1)For Loops
#Syntax: for 'value' in range(from,to,stepover): print(_this_) 
#Eg:1
for i in 'Hi I am Vishal':
    print(i)
#Eg:2 Print Counting (1-10)
for i in range(1,10):       #for(i=1;i<10;i++) in C/C++
    print(i)
#Eg:3 Gives Factors of 10
for i in range(1,10):
    if(10%i==0):
        print(i)
#Eg:4 Total of Range(1-10)
n=0
for i in range(1,11):
    n=n+i
print(n)
#Nested-Loops
#Eg:1
for i in range(1,4):
    for j in range(1,5):
        print(i,j)
#Using Dictionary
user={'name':"vishalbehl",'sec':"cse_3b",'rollno':101}
for item in user:
    print(item)
for item in user.keys():
    print(item)
for item in user.items():
    print(item)
for item in user.values():
    print(item)

#2)While Loops
#Syntax: while condition: print(_this_)
#Eg1:
i=1
while i<=5:
    print(i)
    i=i+1
#Eg2: 
# while True:
#     response=input('Say Somethig:')
#     if(response=='Bye'):
#         break
#Eg3: We can use else with while loop
i=1
while i<=5:
    print(i)
    i=i+1
else: print("Out of Loop")

#GUI USING LOOPS
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,1,1,1,0,0],
  [0,0,1,1,1,0,0]
]
for image in picture:
  for pixel in image:
    if (pixel==1):
      print('*', end ="")
    else:
      print(' ', end ="")
  print('')
#EXERCISE:1 Check for Duplicates in List
list_1=['a','b','b','c','d','e','e']        #GIVEN LIST
duplicates=[]                               #EMPTY LIST TO STORE DUPLICATE
for value in list_1:                        #Traversing the list for the value
    if list_1.count(value)>1:               
        if value not in duplicates:         #Check whether duplicate has same value or not 
            duplicates.append(value)        #If not then add the value to duplicate list
print(duplicates)                           #Print duplicates
#____________________________________________________________________________#
#-----------------------------FUNCTIONS IN PYTHON----------------------------#
#Syntax: def Funct():    {TO-DO}
#Eg:
def say_hello():            #Declaring a Function
    print("HELLOOOO")
say_hello()                 #Calling a Function
#Parameters:
def say_hello(fname,lname):
    print(f"Hello {fname} {lname}")
#Arguement:
#1)Positional Arguement
say_hello("Vishal","Behl")
#2)Keyword Arguement
say_hello(lname="Jr",fname="Dale")

#COMMENTING IN FUNCTION
def comment():
    '''Commment in functions'''
    print("comment")
#Both arguements gives the comment in the function
# help(comment)
# print(comment.__doc__)
###############################################################
#*args(Arguement):Taking the parameters as tuple 
#**kwargs(Keyword arguement):Taking the parameters as dictionary

def func(*args,**kwargs):
    total=0
    for items in kwargs.values():
        total+=items
    return sum(args) + total

print(func(1,2,3,4,5,num1=32,num2=33))

#RULE FOR PRECEDENCE: params,*args,default params,**kwargs
################################################################

#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_END_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#