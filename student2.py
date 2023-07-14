class student:
    def __init__(self):
        self.roll=input("Enter the rollno:")
        self.name=input("Enter the name:")
        self.s_class=input("Enter the class:")

class demo(student):
    def display(self):
        print("##### Student Details Are #####")
        print("Rollno:",self.roll)
        print("Name:",self.name)
        print("Class:",self.s_class)

s=demo()
s.display()
