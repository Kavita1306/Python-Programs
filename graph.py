import numpy as np
import matplotlib.pyplot as plt

# data to plot
marks_Kavita = [87, 68, 40, 63]
marks_Khushboo = [75, 62, 54, 34]

# create plot
fig, ax = plt.subplots()
bar_width = 0.35
X = np.arange(4)

p1 = plt.bar(X, marks_Kavita, bar_width, color='b',
label='Kavita')

# The bar of second plot starts where the first bar ends
p2 = plt.bar(X + bar_width, marks_Khushboo, bar_width,
color='g',
label='Khushboo')

plt.xlabel('Subject')
plt.ylabel('Scores')
plt.title('Scores in each subject')
plt.xticks(X + (bar_width/2) , ("English", "Science", "Sports", "History"))
plt.legend()
plt.tight_layout()
plt.show()