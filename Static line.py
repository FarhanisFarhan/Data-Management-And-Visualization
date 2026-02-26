import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig, ax = plt.subplots()

x_data = []
y_data = []

line, = ax.plot([], [], marker='o')

ax.set_xlim(0, 20)
ax.set_ylim(0, 100)

def update(frame):
    x_data.append(frame)
    y_data.append(random.randint(0, 100))
    
    line.set_data(x_data, y_data)
    return line,

ani = animation.FuncAnimation(fig, update, frames=range(20), interval=500)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Dynamic Line Chart")
plt.show()