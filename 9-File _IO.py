#____________________________________________________________________________#
#------------------------------FILE I/O IN PYTHON----------------------------#
'''MODES OF FILE
    -'r': Read the conntent of the file
    -'w': Write the content in the file with formatting previous content 
    -'a': Append the content of the file
    -'x': Create file of not exist 
    -'t': Text mode
    -'b': Binary mode
    -'+': Read and Write
Syntax:
f=open(file.txt)        Here 'f' is the pointer to the file
content=f.read()
print(content)
f.close
'''
f=open("file.txt","r")
# f.write("///.................Vishal Behl..................///")
# content=f.read(10)
# print(content)
# for line in f:
#     # content=f.read()
#     print(line)
print(f.readline())
print(f.tell())                 #Gives the position of the pointer in the file
# print(f.readlines())            #Gives the Text in file in the form of List
f.seek(0)                        #Reset the position to the pointer specified
print(f.readline())
f.close

#Using with block to open a file
with open("file.txt") as f:
    print(f.readline())