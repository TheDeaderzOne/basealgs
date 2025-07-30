import heapq
import math

#I understand fenwick, don't wanna get in weeds of implementing


# ogarr = [1,3,4,8,6,1,4,2]

# newarr = [0]*len(ogarr)

# def initializefenwick(arr,oglist):
#     for x in range(len(arr)):
#         if (x+1) & 1 == 1:
#             arr[x] = oglist[x]
#         else:
#             tempvar = (x+1)&((-1*x)-1)
#             ind = (x+1)-tempvar
#             while (tempvar>>1) !=0:
#                 tempvar>>=1
#                 ind+=tempvar
#                 arr[x]+=arr[ind-1]
#             arr[x]+=oglist[x]
#     return arr

# initializefenwick(newarr,ogarr)

# def sumquery(fenwickarr,startind,endind,ogarr):
#     if startind==endind:
#         return ogarr[startind]
    
#     realstartind = startind
#     realendind = endind+1

#     firstsum = 0
#     while realstartind>0:
#         firstsum+=fenwickarr[realstartind-1]
#         realstartind -= (realstartind)&(-1*realstartind)

#     secondsum = 0
#     while realendind>0:
#         secondsum+=fenwickarr[realendind-1]
#         realendind -= (realendind)&(-1*realendind)
    
#     return int(secondsum-firstsum)

# print(sumquery(newarr,1,6,ogarr))

# def add(index,amount,newlist):
#     referencepointer = index+1

#     while referencepointer<=len(newlist):
#         newlist[referencepointer-1]+=amount
#         referencepointer+=(referencepointer)&(-1*referencepointer)

#     return newlist

# print(add(2,7,newarr))

# nodeslist = [[(1,5),(3,9),(4,1)],[0,2],[1,3],[0,2,4],[0,3]]
# distlist = [math.inf]*len(nodeslist)
# visited = [0]*len(nodeslist)
# pq = []
# def Dijkstra(startnode,priorityqueue,distlist,visited,nodelist):
#     distlist[startnode]=0

#     heapq.heappush(priorityqueue,(0,startnode))



#     while len(priorityqueue)>0:
        
#         x = heapq.heappop(priorityqueue)
#         if visited[x[1]]==0:
#             visited[x[1]]=1
#             for h in nodelist[x[1]]:
                
#                 weight = x[0]


        
#                     pass

#         pass

        

#     pass



# distancearr = [math.inf]*9
# eliminated = [0]*9
# pq = []
# adlist = [[],[],[],[],[],[],[],[],[]]
# hx = [[0,1,4],[1,2,8],[2,3,7],[3,4,9],[4,5,10],[5,6,2],[6,7,1],[0,7,8],[3,5,14],[2,5,4],[2,8,2],[6,8,6],[7,8,7],[1,7,11]]

# for x in hx:
#     ind = x[0]
#     ind2 = x[1]
#     ind3 = x[2]
#     adlist[ind].append([ind3,ind2])
#     adlist[ind2].append([ind3,ind])

# def Djikstras(priorqueue,distances,visiteddike,startnode,adjlist):
#     heapq.heappush(priorqueue,(0,startnode))
#     distances[startnode] = 0
#     while len(pq)>0:
#         dist,tempnode = heapq.heappop(pq)
#         if visiteddike[tempnode]==0:
#             visiteddike[tempnode]=1
#             for s in adjlist[tempnode]:
#                 weight = s[0]
#                 snode = s[1]
#                 distances[snode] = min(dist+weight,distances[snode])
#                 heapq.heappush(priorqueue,(distances[snode],snode))
#     return distances

# print(Djikstras(pq,distancearr,eliminated,0,adlist))



#Prims

edgelist=[[(3,1),(5,4)],[(5,2),(6,4)],[(5,1),(9,3),(3,5)],[(9,2),(7,5)],[(5,0),(6,1),(2,5)],[(3,2),(7,3),(2,4)]]

pq = []
visited = [0]*len(edgelist)
distl = [math.inf]*len(edgelist)

def Prims(visit,pq,distlist,startnode,edgearr):
    counter = 0
    heapq.heappush(pq,(0,startnode))

    distlist[startnode]=0

    while len(pq)>0:
        distance,nodes = heapq.heappop(pq)
        
        if visit[nodes]==0:
            counter+=distance
            visit[nodes]=1
            for x in edgearr[nodes]:
                weight = x[0]
                vertex = x[1]
                distlist[vertex]=min(distlist[vertex],weight)
                heapq.heappush(pq,(distlist[vertex],vertex))


    return counter

print(Prims(visited,pq,distl,0,edgelist))






#Union Find






#Tortoise and Hare

# sus = [1,2,3,4,5,4]

# def TortoiseHare(succgraph):
#     tortoise = 0
#     hare = 0

