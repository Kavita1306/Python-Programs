class student:
    def getinfo(self,rollno,name,s_class):
        student.rollno=rollno
        student.name=name
        student.s_class=s_class

    def display(self):
        print("**** Student Details Are ****")
        print("Roll no is:",student.rollno)
        print("Nmae is:",student.name)
        print("Class is:",student.s_class)

rollno=input("Enter the roll no of the student:")
name=input("Enter the name of the student:")
s_class=input("Enter the class of the student:")
    
s1= student()
s1.getinfo(rollno,name,s_class)
s1.display()