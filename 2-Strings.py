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
print(f"Hi! {name}. Your age is {age} year old")
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
