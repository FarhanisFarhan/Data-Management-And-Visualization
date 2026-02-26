import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig, ax = plt.subplots()

data = []

def update(frame):
    ax.clear() 
    
    data.append(random.randint(0, 100))
    
    ax.hist(data, bins=10)
    
    ax.set_title("Dynamic Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

ani = animation.FuncAnimation(fig, update, interval=500)

plt.show()