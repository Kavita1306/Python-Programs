import numpy as np 
my_array = np.arange(12).reshape(4, 3)
print("Original array:")
print(my_array)

my_array[:, [2, 0]] = my_array[:, [0, 2]]
print("After swapping arrays the last column and first column:")
print(my_array)