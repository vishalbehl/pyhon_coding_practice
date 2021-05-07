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
