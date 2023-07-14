class Class1:
    def test(self):
        print("In Class1")
       
class Class2(Class1):
    def test(self):
        print("In Class2")
 
class Class3(Class2,Class1):
    pass

obj = Class3()
obj.test()

