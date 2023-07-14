import pandas as pd
import numpy as np
A = np.random.randint(10, size=(4,3))
A=np.array([[9, 2, 0],        
   [4, 3, 0],        
   [2, 3, 1],        
   [7, 1, 3]])

df = pd.DataFrame(A)
print(df)
