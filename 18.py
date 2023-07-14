list=[10,"python",8,43,"Programming",34]
temp=0
for i in list:
 try:
     temp=temp+i
 except TypeError:
            pass
        
print(temp)
