import sys
import math
import heapq
sys.setrecursionlimit(10**6)
numbernodes = 5
nodepaths = [(2,3,7),(3,4,2),(0,4,1),(0,3,9),(0,1,5),(1,2,2)]
mindistance = [math.inf]*numbernodes
nodevisitedarr = [0]*numbernodes
priorityqueue = []
adjarr = []
for _ in range(numbernodes):
    adjarr.append([])

for x in nodepaths:
    adjarr[x[0]].append([x[1],x[2]])
    adjarr[x[1]].append([x[0],x[2]])


def Dijkstras(pq,distancearr,adjlist,startnode,visited):
    heapq.heappush(pq,(startnode,0))
    distancearr[startnode]=0
    while len(pq)>0:
        node,dist = heapq.heappop(pq)
        if visited[node] == 0:
            visited[node]=1
            for x in adjlist[node]:
                nodenumber = x[0]
                tempdist = x[1]
                distancearr[nodenumber]=min(distancearr[nodenumber],tempdist+dist)
                heapq.heappush(pq,(nodenumber,distancearr[nodenumber]))
    return distancearr     


print(Dijkstras(priorityqueue,mindistance,adjarr,0,nodevisitedarr))

def PrimsMST(pq,adjlist,startnode,visited):
    pq = []
    visited = [0]*numbernodes
    heapq.heappush(pq,(startnode,0))
    spanningtreelength = 0
    while len(pq)>0:
        node,dist = heapq.heappop(pq)
        if visited[node] == 0:
            visited[node]=1
            spanningtreelength+=dist
            nodedistance = math.inf
            for x in adjlist[node]:
                nodenumber = x[0]
                tempdist = x[1]
                nodedistance=min(nodedistance,tempdist)
                heapq.heappush(pq,(nodenumber,nodedistance))
    return spanningtreelength

print(PrimsMST(priorityqueue,adjarr,1,nodevisitedarr))

#Edit Distance

string1 = "camaraderie"
string2 = "comradery"
ResultsTracker = []
for _ in range(len(string1)+1):
    ResultsTracker.append([])
    for k in range(len(string2)+1):
        ResultsTracker[-1].append(0)

def LevinsteinDistance(firststring,secondstring,trackerlist):
    firststring = firststring.lower()
    secondstring = secondstring.lower()
    firststringlist = list(firststring)
    secondstringlist = list(secondstring)
    for n in range(len(firststring)+1):
        for j in range(len(secondstring)+1):
            if n == 0 and j==0:
                pass
            elif n==0:
                trackerlist[n][j]=int(j)
            elif j == 0:
                trackerlist[n][j]=int(trackerlist[n-1][j])+1
            else:
                trackerlist[n][j]=min(trackerlist[n-1][j],trackerlist[n-1][j-1],trackerlist[n][j-1])
                if firststringlist[n-1]!=secondstringlist[j-1]:
                    trackerlist[n][j]+=1
    
    return trackerlist[len(firststring)][len(secondstring)]

print(LevinsteinDistance(string1,string2,ResultsTracker))


#UnAdvanced KnapSack
weights = [1,3,3,5,11]
hu = 0
for x in weights:
    hu+=x
possibleweights = [False]*(hu+1)

possibleweights[0]=True

def KnapSackSolver (weightclass,solvability):
    for w in range(len(weightclass)):
        for hk in range(len(solvability)-1,-1,-1):
            if solvability[hk]==True:
                solvability[hk+weightclass[w]] = True
    return solvability

print(KnapSackSolver(weights,possibleweights))
        

#Longest Increasing Subsequence

IncreasingArr = [6,2,5,1,7,4,8,3]

PrefixSumLikeMaxSequenceEnding = [1]*len(IncreasingArr)

def IncreasingArrN2(arr,prefixarr):
    for x in range(len(arr)):
        for h in range(x):
            if arr[x]>arr[h]:
                prefixarr[x]=max(prefixarr[x],prefixarr[h]+1)
    return prefixarr

print(IncreasingArrN2(IncreasingArr,PrefixSumLikeMaxSequenceEnding))





#nlogn Longest Increasing Subsequence Solution
sequencearrty = []
def LISTrue(numarr,sequencearr):
    sequencearr.append(numarr[0])
    for x in range(len(numarr)):
        if numarr[x]>sequencearr[-1]:
            sequencearr.append(numarr[x])
        else:
            comp = numarr[x]
            leftpointer = 0
            rightpointer = len(sequencearr)-1
            while leftpointer!=rightpointer:
                mid = (leftpointer+rightpointer)//2
                if sequencearr[mid]>comp:
                    rightpointer = mid
                elif sequencearr[mid]<comp:
                    leftpointer=mid+1
            sequencearr[leftpointer]=comp
    return sequencearr
    
