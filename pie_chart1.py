import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Python", "C++", "C", "Java"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Programming Languages:")
plt.show() 