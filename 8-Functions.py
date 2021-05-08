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
#Lambda Functions:
#These are the one liner statement used to define a function
minus=lambda x,y :x-y
print(minus(19,12))
################################################################
