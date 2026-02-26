import matplotlib.pyplot as plt

data = [12, 15, 13, 17, 19, 21, 22, 25, 18, 16, 14, 20, 23, 24]

plt.hist(data, bins=5)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Static Histogram")

plt.grid(True)

plt.show()