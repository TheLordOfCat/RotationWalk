import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import *
import math

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

def proces_point_stable(xS, yS, next_level, r, boundry, x_points, y_points, angles_rad, marked):
    for a in angles_rad:
        x = math.cos(a)*r + xS
        y = math.sin(a)*r + yS
        
        x = round(x,2)
        y = round(y,2)
        
        if -1 * boundry <= x and x <= boundry and -1 * boundry <= y and y <= boundry:
            if not ((x,y) in marked):
                x_points.append(x)
                y_points.append(y)
                next_level.append((x,y))
                marked.add((x,y))
            
def process_level_stable(parent_level, levels, r, boundry, x_points, y_points, angles_rad, marked):
    next_level = []

    for i in range(0, len(levels[parent_level])):
        proces_point_stable(levels[parent_level][i][0], levels[parent_level][i][1], next_level, r, boundry, x_points, y_points, angles_rad, marked)
    
    levels.append(next_level)

def proces_point_dynamic(xS, yS, next_level, r, boundry, x_points, y_points, angles_rad):
    for a in angles_rad:
        x = math.cos(a)*r + xS
        y = math.sin(a)*r + yS

        x = round(x,2)
        y = round(y,2)
        
        if -1 * boundry <= x and x <= boundry and -1 * boundry <= y and y <= boundry:
            x_points.append(x)
            y_points.append(y)
            next_level.append((x,y))
            
def process_level_dynamic(parent_level, levels, r, boundry, x_points, y_points, angles_rad):
    next_level = []

    for i in range(0, len(levels[parent_level])):
        proces_point_dynamic(levels[parent_level][i][0], levels[parent_level][i][1], next_level, r, boundry, x_points, y_points, angles_rad)
    
    levels.append(next_level)