print(LISTrue(IncreasingArr,sequencearrty))
#binsearch everytime





#Bellman-Ford
edgenumber = 5
dist = [math.inf]*edgenumber
edgelist = [(2,3,7),(3,4,2),(0,4,1),(0,3,9),(0,1,5),(1,2,2)]
adjarr = []
for _ in range(edgenumber):
    adjarr.append([])

for x in edgelist:
    adjarr[x[0]].append([x[1],x[2]])
    adjarr[x[1]].append([x[0],x[2]])

print(adjarr)

def BellmanFord(startnode,distance,adjlist):
    distance[startnode]=0
    for i in range(len(distance)):
        for edge in adjlist[i]:
            node = edge[0]
            weight = edge[1]
            distance[node]=min(distance[node],distance[i]+weight)
    return distance

print(BellmanFord(1,dist,adjarr))


#Bellman-Ford Negative Cycles

#Floyd Warshall

nodenumber = 5

edgeyarr = [(2,3,7),(3,4,2),(0,4,1),(0,3,9),(0,1,5),(1,2,2)]

shortestdistmatrix = []

for x in range(nodenumber):
    shortestdistmatrix.append([])
    for y in range(nodenumber):
        if x == y:
            shortestdistmatrix[-1].append(0)
        else:
            shortestdistmatrix[-1].append(math.inf)

for x in edgeyarr:
    shortestdistmatrix[x[0]][x[1]]=x[2]
    shortestdistmatrix[x[1]][x[0]]=x[2]

def FloydWarshall(distmatrix):
    squaredim = len(distmatrix)
    for num in range(squaredim):
        for x in range(squaredim):
            for y in range(squaredim):
                distmatrix[x][y]=min(distmatrix[x][y],distmatrix[x][num]+distmatrix[y][num])
    return distmatrix

print(FloydWarshall(shortestdistmatrix))
print('zex')

#Bitmask DP

#Range DP

#Digit DP

#True 0/1 KnapSack

#Kruskal's Solution

#Geometry Algorithms

#Segment tree

#Spare Tables/Range Minimum Queries (RMQ's)

MinArray = [1,3,4,8,6,1,4,2]

QueryArrMin = []

#K&-k


const = 0
ex = len(MinArray)
while ex>>1 != 0:
    ex=ex>>1
    const+=1

for x in range(const+1):
    QueryArrMin.append([])

#firstrow
    
def SparseTableRMQ(numarr,appendarr,constant):
    appendarr[0]=list(numarr)
    individualquerylen = 1
    for row in range(constant):
        prevquerylen = int(individualquerylen)
        individualquerylen = individualquerylen<<1
        for h in range(len(numarr)-individualquerylen+1):
            appendarr[row+1].append(min(appendarr[row][h],appendarr[row][h+prevquerylen]))
    return appendarr

SparseTableRMQ(MinArray,QueryArrMin,const)

def SparseTableQueryAnswer(param1,param2,queryarr):
    lenseq = param2-param1+1
    con = 0
    while lenseq>>1 != 0:
        lenseq>>=1
        con+=1
    secondquery = lenseq-(2**con)
    return min(queryarr[con][param1],queryarr[con][secondquery])

print(SparseTableQueryAnswer(1,6,QueryArrMin))

#simplify the solution




#toposort fails at 1



#Topo Sort (DFS)

#Ternary Search

def mathfunc(x):
    return -3*(x**2)+(75*x)-2
def TernarySearch(leftbound,rightbound):
    error = 10**-6
    while rightbound-leftbound > error:
        if mathfunc(rightbound) < mathfunc(leftbound):
            rightbound -= ((rightbound-leftbound)/3)
        else:
            leftbound += ((rightbound-leftbound)/3)
    return mathfunc(rightbound)

print(TernarySearch(-1000,1000))



#BIT/Fenwick Tree

ogarr = [1,3,4,8,6,1,4,2]

newarr = [0]*len(ogarr)

def initializefenwick(arr,oglist):
    for x in range(len(arr)):
        if (x+1) & 1 == 1:
            arr[x] = oglist[x]
        else:
            tempvar = (x+1)&((-1*x)-1)
            ind = (x+1)-tempvar
            while (tempvar>>1) !=0:
                tempvar>>=1
                ind+=tempvar
                arr[x]+=arr[ind-1]
            arr[x]+=oglist[x]
    return arr

initializefenwick(newarr,ogarr)

