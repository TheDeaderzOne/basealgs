import math
import random

#Closest Pair of Points, O(NlogN) solution time

#Uses Sweep Line, where it sorts all the points, then goes from left to right, adding them to the set once they are processed

#The set is kept such that if the x value is larger than the current minimum distance, it is removed in O(logN) time via set discard

#Each time, the points in the set are used to calculate minimum distance once the bad ones are removed

pointar = []

for _ in range(1000):
    pointar.append((random.randint(-100000,100000),random.randint(-100000,100000)))

pointar.sort()

def euclideandist(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def ClosestPairPoints(pointarr):
    mindist = math.inf; movingpointer = 0
    prevpoints = set(); prevpoints.add(pointarr[0])

    for i in range(1,len(pointarr),1):

        while pointarr[i][0]-pointarr[movingpointer][0]>mindist:
            set.discard(prevpoints,pointarr[movingpointer])
            movingpointer+=1

        for j in prevpoints:
            if pointarr[i][1]-mindist <= j[1] <= pointarr[i][1]+mindist:
                mindist = min(mindist,euclideandist(j,pointarr[i]))

        set.add(prevpoints, pointarr[i])

    return mindist

print(ClosestPairPoints(pointar))
# Sweep Line, line segments