
import numpy as np
import defs as d
import pygame

def constraint_circle(pos,speed,r):

    #ogranicenja ekrana
    if pos[1] >= (d.HEIGHT - r) / d.PIXEL_PER_METER:
            speed[1] = -speed[1] 

    if pos[1] <=   r / d.PIXEL_PER_METER:
            speed[1] = -speed[1]

    if pos[0] >= (d.WIDTH - r) / d.PIXEL_PER_METER:
            speed[0] = -speed[0] 

    if pos[0] <= r / d.PIXEL_PER_METER:
            speed[0] = -speed[0]
    

    return pos,speed







