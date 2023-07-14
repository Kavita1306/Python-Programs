list=["a","b","c"]
index1=list.index("a")
index2=list.index("c")
list[index1],list[index2]=list[index2],list[index1]
print(list)
