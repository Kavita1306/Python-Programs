import numpy as np
import pandas as pd
array=np.array([10,20,1,2,3,4,5,6,7])
print("Numpy array is:")
display(array)
series=pd.Series(array)
print("Pandas series:")
display(series)


import pandas as pd
list=['m','c','a']
ser=pd.Series(list)
print(ser)
