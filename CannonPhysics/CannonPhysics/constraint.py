
import numpy as np
import defs as d
import pygame

def constraint_circle(pos,speed,r):

    #ogranicenja ekrana
    if pos[1] >= (d.HEIGHT - r) / d.PIXEL_PER_METER:
            speed[1] = -speed[1] 

    elif pos[1] <=   r / d.PIXEL_PER_METER:
            speed[1] = -speed[1]

    if pos[0] >= (d.WIDTH - r) / d.PIXEL_PER_METER:
            speed[0] = -speed[0] 

    elif pos[0] <= r / d.PIXEL_PER_METER:
            speed[0] = -speed[0]
    

    return pos,speed

def constraint_polygon(pos,speed,points):

    #ogranicenja ekrana
    
    for i in range(len(points)):
        temp = points[i]
        if temp[1] >= d.HEIGHT :
                speed[1] = -speed[1] 
                break;
        elif temp[1] <=  0:
                speed[1] = -speed[1]
                break;
    
    for i in range(len(points)):
        temp = points[i]
        if temp[0] >= d.WIDTH :
            speed[0] = -speed[0] 
            break;

        elif temp[0] <= 0:
            speed[0] = -speed[0]
            break;

    

    return pos,speed







