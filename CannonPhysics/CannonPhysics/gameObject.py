
import numpy as np
import pygame 
import physics as phy
import constraint as con
import defs as d

class GameObject():

    def addForce(self,f):
        pass
    
    def move(self,screen,deltaTime):
        pass

class Circle(GameObject):
    
    def __init__(self, X, Y , r):
        self.t = 0
        self.r = r
        self.mass = 1 * r * np.pi
        self.pos = np.array([X/d.PIXEL_PER_METER,Y/d.PIXEL_PER_METER])
        self.speed = np.array([20.0,20.0])
        self.drag = np.pi * (r/d.PIXEL_PER_METER)**2 * 0.47
        self.force = np.array([0.0,0.0])

    def move(self,screen,deltaTime):
        #racunamo sledecu poziciju sa svim
        self.pos , self.speed = phy.physics_step(self.mass,self.pos,self.speed,self.force,self.drag,deltaTime)

        #constraint
        self.pos , self.speed = con.constraint_circle(self.pos,self.speed,self.r)
        pygame.draw.circle(screen, (0, 0, 255), self.pos * d.PIXEL_PER_METER ,self.r )
        

    def addForce(self, fx,fy):
        self.force = np.array([fx,fy])
        




