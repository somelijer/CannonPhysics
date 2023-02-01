
import numpy as np
import defs as d
import pygame




def closestDots(objectA,objectB,direction):
    '''
    Smatramo da je direction od smera points A ka points B
    '''
    tackaA = objectA.findFurthestPoint(direction) 
    tackaB = objectB.findFurthestPoint(-direction)
    ret = np.array([tackaA,tackaB])
    return objectA.findFurthestPoint(direction) - objectB.findFurthestPoint(-direction),ret

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
    firstPoint, firstPointsSave = closestDots(objectA,objectB,direction)
    direction = -firstPoint

    secondPoint, secondPointsSave = closestDots(objectA,objectB,direction)
    #logicki ako trazimo u pravcu od tacke do tacke i nije u pravcu koordinatnog pocetka nema kolizije
    if(secondPoint.dot(direction) <= 0):
        return False

    ao = -firstPoint
    ab = secondPoint - firstPoint
    direction = tripleProduct(ab,ao,ab)

    while(True):
        thirdPoint,thirdPointsSave = closestDots(objectA,objectB,direction)
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
            simplex = [firstPoint,secondPoint,thirdPoint]
            normal = EPA(objectA,objectB,simplex)
            if(d.COLISION_OFF == False):
                solveColision(objectA,objectB,normal)
            return True


def EPA(objectA,objectB,simplex):
    minDistance = np.Inf
    minNormal = np.array([0,0])
    minIndex = np.Inf
    while(minDistance == np.Inf):
        for i in range(len(simplex)):
            j = (i+1) % len(simplex)

            pointA = simplex[i]
            pointB = simplex[j]

            oa = pointA

            ab = pointB - pointA

            normal = tripleProduct(ab,oa,ab)
            normal = normal / np.linalg.norm(normal)
            dist = np.dot(normal,pointA)

            if(dist < 0):
                distance *= -1
                normal *= -1

            if(dist < minDistance):
                minDistance = dist
                minNormal = normal
                minIndex = j

        s,savePoints = closestDots(objectA,objectB,minNormal)
        sDistance = np.dot(minNormal,s)

        if(abs(sDistance - minDistance) > 0.001 ):
            minDistance = np.Inf
            simplex.insert(minIndex,s)
    print(savePoints)
    return minNormal

def CircleColisionCheck(circleA,circleB):
    centreA = circleA.getCentre()
    centreB = circleB.getCentre()
    radiusA = circleA.getRadius()
    radiusB = circleB.getRadius()
    if( np.linalg.norm(centreA - centreB) >= radiusA + radiusB ):
        return False

    vector = centreB - centreA
    vlen = np.linalg.norm(vector)

    if vlen != 0:
        vjed = vector / vlen
    else:
        vjed = vector

    if(d.COLISION_OFF == False):
        solveCircleColision(circleA,circleB,vjed )
    return True








def solveCircleColision(circleA,circleB,vjed ):
    mA = circleA.mass
    mB = circleB.mass
    uA = circleA.speed
    uB = circleB.speed

    print(uA,vjed,uA*vjed,np.dot(uA,vjed))

    p =  d.COEF_RESTITUTION * 2 * (np.dot(uA,vjed) - np.dot(uB,vjed)) / (mA + mB)

    circleA.speed = uA - p * mB * vjed
    circleB.speed = uB + p * mA * vjed

def solveColision(objectA,objectB,normal):
    '''
    objectA.speed = normal * np.dot(objectA.speed * -1,normal)
    objectB.speed = normal * np.dot(objectB.speed * -1,normal)
    '''













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

            if(o[i].isCircle() and o[j].isCircle()):
                if(CircleColisionCheck(o[i],o[j])):
                    colObj.append(o[i])
                    colObj.append(o[j])

            if( GJK( o[i],o[j]) ):
                colObj.append(o[i])
                colObj.append(o[j])


    for i in range(len(colObj)):
        colObj[i].colisionColor()

        

    





