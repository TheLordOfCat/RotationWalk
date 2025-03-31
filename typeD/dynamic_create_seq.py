import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import *
import math
import rotation_walk as rw
import os

######### Arguments #########

r = 10
angle = 75 #in degrees <0,360>
total_levels = 3  # >= 1
boundry = 100
folder_path = 'typeD\\dynamic_colored'
points_scaling = 3
points_size = [6, 5, 4, 3, 2, 1, 0.5, 0.25, 0.125]
figure_side_size = 20
level_colors = ['ko', 'go', 'bo', 'ro']

#############################
step = 1

def log_step(message):
    global step
    print(str(step) + ") " + message)
    step += 1

levels = [[(0,0)]]
levels_x = [[0]]
levels_y = [[0]]

print("### Symulating Rotational Walk ###")
log_step("getting number of rotations")

angles_degree = rw.get_angles(angle)
angles_rad = rw.convert_degree_to_rad(angles_degree)

log_step("approximating number of points")
approx_number_of_points = [0]
for i in range(1, total_levels+1):
    temp = approx_number_of_points[-1]
    temp += rw.get_aproximation(len(angles_degree), i)
    approx_number_of_points.append(temp)

print("Approximated number of points = " + str(approx_number_of_points))
proceed = input("Do you wish to proceed Y/n?")

log_step("checking color integrity")
if total_levels+1 > len(level_colors):
    fill_level_colors = input("Number of total_levels exeeds lenght of level_colors. Do you wish to fill it in Y/n?")
    if fill_level_colors == "Y":
        while total_levels+1 > len(level_colors):
            level_colors.append("ko")
    else:
        proceed = "n"

if proceed == "Y":
    log_step("creating folder")
    folder_path = os.path.join(folder_path, "sekwencja - " + str(angle) + "katna, " + str(i) + " poziomowa")

    if not os.path.exists(folder_path):
        # Create the directory (including any necessary parent directories)
        os.makedirs(folder_path)

    for i in range(1, total_levels+1):
        fig, ax = plt.subplots(figsize = (figure_side_size, figure_side_size))
        log_step("processing level number - " + str(i))
        log_step("adding points")

        levels_x.append([])
        levels_y.append([])
        rw.process_level_dynamic(i-1, levels, r, boundry, levels_x[-1], levels_y[-1], angles_rad)

        log_step("plotting points")

        title = "Spacer-" + str(angle) + "katny," + str(i) + "poziomowy.png"
        fig.suptitle(title, fontsize=8) 

        index_size = 0
        while points_scaling**(index_size+1) < approx_number_of_points[i]:
            if index_size+1 < len(points_size):
                index_size += 1
            else:
                break
        
        for j in range(0, len(levels)):
            ax.plot(levels_x[j], levels_y[j], level_colors[j], label = "level " + str(j), markersize = points_size[index_size])

        ax.legend()
        fig.savefig(folder_path + "//"+title)


log_step("done")
