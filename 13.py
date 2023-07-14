list=[11,45,56,78,64]
print("Original list:")
print(list)
for i in list:
    if(i%2==0):
        list.remove(i)

print("List after removing negative numbers:")
print(list)