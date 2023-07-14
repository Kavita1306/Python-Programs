def Cloning(list):
    li_copy=list[:]
    return li_copy

list=[2,6,7,3,8,9,10]
list2=Cloning(list)
print("Original list",list)
print("After Clonning:",list2)
