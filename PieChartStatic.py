import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [25, 35, 20, 20]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.axis('equal')

plt.title("Static Pie Chart")
plt.show()
