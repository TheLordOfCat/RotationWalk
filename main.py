import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import *
import math

######### Arguments #########

r = 1
angle = 60 #in degrees <0,360>
totalLevels = 3  # >= 1
boundry = 5

#############################

def get_angles(change):
    curAngle = change
    MOD = 360
    ans = []
    while curAngle != 0:
        ans.append(curAngle)
        curAngle = (curAngle + change)%MOD
    ans.append(0)
    return ans

def convert_degree_to_rad(ang):
    ans = []
    for a in ang:
        ans.append(np.radians(a))
    return ans

def get_aproximation(numberOfTurns, level):
    totalPoints = 1
    curPoints = 1
    for i in range(2, level+1):
        curPoints *= numberOfTurns
        totalPoints += curPoints
    return totalPoints

levels = [[(0,0)]]

x_points = [0]
y_points = [0]

def proces_point(xS, yS, next_level):
    global x_points, y_points, boundry, angles_rad

    for a in angles_rad:
        x = math.cos(a)*r + xS
        y = math.sin(a)*r + yS
        
        if -1 * boundry <= x and x <= boundry and -1 * boundry <= y and y <= boundry:
            x_points.append(x)
            y_points.append(y)
            next_level.append((x,y))
            

def process_level(parent_level):
    next_level = []

    for i in range(0, len(levels[parent_level])):
        proces_point(levels[parent_level][i][0], levels[parent_level][i][1], next_level)
    
    levels.append(next_level)

print("### Symulating Rotational Walk ###")
print("1) getting number of rotations")
angles_degree = get_angles(angle)
angles_rad = convert_degree_to_rad(angles_degree)

print("2) approximating number of points")
approx_number_of_points = get_aproximation(len(angles_degree), totalLevels)
print("Approximated number of points = " + str(approx_number_of_points))
proceed = input("Do you wish to proceed Y/n?")

if proceed == "Y":
    print("3) getting points")

    print("4) plotting points")
    fig, ax = plt.subplots(figsize = (10,10))

    for i in range(1, totalLevels):
        process_level(i-1)

    ax.plot(x_points, y_points, 'ko')
    plt.show()
    print("5) done")
else:
    print("3) done")
