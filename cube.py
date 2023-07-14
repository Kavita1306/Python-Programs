n=input(" Enter a number: ")
sum=0
for i in range(0,len(n)):
  sum=sum+pow(int(n[i]),3)
print("Sum of cube of digits  : ",sum)
if(sum==int(n)):
  print("Digits are matching to cube  : ", n)
else:
  print("Digits are not matching to cube : ", n)