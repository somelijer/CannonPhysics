
import numpy as np
import defs as d

def constraint_circle(pos,speed,r):

    #ogranicenja ekrana
    if pos[1] >= (d.HEIGHT - r) / d.PIXEL_PER_METER:
            speed[1] = -speed[1] * d.COEF_RESTITUTION
            pos[1] -= pos[1] -  (d.HEIGHT - r) / d.PIXEL_PER_METER

    elif pos[1] <=   r / d.PIXEL_PER_METER:
            speed[1] = -speed[1] * d.COEF_RESTITUTION
            pos[1] -=  pos[1] - r / d.PIXEL_PER_METER

    if pos[0] >= (d.WIDTH - r) / d.PIXEL_PER_METER:
            speed[0] = -speed[0] * d.COEF_RESTITUTION
            pos[0] -= pos[0] - (d.WIDTH - r) / d.PIXEL_PER_METER

    elif pos[0] <= r / d.PIXEL_PER_METER:
            speed[0] = -speed[0] * d.COEF_RESTITUTION
            pos[0] -= pos[0] - r / d.PIXEL_PER_METER
    

    return pos,speed

def constraint_polygon(pos,speed,points):

    #ogranicenja ekrana
    
    for i in range(len(points)):
        temp = points[i]
        if temp[1] >= d.HEIGHT :
                #speed[1] = -speed[1] * d.COEF_RESTITUTION
                pos[1] -= (temp[1] - d.HEIGHT )/ d.PIXEL_PER_METER
                normal = np.array([0.0,-1.0])
                return pos,points[i],normal,True

        elif temp[1] <=  0:
                #speed[1] = -speed[1]* d.COEF_RESTITUTION
                pos[1] -= (temp[1])/ d.PIXEL_PER_METER
                normal = np.array([0.0,1.0])
                return pos,points[i],normal,True
    
    for i in range(len(points)):
        temp = points[i]
        if temp[0] >= d.WIDTH :
            #speed[0] = -speed[0] * d.COEF_RESTITUTION
            pos[0] -= (temp[1] - d.HEIGHT )/ d.PIXEL_PER_METER
            normal = np.array([-1.0,0.0])
            return pos,points[i],normal,True

        elif temp[0] <= 0:
            #speed[0] = -speed[0] * d.COEF_RESTITUTION
            pos[0] -= (temp[1])/ d.PIXEL_PER_METER 
            normal = np.array([1.0,0.0])
            return pos,points[i],normal,True

    return pos,np.array([-0.0,-0.0]),np.array([0.0,0.0]),False
    








