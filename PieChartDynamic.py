import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

labels = ['A', 'B', 'C', 'D']
values = [25, 35, 20, 20]

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    

    new_values = [random.randint(10, 40) for _ in values]
    
    ax.pie(new_values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title("Dynamic Pie Chart")

ani = FuncAnimation(fig, update, interval=1000)

plt.show()
