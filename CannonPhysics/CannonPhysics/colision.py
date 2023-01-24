from re import A
import numpy as np
import defs as d
import pygame

def findFurthestPoint(d,points):
    maxPoint = np.array([0,0])
    maxDist = -np.inf

    for i in range(len(points)):
        dist = np.dot(points[i],d)
        if(dist > maxDist):
            maxDist = dist
            maxPoint = points[i]

    return maxPoint

def closestDots(pointsA,pointsB,direction):
    '''
    Smatramo da je direction od smera points A ka points B
    '''
    return findFurthestPoint(direction,pointsA) - findFurthestPoint(-direction,pointsB)

def sameDirection(vector,direction):
    if(np.dot(direction,vector) > 0):
        return True
    else:
        return False

def tripleProduct(a,b,c):
    a = np.append(a,0)
    b = np.append(b,0)
    c = np.append(c,0)
    res = np.cross(np.cross(a,b),c)
    return np.array([res[0],res[1]])








def GJK(pointsA,pointsB,centreA,centreB):
    #predstavlja prvu tacku pretrazivanja za simplex
    direction = centreB - centreA
    firstPoint = closestDots(pointsA,pointsB,direction)
    direction = -firstPoint

    secondPoint = closestDots(pointsA,pointsB,direction)
    #logicki ako trazimo u pravcu od tacke do tacke i nije u pravcu koordinatnog pocetka nema kolizije
    if(secondPoint.dot(direction) <= 0):
        return False

    ao = -firstPoint
    ab = secondPoint - firstPoint
    direction = tripleProduct(ab,ao,ab)

    while(True):
        thirdPoint = closestDots(pointsA,pointsB,direction)
        #logicki ako trazimo u pravcu od tacke do tacke i nije u pravcu koordinatnog pocetka nema kolizije
        if(thirdPoint.dot(direction) <= 0):
            return False

        co = -thirdPoint
        cb = secondPoint - thirdPoint
        ca = firstPoint - thirdPoint


        
        cbPerp = tripleProduct(ca,cb,cb)
        caPerp = tripleProduct(cb,ca,ca)

        if(np.dot(caPerp , co) > 0):
            secondPoint = thirdPoint
            direction = caPerp
        elif(np.dot(cbPerp,co) > 0):
            firstPoint = thirdPoint
            direction = cbPerp
        else:
            return True



        

    





