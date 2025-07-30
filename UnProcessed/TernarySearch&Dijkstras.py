import sys
import heapq
import math

numbernodes = 5
nodepaths = [[0,1,7],[0,2,3],[1,2,1],[1,3,2],[1,4,6],[3,4,4],[2,3,2]]
mindistance = [math.inf]*numbernodes
visited = [0]*numbernodes
priorityqueue = []
adjarr = []
for _ in range(numbernodes):
    adjarr.append([])

for x in nodepaths:
    adjarr[x[0]].append([x[1],x[2]])
    adjarr[x[1]].append([x[0],x[2]])
print(adjarr)
def Dijkstras(pq,visit,startnode,adjlist,mindistarr):
    heapq.heappush(pq,(0,startnode))
    mindistarr[startnode]=0
    while len(pq)>0:
        distance,nodenum = heapq.heappop(pq)
        if visit[nodenum]==0:
            visit[nodenum] = 1
            for x in adjlist[nodenum]:
                tempnode = x[0]
                edgedist = x[1]
                if mindistarr[tempnode]>distance+edgedist:
                    mindistarr[tempnode]= distance+edgedist
                    heapq.heappush(pq,(mindistarr[tempnode],tempnode))
                    print(pq)
                
    return mindistarr

# print(Dijkstras(priorityqueue,visited,0,adjarr,mindistance))


def PrimsMST(PQ,visit,distlist,startnode,adjarr):
    totaldist = 0
    heapq.heappush(PQ,(0,startnode))
    distlist[startnode]=0
    while len(PQ)>0:
        nodedist,node = heapq.heappop(PQ)
        if visit[node] == 0:
            visit[node]=1
            totaldist+=distlist[node]
            for x in adjarr[node]:
                tempnode = x[0]
                tempdist = x[1]
                if distlist[tempnode]>(tempdist):
                    distlist[tempnode] = tempdist
                    heapq.heappush(PQ,(distlist[tempnode],tempnode))

    return totaldist

def Polynomial(x):
    return 1*(x**2)+(2*x)+1

def TernarySearch(lowerlimit,upperlimit):
    while upperlimit - lowerlimit > 10e-9:
        if Polynomial(upperlimit-((upperlimit - lowerlimit)/3))>=Polynomial(lowerlimit+((upperlimit - lowerlimit)/3)):
            upperlimit-=((upperlimit - lowerlimit)/3)
        else:
            lowerlimit+=((upperlimit - lowerlimit)/3)

    return (upperlimit)

print(PrimsMST(priorityqueue,visited,mindistance,0,adjarr))
print(TernarySearch(-1000,1000))


#Union Find



#Do Every Single Linear Algebra CS Topic Possible 

#Putnam Lin Alg




