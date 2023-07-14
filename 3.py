largest = {"first": 0, "second": 0, "third": 0}

lst = [12, 45, 20,67,88,43,21,34,64]

for number in lst:
   if number > largest["first"]:
       largest["third"] = largest["second"]
       largest["second"] = largest["first"]
       largest["first"] = number
   elif number > largest["second"]:
       largest["third"] = largest["second"]
       largest["second"] = number
   elif number > largest["third"]:
       largest["third"] = number
print(largest["third"])