def sumquery(fenwickarr,startind,endind,ogarr):
    if startind==endind:
        return ogarr[startind]
    
    realstartind = startind
    realendind = endind+1

    firstsum = 0
    while realstartind>0:
        firstsum+=fenwickarr[realstartind-1]
        realstartind -= (realstartind)&(-1*realstartind)

    secondsum = 0
    while realendind>0:
        secondsum+=fenwickarr[realendind-1]
        realendind -= (realendind)&(-1*realendind)
    
    return int(secondsum-firstsum)

print(sumquery(newarr,1,6,ogarr))

def add(index,amount,newlist):
    referencepointer = index+1

    while referencepointer<=len(newlist):
        newlist[referencepointer-1]+=amount
        referencepointer+=(referencepointer)&(-1*referencepointer)

    return newlist

print(add(2,7,newarr))

#Segment Tree

originalarraylist = [1,3,4,8,6,1,4,2]

segmenttreearr = [0]*(2*len(originalarraylist))


def segmenttreemaker(originalarr,segmenttreearrsy):
    for i in range(len(originalarr)):
        segmenttreearrsy[i+len(originalarr)] = originalarr[i]
    
    for h in range(len(originalarr)-1,0,-1):
        segmenttreearrsy[h]=segmenttreearrsy[2*h]+segmenttreearrsy[2*h+1]
    
    return segmenttreearrsy

print(segmenttreemaker(originalarraylist,segmenttreearr))


def sum(firstnum,secondnum,segmenttreelist):
    sum = 0
    lensy = int(len(segmenttreelist)/2)
    firstnum+=lensy
    secondnum+=lensy
    while firstnum<secondnum:
        if firstnum & 1 == 1:
            sum+=segmenttreelist[firstnum]
            firstnum+=1
        if secondnum & 1 == 0:
            sum+=segmenttreelist[secondnum]
            secondnum-=1
        firstnum//=2
        secondnum//=2
    if firstnum == secondnum:
        sum+=segmenttreelist[firstnum]
    return sum

print(sum(1,6,segmenttreearr))

def add(newnumber,index,segmenttreelis):
    lent = int(len(segmenttreelis)/2)
    differential = newnumber-segmenttreelis[index+lent]
    newind = int(index+lent)
    while newind>0:
        segmenttreelis[newind]+=differential
        newind//=2
    return segmenttreelis

print(add(5,4,segmenttreearr))

#Iterative vs. Recursive

#Euler Tours

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

#BIT 

newfenwicknodevalues = [0]*len(nodevalues)

def FenwickTree(fenwickarr,nodevalue):
    fenwickarr[0]=nodevalue[0]
    for x in range(len(nodevalue)-1):
        comp = int(x+2)
        leastbit = (comp)&(-1*comp)
        indy = int(comp-leastbit)
        leastbit>>=1
        while leastbit > 0:
            indy+=leastbit
            fenwickarr[comp-1]+=fenwickarr[indy-1]
            leastbit>>=1
        fenwickarr[comp-1]+=nodevalue[comp-1]
    return fenwickarr

FenwickTree(newfenwicknodevalues,nodevalues)

def FenwickSum(start,end,fenwick,nodeval):
    #start and end are 0 index based
    if start == end:
        return nodeval[start]
    firstsum = 0
    start-=1
    while start>=0:
        firstsum+=fenwick[start]
        start-=(start+1)&(-1*start-1)

    secondsum = 0

    while end>0:
        secondsum+=fenwick[end]
        end-=(end+1)&(-1*end-1)

    return int(secondsum-firstsum)

def FenwickUpdate(node,newnumber,fenwickarr,oldarr):
    difference = int(newnumber - oldarr[node])
    negativetrickind = node+1
    oldarr[node] = newnumber
    while negativetrickind<=len(fenwickarr):
        fenwickarr[negativetrickind-1]+=difference
        negativetrickind+=(negativetrickind)&(-1*negativetrickind)
    return fenwickarr
   
subtreesum = []

for u in range(len(subtreelen)):
    subtreesum.append(FenwickSum(u,u+subtreelen[u]-1,newfenwicknodevalues,nodevalues))

print(subtreesum)

#additional techniques

#Range Update

RangeUpdateArr = [3, 3, 1, 1, 1, 5, 2, 2]

DifferenceArray = [0]*len(RangeUpdateArr)

def DifferenceArrayMaker(rangearr,diffarr):
    diffarr[0]=rangearr[0]
    for x in range(len(rangearr)-1):
        diffarr[x+1] = rangearr[x+1]-rangearr[x]

DifferenceArrayMaker(RangeUpdateArr,DifferenceArray)


