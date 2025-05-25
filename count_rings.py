import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import *
import math
import rotation_walk as rw
import os
from collections import Counter

######## Description ########
#Symulates rotation walk.
#Stars a the the first level, creates each level up to total_levels.
#Then assigns each point to a rings by distance to the (0, 0).
######### Arguments #########

r = 10
boundry = 2000000000
angles = [45]
angles_colors = ['b','r', 'g'] 
total_levels = 4
figure_side_size = 10
folder_path = "points_charts"

#############################

step = 1

def distAB(pointA_x, pointA_y, pointB_x, pointB_y):
    dist = math.sqrt((pointB_x-pointA_x)**2 + (pointB_y-pointA_y)**2)
    dist = round(dist,2)
    return dist

def log_step(message):
    global step
    print(str(step) + ") " + message)
    step += 1

log_step("## symulating number of rings ##")
log_step("iterating through angles")
for a in angles:
    fig, ax = plt.subplots(figsize = (figure_side_size, figure_side_size))

    log_step("iterating through angle")

    angles_degree = rw.get_angles(a)
    angles_rad = rw.convert_degree_to_rad(angles_degree)

    levels = [[(0,0)]]
    number_points = []
    sum_points = []

    levels_x = [[0]]
    levels_y = [[0]]

    marked = {(0,0)}

    log_step("getting points")
    for i in range(1, total_levels+1):
        levels_x.append([])
        levels_y.append([])
        rw.process_level_stable(i-1, levels, r, boundry, levels_x[-1], levels_y[-1], angles_rad, marked)

    log_step("counting rings")
    rings = Counter()

    for i in range(0, len(levels)):
        for j in range(0, len(levels_x[i])):
            d = distAB(0, 0, levels_x[i][j], levels_y[i][j])
            rings[d] += 1
    
    rings_list = rings.items()
    sorted_rings_list = sorted(rings_list, key=lambda x:x[0])

    print("----------------" + str(a) + "----------------")
    print("Number of rings: " + str(len(sorted_rings_list)))
    rings_sizes = []
    rings_index = []
    for i in range(0, len(sorted_rings_list)):
        print(sorted_rings_list[i][1], end= " ")
        rings_index.append(i)
        rings_sizes.append(sorted_rings_list[i][1])
    
    # ax.plot(rings_index, rings_sizes, 'ko', label=str(a) + " points by ring", markersize = 1)

    # plt.show()
        
