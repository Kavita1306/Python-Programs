#Date:03-11-2022#

import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)


a=np.array([(1,2,3),(6,7,8)])
b=np.array([(4,5,6),(3,7,9)])
print(a.shape)
print(a.max())
print(a.min())
print(a.sum()+b.sum())


