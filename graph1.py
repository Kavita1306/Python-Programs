import numpy as np
import matplotlib.pyplot as plt
# Create NumPy array for x
x = np.linspace(-10, 10, 100)  
# Create a list of y = x^2 using list comprehension
y = [i*i for i in x]
# Plot
plt.plot(x, y)
plt.show()