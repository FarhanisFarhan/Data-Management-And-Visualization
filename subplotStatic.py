import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 6)
y1 = x * 2
y2 = x ** 2
y3 = x * 3
y4 = x ** 3

fig, axs = plt.subplots(2, 2, figsize=(8, 6))


axs[0, 0].plot(x, y1)
axs[0, 0].set_title("Linear (x*2)")

axs[0, 1].plot(x, y2)
axs[0, 1].set_title("Square (x^2)")

axs[1, 0].plot(x, y3)
axs[1, 0].set_title("Linear (x*3)")

axs[1, 1].plot(x, y4)
axs[1, 1].set_title("Cube (x^3)")

plt.tight_layout()


plt.show()
