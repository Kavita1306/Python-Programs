import matplotlib.pyplot as plt
import numpy as np
a=np.array([83,45,67,21,50,32,72,10,30,61,2,84,45,22])
fig,ax=plt.subplots(figsize=(10,5))
ax.hist(a,bins=[0,25,50,75,100])
plt.show()
