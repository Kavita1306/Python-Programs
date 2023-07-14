class person:
    def __init__(self,x,y):
        self.add=x+y
        self.sub=x-y
        
    def myfunc(self):
     print("sum=",self.add)
     print("sub=",self.sub)
           
        
p1=person(50,25)
print(p1.myfunc())