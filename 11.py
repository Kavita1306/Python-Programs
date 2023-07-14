file = open('intro.txt','w')
integer_list = [77,42,31,11,10,9]
x = 0
for y in integer_list:
   x += y
print("File has been created successfully:") 
print("Sum of list",x)
file.close()