#     tortoise = succgraph[tortoise]
    # hare = succgraph[succgraph[hare]]

    # while tortoise != hare:
    #     tortoise = succgraph[tortoise]
    #     hare = succgraph[succgraph[hare]]

    # print(tortoise)
    
    # hare = 0

    # while tortoise != hare:
    #     tortoise = succgraph[tortoise]
    #     hare = succgraph[succgraph[hare]]
    
    # cycle = []

    # cycle.append(tortoise)

    # tortoise = succgraph[tortoise]

    # while tortoise != hare:
    #     cycle.append(tortoise)
    #     tortoise = succgraph[tortoise]


    # cycle.append(tortoise)

    # return cycle


# print(TortoiseHare(sus))



# parentlist = [int(i) for i in range(5)]
# sizes = [0]*5

# def UFMakeSet(parents,size,v):
#     parents[v]=v
#     size[v]=1

# def UFFindSet(node,parents):
#     if node == parents[node]:
#         return node
#     else:
#         parents[node]=UFFindSet(parents[node],parents)

# def UFUnionSet(element1, element2, parents,sizes):
#     first = UFFindSet(element1,parents)
#     second = UFFindSet(element2,parents)
#     if first!=second:
#         if sizes[second]<sizes[first]:
#             second,first = first,second
#         parents[first]=second
#         sizes[second]+=sizes[first]

# def Connection(node1,node2,parents):
#     if UFFindSet(node1,parents) == UFFindSet(node2,parents):
#         return True
#     return False






parents = [0,1,2,3,4,5]

sizes = [1]*6


edges = [(0,1,3),(1,2,5),(2,3,9),(3,5,7),(0,4,5),(4,5,2),(1,4,6),(2,5,3)]

edges.sort(key=lambda x:x[2])


def DSUFind(parentlist,node):
    if node == parentlist[node]:
        return node
    
    parentlist[node]=DSUFind(parentlist,parentlist[node])

    return parentlist[node]


def DSUUnion(parentlist,node1,node2,size):
    
    gh = int(DSUFind(parentlist,node1))
    gb = int(DSUFind(parentlist,node2))
    
    if gb!=gh:
        if size[gb]>size[gh]:
            size[gb]+=size[gh]
            parentlist[gh]=gb
        else:
            size[gh]+=size[gb]
            parentlist[gb]=gh
    

def DSUConnect(node1,node2,parentlist):
    if DSUFind(parentlist,node1)==DSUFind(parentlist,node2):
        return False
    return True


counter = 0

for j in range(len(edges)):
    if DSUConnect(edges[j][0],edges[j][1],parents):
        counter+=edges[j][2]
        DSUUnion(parents,edges[j][0],edges[j][1],sizes)


print(counter)


print(edges)





directedgraph = [[1],[2],[5],[0,4],[1,2],[]]
visited = [0]*len(directedgraph)
exitarrsy = []

def exittime(visit,edgegraph,startnode,exitarr):
    visit[startnode]=1
    for x in edgegraph[startnode]:
        if visit[x]==0:
            exittime(visit,edgegraph,x,exitarr)
    
    exitarr.append(startnode)



for x in range(len(directedgraph)):
    if visited[x]==0:
        exittime(visited,directedgraph,x,exitarrsy)

exitarrsy.reverse()

print(exitarrsy)




#Strong Connectivity




#Segment Tree




#Ternary Search


def functor(input):
    return input**2+input+1

def TernSearch(bound1,bound2):
    while abs(bound1-bound2)>.00001:

        value1 = functor(bound1)
        value2 = functor(bound2)
        if value2>value1:
            bound2-=(abs(bound1-bound2)/3)
        else:
            bound1+=(abs(bound1-bound2)/3)

    return (bound1,functor(bound1))


print(TernSearch(-10000,1))






#Convex Hull
pointsetreal=[(4,0),(0,2),(-1,-7),(1,10),(2,-3)]

pointset=[(4,0),(0,2),(-1,-7),(1,10),(2,-3)]

#First Step, sort

pointset.sort(key=lambda x:(x[0],-x[1]))
pointsetreal.sort(key=lambda x:(-x[0],x[1]))

print(pointsetreal)

print(pointset)
#second step, take the first two points, then algorithm

def ConvexHull(pointsarr,startnode1,startnode2):
    convexhull=[pointsarr[startnode1],pointsarr[startnode2]]

    for x in range(len(pointsarr)-2):
        if pointsarr[x+2][0]!=convexhull[-1][0]:
            line1 = (convexhull[-1][0]-convexhull[-2][0],convexhull[-1][1]-convexhull[-2][1])
            line2 = (pointsarr[x+2][0]-convexhull[-1][0],pointsarr[x+2][1]-convexhull[-1][1])

            crossproduct = (line1[0]*line2[1])-(line1[1]*line2[0])

            if crossproduct>=0:
                
                convexhull[-1]=pointsarr[x+2]

                while len(convexhull)>2:
                    line1 = (convexhull[-2][0]-convexhull[-3][0],convexhull[-2][1]-convexhull[-3][1])
                    line2 = (convexhull[-1][0]-convexhull[-2][0],convexhull[-1][1]-convexhull[-2][1])

                    crossproduct = (line1[0]*line2[1])-(line1[1]*line2[0])
                    if crossproduct>=0:
                        convexhull.pop(-2)
                    else:
                        break
            else:
                convexhull.append(pointsarr[x+2])

    return convexhull

