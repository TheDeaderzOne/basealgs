import math
import cmath
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


#BasicWindingNums

#use 2d dot product

pointlisty = [(-55, 60), (15, 25), (40, 5), (60,-20),(50, -60), (-45, -50)]


def angler(point1,point2,testpoint):
    dumdum = math.remainder(cmath.phase(complex(point2[0]-testpoint[0],point2[1]-testpoint[1]))-cmath.phase(complex(point1[0]-testpoint[0],point1[1]-testpoint[1])),2*math.pi)
    return dumdum


def wind(pointarr,testp):
    angle = 0
    for x in range(len(pointarr)-1):
        angle+=angler(pointarr[x],pointarr[x+1],testp)
    angle += angler(pointarr[-1],pointarr[0],testp)

    return round(angle/(2*math.pi))


print(wind(pointlisty,(0,0)))

def mid(point1,point2):
    return ((point1[0]+point2[0])/2, (point1[1]+point2[1])/2)

def slope(vec1):
    return vec1[1]/vec1[0]

def vectorsubtract(point1,point2):
    return (point1[0]-point2[0],point1[1]-point2[1])

def vectoradd(point1,point2):
    return (point1[0]+point2[0],point1[1]+point2[1])

def crossprod(vec1,vec2):
    return vec1[0]*vec2[1] - vec1[1]*vec2[0]

def vectorscale(scalar,vec):
    return (vec[0]*scalar,vec[1]*scalar)

def veccyswapinv(vec):
    return (-vec[0],-vec[1])



#bad circumcircle alg

def circumcirle(point1,point2,point3):

    veccy1 = vectorsubtract(point2,point1)
    veccy2 = vectorsubtract(point3,point2)
    print(veccy1,veccy2)
    if crossprod(veccy1,veccy2)==0:
        return False
    if slope(veccy1) == 0:
        inv1 = 0
        inv2 = -1/slope(veccy2)
    elif slope(veccy2) == 0:
        inv2 = 0
        inv1 = -1/slope(veccy1)
    else:
        inv1 = -1/slope(veccy1)
        inv2 = -1/slope(veccy2)
    print(inv1)
    firstcons = crossprod((1,inv1),mid(point1,point2))*veccy1[1]*-1
    print(firstcons,mid(point1,point2))
    seccons = crossprod((1,inv2),mid(point3,point2))*veccy2[1]*-1

    factor = crossprod(veccyswapinv(veccy1), veccyswapinv(veccy2))
    turt = vectorscale(firstcons/factor,veccyswapinv(veccy2))

    turt2 = vectorscale(seccons/factor,veccyswapinv(veccy1))

    tec = vectorsubtract(turt,turt2)
    return (tec[1],-tec[0])






def perp(pair):
    return (pair[1],-pair[0])

def square(pair):
    return pair[0]**2 + pair[1]**2

#good circumcircle alg

def circumcircle(a,b,c):
    b = vectorsubtract(b,a)
    c = vectorsubtract(c,a)

    if crossprod(b,c) == 0:
        return "BRUH"
    
    teccy = vectorscale(1/(2*crossprod(b,c)),perp(vectorsubtract(vectorscale(square(c),b),vectorscale(square(b),c))))
    
    return vectorsubtract(a,teccy)


print(circumcircle((0,0),(3,0),(1.5,1.5*math.sqrt(3))))


#Distance to the side

#line = ax+by = c

def sidedistance(a,b,c,point):
    return (crossprod((b,-a),point)-c)/math.sqrt(a**2+b**2)

print(sidedistance(1,2,5,(3,3)))

#orthogonalprojection/reflection

def orthogonalproj(a,b,c,point):

    return vectoradd(point,vectorscale((crossprod((b,-a),point)-c)/(a**2+b**2),perp((b,-a))))

print(orthogonalproj(3,2,5,(3,3)))


