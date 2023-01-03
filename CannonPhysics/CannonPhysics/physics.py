
import numpy as np
from rk4N import rk4N
import defs as d
import pygame

def physics_step(mass,pos,speed,addedForce,drag_const,deltaTime):

    #racunanje gravitacione sile
    fg = np.array([0,mass * d.GRAVITY_ACC])
    
    #racunanje primitivne sile otpora vazduha
    f_drag =  -(1/2) * speed * np.linalg.norm(speed, 2) * d.AIR_RESIS * drag_const

    #racunanje rezultujuce sile
    f_rez = fg + f_drag + addedForce
    
    
    


    
    fx = lambda *args: f_rez[0]/mass 
    fy = lambda *args: f_rez[1]/mass 
    
    ta = 0
    tb = deltaTime
    h = (tb - ta)

    #racunamo po x osi
    v = speed[0]
    x = pos[0]
    nfx0 = np.array([x,v])
    _ , update = rk4N(ta, tb, h,nfx0,fx)
    pos[0] = update[0,-1]
    speed[0] = update[1,-1]

    #racunamo po y osi
    v = speed[1]
    x = pos[1]
    nfx0 = np.array([x,v])
    _ , update = rk4N(ta, tb, h,nfx0,fy)
    print(update,deltaTime)
    pos[1] = update[0,-1]
    speed[1] = update[1,-1]

    return pos,speed