FenwickList = [0]*len(RangeUpdateArr)


def AnotherFenwickTree(fenwickarr,differencearr):
    fenwickarr[0]=differencearr[0]
    for x in range(len(fenwickarr)-1):
        comp = int(x+2)
        leastsigbit = (comp)&(-1*comp)
        indy = int(comp - leastsigbit)
        leastsigbit>>=1
        while leastsigbit > 0:
            indy+=leastsigbit
            fenwickarr[comp-1]+=fenwickarr[indy-1]
            leastsigbit>>=1
        fenwickarr[comp-1]+=differencearr[comp-1]
    return fenwickarr

AnotherFenwickTree(FenwickList,DifferenceArray)

def AnotherFenwickSum(value,fenwickarr):
    #0 based value
    sum = 0
    while value>=0:
        sum+=fenwickarr[value]
        value-=(value+1)&(-1*value-1)
    return sum

def AnotherFenwickUpdate(pos,valueadded,fenwickarr,differencearr):
    diffy = int(valueadded)
    differencearr[pos]+=valueadded

    while pos < len(fenwickarr):
        fenwickarr[pos]+=diffy
        pos+=(pos+1)&(-1*pos-1)

    return fenwickarr

def RangeUpdateFR(ind1,ind2,numberincrease,fenwickarr,diffarr):

    AnotherFenwickUpdate(ind1,numberincrease,fenwickarr,diffarr)
    if ind2<len(fenwickarr)-1:
        AnotherFenwickUpdate(ind2+1,-1*numberincrease,fenwickarr,diffarr)
    return fenwickarr

RangeUpdateFR(1,4,-4,FenwickList,DifferenceArray)
    
for a in range(8):
    print(AnotherFenwickSum(a,FenwickList))


#ancestors of a tree (precal)





#LCA: 3 Main Methods: Segment Tree, Sparse Tables, Binary Lifting
    



#TopoSort (Kahn's Algorithm)

#Topo Sort (Kahn's Algo)

numnodes=6
edgelistyarr = [(0,1),(1,2),(2,5),(0,3),(3,4),(4,1),(4,2)]
visitedarr = [0]*numnodes

adjarrsy = [[] for _ in range(numnodes)]


for x in edgelistyarr:
    adjarrsy[x[0]].append(x[1])


topolist = []

elqueue = []

# def bfs(adjacencylist,visitedlist,startnode,queue,topo):
#     queue.append(startnode)
#     thrup = []
#     thrup.append(startnode)
#     while len(queue)>0:
#         counter = 0
#         for x in adjacencylist[queue[0]]:
#             if visitedlist[x]==0:
#                 queue.append(x)
#                 thrup.append(x)
#                 visitedlist[x]=1
#                 counter+=1
#             elif visitedlist[x]==1:
#                 counter+=1

#         if len(queue) == 1 and counter == 0:
#             for x in thrup:
#                 visitedlist[x]=2
#             thrup.reverse()
#             topo.extend(thrup)
#             break

#         queue.pop(0)

#     return topo

def dfs(adjlist,visitlist,startnode,topo):
    visitlist[startnode]=1
    for x in adjlist[startnode]:
        if visitlist[x]==0:
            dfs(adjlist,visitlist,x,topo)
    if len(adjlist[startnode])>0 and len(topo)==0:
        return "bruh"
    topo.append(startnode)

    return topo

templist = []

for x in range(numnodes):
    if visitedarr[x]==0:
        tempvar = dfs(adjarrsy,visitedarr,x,templist)
        templist = []
        if tempvar == "bruh":
            print(tempvar)
        else:
            topolist.extend(list(tempvar))
    
topolist.reverse()
print(topolist)

pathnum = []

def TopoSortDP(startnode,endnode,pathnumlist,topolist,adjlist):
    tempind = topolist.index(startnode)
    tempind2 = topolist.index(endnode)
    ghlist = topolist[tempind:(tempind2+1)]
    print(ghlist)
    if tempind2<tempind:
        return "bruh"
    elif tempind2 == tempind:
        return 1
    else:
        pathnumlist = [0]*len(topolist)
        pathnumlist[startnode]=1
        heu = 0
        for x in ghlist:
            for h in adjlist[topolist[tempind+heu]]:
                pathnumlist[h]+=(pathnumlist[x])
                print(pathnumlist)
            heu +=1
    return int(pathnumlist[endnode])

print(TopoSortDP(0,2,pathnum,topolist,adjarrsy))
        
    




#Topo Sort DP




