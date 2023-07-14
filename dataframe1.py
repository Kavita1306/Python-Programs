import pandas as pd
dict_a = {
   'col_a':[1,2,3,4], 
   'col_b': [2,5,6,7], 
   'col_c':['a','b','c','d']
}
df = pd.DataFrame(dict_a)
print(df)