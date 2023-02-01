import defs as d
import gameObject as go
import numpy as np

def testCircleOnCircle():
    objects = []
    for i in range(1,4):
        circle = go.Circle(d.WIDTH / 2 + 10*i ,d.HEIGHT * i/ 5 ,i*10)
        objects.append(circle)
    

    return objects

def testCircleOnCircle2():
    objects = []
    for i in range(2,4):
        circle = go.Circle(d.WIDTH / 2 + 10*i ,d.HEIGHT * i/ 5 ,i*3*i*i)
        objects.append(circle)
    

    return objects

def testSquareAndCircles():
    objects = []
    for i in range(1,4,2):
        circle = go.Circle(d.WIDTH / 2 ,d.HEIGHT * i/ 5 ,i*10)
        objects.append(circle)
    
    i = 2
    reck2 = go.Rectangle(d.WIDTH / 2  ,d.HEIGHT /2,20 * i,20 * i, np.pi / 4)
    reck2.setSpeed(0.0,-10.0)
    objects.append(reck2)

    return objects


def testSquares():
    objects = []
    for i in range(1,4):
        if(i%2 == 1):
            reck2 = go.Rectangle(d.WIDTH / 2  ,d.HEIGHT *i/5,20 * i,20 * i, np.pi / 4)
            reck2.setSpeed(0.0,-10.0)
        else:
            reck2 = go.Rectangle(d.WIDTH / 2  ,d.HEIGHT *i/5,20 * i,20 * i,0)
        objects.append(reck2)

    return objects

def testSquares2():
    objects = []
    for i in range(1,4):
        reck2 = go.Rectangle(d.WIDTH / 2  ,d.HEIGHT *i/5,20 * i,20 * i,0)
        if(i%2 == 1):
            reck2.setSpeed(0.0,-10.0)
        objects.append(reck2)

    return objects

def testStaticCirclesOnGround():
    objects = []
    for i in range(1,4):
        circle = go.Circle(d.WIDTH * i / 6 ,d.HEIGHT - i*10,i*10)
        objects.append(circle)
    
    for i in range(1,4):
        reck2 = go.Rectangle(d.WIDTH * i / 6  ,d.HEIGHT /6,40 * i,20 * i, np.pi * (i-1)/3)
        objects.append(reck2)

    return objects

def testCannon():
    objects = []

    circle = go.Circle(20 ,d.HEIGHT - 20,20)
    circle.setSpeed(17.0,-17.0)
    objects.append(circle)
    
    h = 60
    reck2 = go.Rectangle(d.WIDTH * 7/ 8  ,d.HEIGHT - h,h * 2,20 * 2, 0)
    objects.append(reck2)

    h = 100
    reck2 = go.Rectangle(d.WIDTH * 6/ 8  ,d.HEIGHT - h,h * 2,20 * 2, 0)
    objects.append(reck2)
    
    return objects

def testCannon():
    objects = []

    circle = go.Circle(20 ,d.HEIGHT - 20,20)
    circle.setSpeed(17.0,-17.0)
    objects.append(circle)
    
    h = 60
    reck2 = go.Rectangle(d.WIDTH * 7/ 8  ,d.HEIGHT - h,h * 2,20 * 2, 0)
    objects.append(reck2)

    h = 100
    reck2 = go.Rectangle(d.WIDTH * 6/ 8  ,d.HEIGHT - h,h * 2,20 * 2, 0)
    objects.append(reck2)
    
    return objects