upperhull = ConvexHull(pointset,0,1)

lowerhull = ConvexHull(pointsetreal,0,1)

lowerhull.pop(0)
lowerhull.pop(-1)

upperhull.extend(lowerhull)

print(upperhull)




#





#Flows (Edmonds-Karp) 

aglist = []
numbernodes = 6
edgeweightlist = [(0,1,5),(1,2,6),(2,5,5),(4,5,2),(2,4,8),(0,3,4),(3,1,3),(3,4,1)]
dumlist = []
edgelenmatrix = []

for _ in range(numbernodes):
    aglist.append([])
    dumlist.append([])
    edgelenmatrix.append([0]*numbernodes)

for line in edgeweightlist:
    aglist[line[0]].append(line[1])
    dumlist[line[1]].append(line[0])
    edgelenmatrix[line[0]][line[1]]=line[2]
    edgelenmatrix[line[1]][line[0]]=0

huqueue = []
recorder = []
visiters = [0]*numbernodes

def EdmondsKarp(startnode,sink,adjarr,recordlist,visit,q,edgemat):
    #currentnode,weight,parentnode
    q.append((startnode,-1))
    visit[startnode]=1
    while len(q)>0:
        for x in adjarr[q[0][0]]:
            if visit[x]==0 and edgemat[q[0][0]][x] > 0:
                q.append((x,q[0][0]))
                visit[x]=1
        jute = q.pop(0)
        recordlist.append(jute)
        if jute[0]==sink:
            break

    if len(recordlist)==1:
        return 0

    edgearron = []

    key = recordlist.pop()
    temph = math.inf
    while len(recordlist)>0:
        newcomp = recordlist.pop()
        if key[1]==newcomp[0]:
            temph = min(temph,edgemat[newcomp[0]][key[0]])
            edgearron.append([newcomp[0],key[0]])
            key = newcomp

    for x in edgearron:
        edgemat[x[0]][x[1]]-=temph
        edgemat[x[1]][x[0]]+=temph
    
    return edgemat

sinknode = 5
startnod = 0

yuh = 0
while yuh == 0:
    ji = EdmondsKarp(startnod,sinknode,aglist,recorder,visiters,huqueue,edgelenmatrix)
    huque = []
    visiters = [0]*numbernodes
    recorder = []
    if ji == 0:
        break

maxflow = 0

for x in dumlist[sinknode]:
    maxflow+=edgelenmatrix[sinknode][x]

print(maxflow)

print(edgelenmatrix)




#Euler Tours



#Sweep Line

neighborarr = [[1, 2, 3, 4], [0,5], [0], [0,6,7,8], [0],[1],[3],[3],[3]]
weightarr = [2,3,5,3,1,4,4,3,1]
start = [0]*9
end = [0]*9
moves = 0 
lissy = []
nodevalues = []
subtreelen = []
def EulerTour(node1,node2):
    global moves
    lissy.append(node1)
    nodevalues.append(weightarr[node1])
    start[node1] = moves
    moves+=1
    for x in neighborarr[node1]:
        if x!=node2:
            EulerTour(x,node1)
    end[node1]=moves
    
    return 0

EulerTour(0,'b')

for x in lissy:
    subtreelen.append(end[x]-start[x])
print(lissy)
print(subtreelen)


originalarraylist = [1,3,4,8,6,1,4,2]


def SegmentTreeBuilder():
    segmenttree = [0]*(len(originalarraylist)*2)
    for x in range(len(originalarraylist)):
        segmenttree[x+len(originalarraylist)]=originalarraylist[x]
    
    for k in range(len(originalarraylist)-1,0,-1):
        segmenttree[k]=max(segmenttree[2*k],segmenttree[2*k+1])

    

    return segmenttree
gex = SegmentTreeBuilder()

def SegmentTreeChecker(index1,index2):
    maxy = 0
    index1+=(len(originalarraylist))
    index2+=(len(originalarraylist))
    while index1<=index2:

        if index1&1==1:
            maxy = max(maxy, gex[index1])
            index1+=1
        
        if index2&1==0:
            maxy = max(maxy, gex[index2])
            index2-=1

        index1//=2
        index2//=2
    
    return maxy

# print(gex)


def SegmentTreeAdjuster(index,changednumber):
    index+=len(originalarraylist)
    gex[index]=changednumber
    index//=2
    while index>0:
        gex[index]=max(gex[2*index],gex[2*index+1])
        index//=2

    return gex
    
# print(SegmentTreeAdjuster(3,4))
