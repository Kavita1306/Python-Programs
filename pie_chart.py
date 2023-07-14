import matplotlib.pyplot as plt
labels = 'Python', 'C++', 'C', 'Java'
sizes = [125, 75, 231, 149]
colors = ['blue', 'green', 'red', 'lightskyblue']
explode = (0.1, 0, 0, 0)  
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()