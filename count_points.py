import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import *
import math
import rotation_walk as rw
import os

######## Description ########
#Symulates rotation walk.
#Starts a the the first level, creates each level up to total_levels and counts points.
#Then displays points by level or total.
######### Arguments #########

r = 1
boundry = 2000000000
angles = [75]
angles_colors = ['b','r', 'g'] 
total_levels = 10
figure_side_size = 10
folder_path = "points_charts"

#############################

step = 1

def log_step(message):
    global step
    print(str(step) + ") " + message)
    step += 1

points_level_created = []
points_level_sum = []

log_step("### simulating number of poinst ###")
log_step("interating through angles")
for a in angles:
    log_step("processing angle " + str(a))

    log_step("getting nubmer of rotations")
    angles_degree = rw.get_angles(a)
    angles_rad = rw.convert_degree_to_rad(angles_degree)

    levels = [[(0,0)]]
    number_points = []
    sum_points = []

    levels_x = [[0]]
    levels_y = [[0]]

    marked = {(0,0)}

    log_step("iterating through levels")
    for i in range(1, total_levels+1):
        levels_x.append([])
        levels_y.append([])
        rw.process_level_stable(i-1, levels, r, boundry, levels_x[-1], levels_y[-1], angles_rad, marked)
    
    log_step("summing points")
    sum = 0
    for i in range(0, len(levels)):
        sum += len(levels[i])
        number_points.append(len(levels[i]))
        sum_points.append(sum)
        
    
    points_level_created.append(number_points)
    points_level_sum.append(sum_points)

log_step("plotting number of points")
fig, ax = plt.subplots(figsize = (figure_side_size, figure_side_size))

display = input("What do you wish to display? \n 1) L - points by level \n 2) T - points total \n 3) LT or TL - points by level and total \n")

if display == "LT":
    display = "TL"

title = ""

for i in range(0, len(angles)):
    title += str(angles[i])
    number = []
    for j in range(0, total_levels+1):
        number.append(j)
    if display == "L":
        ax.plot(number, points_level_created[i], marker='o', linestyle='-', color=angles_colors[i], label=str(angles[i]) + " points by level")
    elif display == "T":
        ax.plot(number, points_level_sum[i], marker='o', linestyle='--', color=angles_colors[i], label=str(angles[i]) + " total")
    elif display == "LT" or display == "TL":
        ax.plot(number, points_level_created[i], marker='o', linestyle='-', color=angles_colors[i], label=str(angles[i]) + " points by level")
        ax.plot(number, points_level_sum[i], marker='o', linestyle='--', color=angles_colors[i], label=str(angles[i]) + " total")
    if i < len(angles)-1:
        title += ", "

title += "katowa " + str(total_levels) + " poziomowa " + display
ax.set_title(title)

ax.legend()

save = input("Do you wish to save the chart? Y/n")

if save == "Y":
    plt.savefig(folder_path + "\\"+title)

plt.show()

