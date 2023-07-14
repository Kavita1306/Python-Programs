my_list=[]
for n in range(100,1000): 
  sum=0
  my_str=str(n)
  k=len(my_str)
  for i in range(0,k):
    sum=sum+pow(int(my_str[i]),3)
  if(sum==int(n)):
    print("This is an matching number: ",n)  
    my_list.append(n)
print("Highest number is: ",max(my_list))
print("Lowest  number is : ",min(my_list))