import sys
import math
import random
pointlist = [(76,89),(760,684)]

def ExampleCrossProduct(Point1,Point2):
    if (Point1[0]*Point2[1])-(Point1[1]*Point2[0]) > 0:
        return "Left"
    elif (Point1[0]*Point2[1])-(Point1[1]*Point2[0]) == 0:
        return "Straight"
    else:
        return "Right"
    
def LinePointDirection():
    pass

def TriangleAreaCross():
    pass


def InsidePoly():
    pass

def LineIntersection():
    pass

def ShortestPointtoLineDistance():
    pass


#find shortest dist each time

print(ExampleCrossProduct(pointlist[0],pointlist[1]))


#Sweep Line (Full Knowledge)


#Convex Hull


geometergraph = [(-10, 20), (30, -40), (15, 25), (-25, -35), (40, 5), (-5, -10), (20, -30), (-35, 45), (50, -60), (-55, 60), (5, 15), (-20, -25), (30, 10), (-45, -50), (25, -5)]

def CrossProduct(pointlist1,pointlist2):
    crossdirection = (pointlist1[0]*pointlist2[1])-(pointlist1[1]*pointlist2[0])

    if crossdirection>0:
        return 1
    elif crossdirection == 0:
        return 0
    else:
        return -1


def ConvexHull(shape,topstate):

    if topstate == True:
        modifier = 1
    else:
        modifier = -1

    shape.sort()
    shapelist = []
    shapelist.append(shape[0])

    for yex in range(1,len(shape)):
        if len(shapelist)==1:
            shapelist.append(shape[yex])
        else:
            shapelist.append(shape[yex])
            pointchecker = CrossProduct((shapelist[-1][0]-shapelist[-3][0],shapelist[-1][1]-shapelist[-3][1]),(shapelist[-1][0]-shapelist[-2][0],shapelist[-1][1]-shapelist[-2][1]))*modifier

            while pointchecker == 1:
                shapelist.pop(-2)
                if len(shapelist)>2:
                    pointchecker = CrossProduct((shapelist[-1][0]-shapelist[-3][0],shapelist[-1][1]-shapelist[-3][1]),(shapelist[-1][0]-shapelist[-2][0],shapelist[-1][1]-shapelist[-2][1]))*modifier
                else:
                    break
    return shapelist

hu = ConvexHull(geometergraph,True)
jk = ConvexHull(geometergraph,False)
if len(jk)>2:
    hu.extend(reversed(ConvexHull(geometergraph,False)[1:len(jk)-1]))
    ConvexHullTotal = list(hu)
else:
    ConvexHullTotal = list(hu)
print(ConvexHullTotal)

#Sweep Line

#ClosestPairPoints

#Lol line sweep takes advantage of the fact that set works in log n to search up elemtns 

# print(ClosestPairPoints(pointar))

#Line Intersections

def crossproductlineinter(line1,line2):
    pass

def LineIntersections(linesegmentarr):
    pass

#Union of Area Rectangles

#LCA