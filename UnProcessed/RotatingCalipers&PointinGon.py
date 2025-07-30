import math
import random

ConvexHullSet = [[2,1],[5,5],[9,2],[8,-3],[4,-4]]

def listsubtracter(list1,list2):
    return [list1[0]-list2[0],list1[1]-list2[1]]

def euclideandist(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def crossproduct(line1,line2):
    return line1[0]*line2[1] - line1[1]*line2[0]

#Good Rotating Caliper Algorithm
    
def RotateCalip(convexhull):
    basispoint = 0; testing = 1; diameterlen = 0
    length = len(convexhull)

    while basispoint<testing:
        while True:
            diameterlen = max(diameterlen,euclideandist(convexhull[basispoint],convexhull[testing]))
            if crossproduct([convexhull[basispoint+1][0]-convexhull[basispoint][0],convexhull[basispoint+1][1]-convexhull[basispoint][1]],[convexhull[(testing+1)%length][0]-convexhull[testing][0],convexhull[(testing+1)%length][1]-convexhull[testing][1]])>=0:
                break
            testing = (testing+1)%length
        basispoint+=1

    return diameterlen

print(RotateCalip(ConvexHullSet))

#Point in Polygon

point1 = [random.randint(0,5),random.randint(0,5)]
point2 = [random.randint(50,100),random.randint(50,100)]


def PointinPolygon(point,xlim,polygonhull):

    slopegenerator = random.randint(-1000,1000)/5000
    directiondeterminant = random.randint(0,1)

    intersections = 0

    #x limit exists because i can't use math.inf for rays

    if directiondeterminant == 0:
        secondpoint = [point[0]+xlim,point[1]+(xlim*slopegenerator)]
    else:
        secondpoint = [point[0]-xlim,point[1]-(xlim*slopegenerator)]
    
    for x in range(len(polygonhull)):
        if point == polygonhull[x]:
            return 'on polygon'
        pointcomp = crossproduct(listsubtracter(secondpoint,point),listsubtracter(polygonhull[x],secondpoint))
        pointcompalt = crossproduct(listsubtracter(secondpoint,point),listsubtracter(polygonhull[x-1],secondpoint))
        bizarropointcomp = crossproduct(listsubtracter(polygonhull[x],polygonhull[x-1]),listsubtracter(secondpoint,polygonhull[x]))
        bizarropointcomp2 = crossproduct(listsubtracter(polygonhull[x],polygonhull[x-1]),listsubtracter(point,polygonhull[x]))
        
        if pointcomp == 0 or pointcompalt == 0:
            intersections+=.5
        else:
            if pointcomp>0 and pointcompalt<0 and bizarropointcomp<0 and bizarropointcomp2>0:
                intersections+=1
            elif pointcomp<0 and pointcompalt>0 and bizarropointcomp>0 and bizarropointcomp2<0:
                intersections+=1
    
    intersections = int(intersections)
    if intersections&1 == 1:
        return 'inside'
    else:
        return 'outside'

print(PointinPolygon(point1,100000,ConvexHullSet))
