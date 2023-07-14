class Parent1():
    def show(self):
        print("Inside Parent1")
class parent2():
    def display(self):
        print("Inside Parent2")

class Child(Parent1,parent2):
    def show(self):
        print("Inside child")

obj=Child()
obj.show()
obj.display()