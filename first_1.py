##Date:07/10/2022##
## write a program to print MCA 1st sem##
##print("MCA 1st sem")##

##Add numbers##
##a=10
##b=20
##sum=0
##c=a+b
##print(c)

#circumference of circle##
##r= int(input("Enter the radius:"))
##pi=3.14
##c=2*pi*r
##print(c)##


## find square root of the number##
##import math
##n=int(input("Enter the number:"))
##root=math.sqrt(n)
##print(root)##


## find whether the number is rational or not##

##n=int(input("Enter the number:"))
##if(n>0):
##print("the number is Positive")##


##Write a program to find largest number
#a=int(input("Enter the value of a:"))
##b=int(input("Enter the value of b:"))
##c=int(input("Enter the value of c:"))
##if a>b and a>c:
    ##print("a is the largest number")
    


##list=[10,5,7,34,12,18]
##print("Largest number is:",max(list))##



#Create a sequence which is a tuple of numbers

#numbers=[4,2,6,7,3,5,8,10,5,8,9]
#square=0
#squares=[]
#for value in numbers:
    #square= value**2
    #squares.append(square)
    #print(squares)#



    ## range Program##
#print(range(15))
#print(list(range(15)))
#print(list(range(4,9)))
#print(list(range(5,25,4)))#


#Program using while loop##

#count=0
#while(count<3):
    #count=count+1
    #print("Kavita")##


    #create an empty dictionary#

#dict={}
#print("Empty Dictionary")
#print(dict)

#Dict=dict({1:'python',2:'C++'})
#print("\n Create Dictionary by using dict(): ")
#print(Dict)#


#Dict=dict([(1,"python"),(2,"C"),(3,"C++")])
#print("The value Pairs are:")
#print(Dict)#


Employee={"Name":"MCA","Age":29,"Salary":80000,"Company":"TCS"}
print(type(Employee))
print("printing Employee data.....")
print("Name:%s"%Employee["Name"])
print("Age:%d"%Employee["Age"])
print("Salary:%d"%Employee["Salary"])
print("Company:%s"%Employee["Company"])