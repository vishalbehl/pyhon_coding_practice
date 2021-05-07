class playerchar:
#Constructor
    def __init__(self,name,age):
        self.name=name                  #Attributes
        self.age=age
    def run(self):
        print("Run!")
        return "Done"
    @classmethod                        #Decorators
    def add(cls,n1,n2):
        return cls('Andy',n1+n2)
    @classmethod                        #Decorators
    def add1(cls,n1,n2):
        return n1+n2
    @staticmethod
    def add2(n,m):
        return n+m
player1=playerchar("Vishal", "20")      #Objects
player2=playerchar("Vikram", "21")
print(player1)
print(player1.age)
print(player2.run())
print(player1.add(12,23))
print(playerchar.add1(12,22))            #We can use decorator with direct class without creating any object 
print(player1.add2(12,12))
# help(player1)                           #Gives the Blueprint of the Object.


#ENCAPSULATION
