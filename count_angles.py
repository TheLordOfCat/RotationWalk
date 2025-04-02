import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import *
import math
import rotation_walk as rw
import os

fig, ax = plt.subplots(figsize = (20,20))

all_angles = []

for i in range(0, 360):
    angles = rw.get_angles(i)

    all_angles.append(len(angles))

    # print(i, end=": ")
    # print(len(angles))
    # ax.plot([i], [len(angles)], 'ko', markersize = 3)

# print("Angels,Number")
# for i in range(0, 360):
#     print(str(i) + "," + str(all_angles[i]))

# ax.set_xticks(np.arange(0, 370, 10)) 
# ax.set_yticks(np.arange(0, 370, 10))
# plt.show()

unice_angles = []
for i in range(0, 360):
    found = False
    ind = 0
    for j in range(0, len(unice_angles)):
        if unice_angles[j][0] == all_angles[i]:
            found = True
            ind = j
            break

    if not found:
        unice_angles.append((all_angles[i], 1, i))
    else:
        unice_angles[ind] = (unice_angles[ind][0], unice_angles[ind][1] + 1, unice_angles[ind][2])

    
unice_angles.sort()
for i in range(0, len(unice_angles)):
    print(str(unice_angles[i][0]) + "," + str(unice_angles[i][1])+ "," + str(unice_angles[i][2]))
