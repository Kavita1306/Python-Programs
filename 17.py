def Repeat(x):
 _size=len(x)
 repeated=[]
 for i in range(_size):
     k=i+1
     for j in range(k,_size):
         if x[i]==x[j] and x[i] not in repeated:
             repeated.append(x[i])
     return repeated
list1=[45,56,23,10,20,45,67,19,56,63,45]
print("Duplicate element are:")
print(Repeat(list1))

