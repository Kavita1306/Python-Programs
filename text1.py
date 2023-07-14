import numpy as np
Data= np.loadtxt("demo.txt",usecols=1,dtype='str')
for each in Data:
    print(each)