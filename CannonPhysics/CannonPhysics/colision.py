
import numpy as np
import defs as d
import pygame


def closestDots(objectA,objectB,direction):
    '''
    Smatramo da je direction od smera points A ka points B
    '''
    return objectA.findFurthestPoint(direction) - objectB.findFurthestPoint(-direction)

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








def GJK(objectA,objectB):
    #predstavlja prvu tacku pretrazivanja za simplex
    centreA = objectA.getCentre()
    centreB = objectB.getCentre()
    direction = centreB - centreA
    firstPoint = closestDots(objectA,objectB,direction)
    direction = -firstPoint

    secondPoint = closestDots(objectA,objectB,direction)
    #logicki ako trazimo u pravcu od tacke do tacke i nije u pravcu koordinatnog pocetka nema kolizije
    if(secondPoint.dot(direction) <= 0):
        return False

    ao = -firstPoint
    ab = secondPoint - firstPoint
    direction = tripleProduct(ab,ao,ab)

    while(True):
        thirdPoint = closestDots(objectA,objectB,direction)
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

def sweepAndPrune(o):
    #sortiramo po x osi
    for i in range(len(i)):
        pass


def colisionCheckClassic(o):
    #sortiramo po x osi
    colObj  = []
    for i in range(len(o)):
        o[i].normalColor()
        for j in range(i+1,len(o)):
            o[j].normalColor()
            if( GJK( o[i],o[j]) ):
                colObj.append(o[i])
                colObj.append(o[j])


    for i in range(len(colObj)):
        colObj[i].colisionColor()

        

    





