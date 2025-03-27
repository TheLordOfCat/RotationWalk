import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import *
import math
import rotation_walk as rw
import os

######### Arguments #########

r = 1
angle = 75 #in degrees <0,360>
totalLevels = 4  # >= 1
boundry = 10
folder_path = ''

#############################
step = 1

def log_step(message):
    global step
    print(str(step) + ") " + message)
    step += 1

levels = [[(0,0)]]

x_points = [0]
y_points = [0]

def process_level(parent_level):
    next_level = []

    for i in range(0, len(levels[parent_level])):
        rw.proces_point(levels[parent_level][i][0], levels[parent_level][i][1], next_level, r, boundry, x_points, y_points, angles_rad)
    
    levels.append(next_level)

print("### Symulating Rotational Walk ###")
log_step("getting number of rotations")

angles_degree = rw.get_angles(angle)
angles_rad = rw.convert_degree_to_rad(angles_degree)

log_step("approximating number of points")
approx_number_of_points = 0
for i in range(1, totalLevels+1):
    approx_number_of_points += rw.get_aproximation(len(angles_degree), totalLevels)

print("Approximated number of points = " + str(approx_number_of_points))
proceed = input("Do you wish to proceed Y/n?")

if proceed == "Y":
    log_step("creating folder")
    folder_path = os.path.join(folder_path, "sekwencja - " + str(angle) + "katna, " + str(i) + " poziomowa")

    if not os.path.exists(folder_path):
        # Create the directory (including any necessary parent directories)
        os.makedirs(folder_path)

    fig, ax = plt.subplots(figsize = (10,10))
    for i in range(1, totalLevels+1):
        log_step("processing level number - " + str(i))
        log_step("adding points")

        process_level(i-1)

        log_step("plotting points")

        title = "Spacer-" + str(angle) + "katny," + str(i) + "poziomowy.png"
        fig.suptitle(title, fontsize=8) 

        ax.plot(x_points, y_points, 'ko')
        fig.savefig(folder_path + "//"+title)


log_step("done")
