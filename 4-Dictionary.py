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