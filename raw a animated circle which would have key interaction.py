import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

BOX_SIZE = 10
RADIUS = 0.5
STEP = 0.5

state = pd.DataFrame({
    "x": [BOX_SIZE / 2],
    "y": [BOX_SIZE / 2]
})

fig, ax = plt.subplots()

circle = Circle((state.loc[0, "x"], state.loc[0, "y"]), RADIUS, color="blue")
ax.add_patch(circle)

ax.set_xlim(0, BOX_SIZE)
ax.set_ylim(0, BOX_SIZE)
ax.set_aspect("equal")
ax.set_title("Move with Arrow Keys")

def update_circle():
    circle.center = (state.loc[0, "x"], state.loc[0, "y"])
    fig.canvas.draw_idle()

def on_key(event):
    x = state.loc[0, "x"]
    y = state.loc[0, "y"]

    if event.key == "left":
        x -= STEP
    elif event.key == "right":
        x += STEP
    elif event.key == "up":
        y += STEP
    elif event.key == "down":
        y -= STEP

    x = np.clip(x, RADIUS, BOX_SIZE - RADIUS)
    y = np.clip(y, RADIUS, BOX_SIZE - RADIUS)

    state.loc[0, "x"] = x
    state.loc[0, "y"] = y

    update_circle()

fig.canvas.mpl_connect("key_press_event", on_key)

plt.show()