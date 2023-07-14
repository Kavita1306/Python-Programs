#Program to print the sum of the digits.
num = int(input("Enter the Number: "))
sum = 0
while num>0:
    n = num % 10
    sum = int(n) + sum
    num = num/10
print(sum)







