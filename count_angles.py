import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import *
import math
import rotation_walk as rw
import os

fig, ax = plt.subplots(figsize = (20,20))

for i in range(0, 360):
    angles = rw.get_angles(i)

    # print(i, end=": ")
    # print(len(angles))
    ax.plot([i], [len(angles)], 'ko', markersize = 3)

ax.set_xticks(np.arange(0, 370, 10)) 
ax.set_yticks(np.arange(0, 370, 10))
plt.show()