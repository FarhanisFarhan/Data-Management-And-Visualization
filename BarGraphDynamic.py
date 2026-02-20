import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation


categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 4]

fig, ax = plt.subplots()
bars = ax.bar(categories, values, color='skyblue')

ax.set_ylim(0, 10)
ax.set_title("Dynamic Bar Chart")
ax.set_ylabel("Value")

def update(frame):
    new_values = [random.randint(1, 10) for _ in values]
    for bar, new_val in zip(bars, new_values):
        bar.set_height(new_val)
    return bars

ani = FuncAnimation(fig, update, interval=1000)

plt.show()
