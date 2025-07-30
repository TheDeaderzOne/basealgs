import math

#Implement Bellman Ford, Floyd Warshall
numnodes = 5
hx = [(2,3,7),(3,4,2),(0,4,1),(0,3,9),(0,1,5),(1,2,2)]

#lenlist = 9

#BellmanFord

warshallmatrix = []
for x in range(numnodes):
    warshallmatrix.append([math.inf]*numnodes)
    warshallmatrix[x][x]=0

for x in hx:
    warshallmatrix[x[0]][x[1]] = x[2]
    warshallmatrix[x[1]][x[0]] = x[2]

print(warshallmatrix)

def FloydWarshall():
    for num in range(numnodes):
        for x in range(numnodes):
            for y in range(numnodes):
                warshallmatrix[x][y] = min(warshallmatrix[x][y],warshallmatrix[x][num]+warshallmatrix[num][y])
    return warshallmatrix

print(FloydWarshall())


distlist = [math.inf]*numnodes

def BellmanFord(startnode):
    distlist[startnode]=0
    for _ in range(numnodes-1):
        for x in hx:
            distlist[x[1]] = min(distlist[x[1]], x[2]+distlist[x[0]])
            distlist[x[0]] = min(distlist[x[0]], x[2]+distlist[x[1]])
    return distlist

print(BellmanFord(4))

def improvedBellmanFord(startnode):
    distlist[startnode]=0
    active = True
    for _ in range(numnodes-1):
        print(_)
        for x in hx:
            if x[2]+distlist[x[0]]<distlist[x[1]]:
                distlist[x[1]] = x[2]+distlist[x[0]]
                active=False
            if x[2]+distlist[x[1]] < distlist[x[0]]:
                distlist[x[0]] = x[2]+distlist[x[1]]
                active=False
        if active:
            return distlist
    return distlist

print(improvedBellmanFord(4))

edgelist = [[1],[2],[5],[0,4],[1,2],[]]

visitarr = [0]*6
paths = []


def toposort(node):
    visitarr[node]=1
    for x in edgelist[node]:
        if visitarr[x]==0:
            toposort(x)
    paths.append(node)
    return paths

for y in range(len(visitarr)):
    if visitarr[y]==0:
        toposort(y)

paths.reverse()

print(paths)

#Two Types of Binsearch



