import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()


x_data, y_data = [], []
sc = ax.scatter(x_data, y_data, color='blue')

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title("Dynamic Scatter Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

def update(frame):
 
    new_x = np.random.rand() * 10
    new_y = np.random.rand() * 10
    
    x_data.append(new_x)
    y_data.append(new_y)
    
    sc.set_offsets(np.c_[x_data, y_data])
    return sc,

ani = FuncAnimation(fig, update, interval=500)

plt.show()
