#____________________________________________________________________________#
#------------------------CONDITIONAL STATEMENT IN PYTHON---------------------#
#1)If-else Statement
#Syntax:
value=12
if(value==30):
    print("No121")
elif(value==12):
    print("Yes")
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