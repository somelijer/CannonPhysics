
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

    def info():
        pass

    def getCentre(self):
        pass

    def findFurthestPoint(self,d):
        pass

class Circle(GameObject):
    
    def __init__(self, X, Y , r):
        self.t = 0
        self.r = r
        self.color = (0, 120, 120)

        self.mass = d.OBJECTS_DENSITY * r**2 * np.pi / (d.PIXEL_PER_METER**2)
        self.drag = np.pi * (r/d.PIXEL_PER_METER)**2 * 0.47

        self.pos = np.array([X/d.PIXEL_PER_METER,Y/d.PIXEL_PER_METER])
        self.speed = np.array([10.0,-10.0])
        self.force = np.array([0.0,0.0])

    def move(self,screen,deltaTime):
        #racunamo sledecu poziciju sa svim
        self.pos , self.speed = phy.physics_step(self.mass,self.pos,self.speed,self.force,self.drag,deltaTime)

        #constraint
        self.pos , self.speed = con.constraint_circle(self.pos,self.speed,self.r)
        pygame.draw.circle(screen, self.color, self.pos * d.PIXEL_PER_METER ,self.r )
        

    def addForce(self, fx,fy):
        self.force = np.array([fx,fy])

    def getCentre(self):
        return self.pos * d.PIXEL_PER_METER

    def info():
        pass

    def findFurthestPoint(self,d):
        maxPoint = np.array([0,0])
        djed = d / np.linalg.norm(d)
        maxPoint = self.getCentre() + djed * self.r 
        
        return maxPoint

    def colisionColor(self):
        self.color = (255, 0, 0)

    def sweepColor(self):
        self.color = (120, 0, 0)

    def normalColor(self):
        self.color = (0, 0, 255)  



class Rectangle(GameObject):
    
    def __init__(self, X, Y , a , b , angle):
        self.t = 0
        self.a = a
        self.b = b
        self.color = (0, 0, 255)

        self.mass = d.OBJECTS_DENSITY * a * b / (d.PIXEL_PER_METER**2) 
        self.momentInertia = a*b
        self.drag = (a**2)/(d.PIXEL_PER_METER**2) + (b**2)/(d.PIXEL_PER_METER**2) * 1.05


        self.angle = angle
        self.rotSpeed = 0.5
        
        self.pos = np.array([X/d.PIXEL_PER_METER,Y/d.PIXEL_PER_METER])
        self.speed = np.array([0.0,-10.0])
        self.force = np.array([0.0,0.0])
        self.momentForce = self.momentInertia * 0
        #cuvano u pikselima a ne metrima
        XX = X  * d.PIXEL_PER_METER  - ( a * np.sin(self.angle) + b * np.cos(-self.angle) ) / 2
        YY = Y * d.PIXEL_PER_METER - ( a * np.cos(self.angle) + b * np.sin(-self.angle) )/ 2
        self.points = np.array([( XX  , YY  ),
                                ( XX   + a * np.sin(self.angle) , YY  + a * np.cos(self.angle)),
                                ( XX   + a * np.sin(self.angle) + b * np.cos(-self.angle), YY   + a * np.cos(self.angle) + b * np.sin(-self.angle) ),
                                ( XX   + b * np.cos(-self.angle) , YY  + b * np.sin(-self.angle) )
                                ])

    def move(self,screen,deltaTime):
        #racunamo sledecu poziciju sa svim
        self.pos , self.speed = phy.physics_step(self.mass,self.pos,self.speed,self.force,self.drag,deltaTime)
        self.angle , self.rotSpeed = phy.physics_step_rotation(self.angle,self.rotSpeed,self.momentInertia,self.momentForce,deltaTime)
        
        #update svih coskova
        a = self.a
        b = self.b
        XX = self.pos[0]  * d.PIXEL_PER_METER  - ( a * np.sin(self.angle) + b * np.cos(-self.angle) ) / 2
        YY = self.pos[1] * d.PIXEL_PER_METER - ( a * np.cos(self.angle) + b * np.sin(-self.angle) )/ 2
        self.points = np.array([( XX  , YY  ),
                                ( XX   + a * np.sin(self.angle) , YY  + a * np.cos(self.angle)),
                                ( XX   + a * np.sin(self.angle) + b * np.cos(-self.angle), YY   + a * np.cos(self.angle) + b * np.sin(-self.angle) ),
                                ( XX   + b * np.cos(-self.angle) , YY  + b * np.sin(-self.angle) )
                                ])
        #constraint
        self.pos , self.speed = con.constraint_polygon(self.pos,self.speed,self.points)
        pygame.draw.polygon(screen,self.color, self.points  ,0 )

    def colisionColor(self):
        self.color = (255, 0, 0)

    def sweepColor(self):
        self.color = (120, 0, 0)

    def normalColor(self):
        self.color = (0, 0, 255)  

    def addForce(self, fx,fy):
        self.force = np.array([fx,fy])

    def getCentre(self):
        return self.pos * d.PIXEL_PER_METER

    def findFurthestPoint(self,d):
        points = self.points
        maxPoint = np.array([0,0])
        maxDist = -np.inf

        for i in range(len(points)):
            dist = np.dot(points[i],d)
            if(dist > maxDist):
                maxDist = dist
                maxPoint = points[i]

        return maxPoint

    
        




