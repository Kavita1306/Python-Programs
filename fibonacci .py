# program to print fibonacci series.
n = int(input("Enter the size of the series:"))
a = 0
b = 1
i = 0
for i in range(0 , n):
    print(a , end = ' ')
    c = a + b
    a = b
    b = c

    