#Trie Data Structure relies on a 2d Array, where there are N nodes, representing the string length
#There are 26 slotsin each list, for the possibility of the letters


#LCA with Binary Lifting

#SCC and 2SAT

edgetuples = [(0,1),(1,0),(0,3),(4,3),(2,1),(5,2),(6,5),(2,6),(5,4),(1,4)]

adjarrnormal = []

adjarrreverse = []

humnodes = 7
visitee = [0]*humnodes

for _ in range(humnodes):
    adjarrnormal.append([])
    adjarrreverse.append([])

for edge in edgetuples:
    adjarrnormal[edge[0]].append(edge[1])
    adjarrreverse[edge[1]].append(edge[0])


topo = []

def toposort(adjacencylist,visitedlist,startnode,topolis):
    
    visitedlist[startnode]=1

    for f in adjacencylist[startnode]:
        if visitedlist[f]==0:
            toposort(adjacencylist,visitedlist,f,topolis)

    topolis.append(startnode)

    return topolis


def Kosajarus(adjnormal,adjreverse,visitlist,topolist,numnodes):
    visitlist=[0]*numnodes
    for a in range(numnodes):
        if visitlist[a] == 0:
            toposort(adjnormal,visitlist,a,topolist)

    cumulativearr = []
    hut = []
    visitlist=[0]*numnodes
    
    for u in range(len(topolist)-1,-1,-1):
        if visitlist[topolist[u]] == 0:
            cumulativearr.append(list(toposort(adjreverse,visitlist,topolist[u],hut)))
            hut = []
    
    return cumulativearr

print(Kosajarus(adjarrnormal,adjarrreverse,visitee,topo,humnodes))



#2SAT Problem

varnum = 4
statementnum = 5

firststatement = [2,-1,1,-2,1]
secondstatement = [-1,-2,3,-3,4]

adjmat = []
bizzaradj = []

for _ in range(2*varnum+1):
    adjmat.append([])
    bizzaradj.append([])

for x in range(len(firststatement)):
    temp1 = firststatement[x]
    temp2 = secondstatement[x]

    adjmat[-1*temp1 + varnum].append(temp2+varnum)
    adjmat[-1*temp2 + varnum].append(temp1+varnum)
    bizzaradj[(temp1+varnum)].append((-1*temp2) + varnum)
    bizzaradj[(temp2+varnum)].append((-1*temp1) + varnum)


def topos(visit,startnode,topolissy,adjlist,counter):

    visit[startnode]=counter

    for x in adjlist[startnode]:
        if visit[x]==0:
            topos(visit,x,topolissy,adjlist,counter)
    
    topolissy.append(startnode)

    return topolissy


def topos2(visit,startnode,adjlist,counter,toposlisty):

    visit[startnode]=counter

    for x in adjlist[startnode]:
        if visit[x]==0:
            topos2(visit,x,adjlist,counter,toposlisty)
    toposlisty.append(startnode)
    return (visit,toposlisty)

premp = [0]*(2*varnum+1)

def SCC(normaladj,reverseadj,visitlist,varnummy):
    topolist = []
    for x in range(2*varnummy+1):
        if x == varnummy:
            pass
        elif visitlist[x]==0:
            topolist = topos(visitlist,x,topolist,normaladj,1)
    visitlist=[0]*(2*varnum+1)
    counters = 1
    ars = []
    hum = []
    for n in range(len(topolist)-1,-1,-1):
        if visitlist[topolist[n]]==0:
            hus = topos2(visitlist,topolist[n],reverseadj,counters,hum)
            visitlist = hus[0]
            ars.append(hus[1])
            hum = []
            counters+=1
            
    return (visitlist,ars)

tex,hud = SCC(adjmat,bizzaradj,premp,varnum)

tex.pop(varnum)

def SATCheckandConstruction(texylist,hudsy):
    firstlist = list(texylist[:varnum])
    secondlist = list(texylist[varnum:])
    for x in range(int(len(texylist)/2)):
        if firstlist[x]==secondlist[-1*x-1]:
            return "impossible"

    answersseen = [-1]*varnum

    for x in range(len(hudsy)-1,-1,-1):
        for y in hudsy[x]:

            if answersseen[abs(int(y-varnum))-1]==-1:
                if int(y-varnum) > 0:
                    answersseen[abs(int(y-varnum))-1]=True
                else:
                    answersseen[abs(int(y-varnum))-1]=False

    #False = 0? Boolean Values are sus
    
    return answersseen

answersseen = [0]*varnum

print(SATCheckandConstruction(tex,hud))


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
#use a capcity matrix

#bfs parent

#Tree and Full DP

#DSU and Kruskal's


