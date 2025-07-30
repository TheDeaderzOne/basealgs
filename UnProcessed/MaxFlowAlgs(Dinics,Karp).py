import math

edgylist = [[[1,16],[2,18]],[[2,10],[3,8]],[[1,4],[4,12]],[[2,1],[5,20]],[[3,7],[5,4]],[]]

# Dinic's

visit = [0]*6
levelsy = [0]*6
qu = []

def levelbfs(queue,adjlist,levels,visit,sink):
    queue.append((0,0))
    while len(queue)>0:
        for x in adjlist[queue[0][0]]:
            if visit[x[0]]==0 and x[1]>0:
                visit[x[0]]=1
                levels[x[0]]=queue[0][1]+1
                queue.append((x[0],levels[x[0]]))
        queue.pop(0)
    if visit[sink]==0: return False
    return levels

def zfs(sink,startnode,bfslevelarr,maxflow,prunearr,adjlist):
    if startnode==sink:
        return maxflow
    while prunearr[startnode]<len(adjlist[startnode]):
        edge = adjlist[startnode][prunearr[startnode]]
        if edge[1]>0 and bfslevelarr[edge[0]]==(bfslevelarr[startnode]+1):
            pathprogress = zfs(sink,edge[0],bfslevelarr,min(maxflow,edge[1]),prunearr,adjlist)
            if pathprogress and pathprogress>0:
                edge[1]-=pathprogress
                return pathprogress
        prunearr[startnode]+=1

def maindinic(queue,adjlist,levels,visit,sink,start):
    prunearr = [0]*6
    maxflow=0
    tec = levelbfs(queue,adjlist,levels,visit,sink)
    while tec!=False:
        prunearr=[0]*6; queue=[]; visit = [0]*6
        maxflow+=zfs(sink,start,levels,math.inf,prunearr,adjlist)
        levels = [0]*6
        tec = levelbfs(queue,adjlist,levels,visit,sink)

    return maxflow
        
print(maindinic(qu,edgylist,levelsy,visit,5,0))

# Edmond's Karp

# tulist = [[[1,16],[2,18]],[[2,10],[3,8]],[[1,4],[4,12]],[[2,1],[5,20]],[[3,7],[5,4]],[]]

tulist = [[[1,1],[2,1],[3,1],[4,1]],[[5,1]],[[7,1]],[[5,1],[6,1],[8,1]],[[7,1]],[[9,1]],[[9,1]],[[9,1]],[[9,1]],[]]

def pushbfs(start,sink,adjlist,n,visit,parentlist):
    queue = [(start,math.inf)]
    for _ in range(n): parentlist.append([])
    while len(queue)>0:
        node = queue.pop(0)
        if node[0] == sink: return node[1]
        for i in range(len(adjlist[node[0]])):
            curnode = adjlist[node[0]][i][0]; edgecapacity = adjlist[node[0]][i][1]
            if visit[curnode] == 0 and edgecapacity > 0:
                visit[curnode] = 1
                parentlist[curnode] = [node[0],i]
                queue.append((curnode,min(node[1],edgecapacity)))
    return 0

def edmondskarp(start,sink,adjlist,n):
    parentarr = []; visits = [0] * n; total = 0
    flowval = pushbfs(start,sink,adjlist,n,visits,parentarr)
    while flowval > 0:
        total += flowval; node = sink
        while node != start:
            adjlist[parentarr[node][0]][parentarr[node][1]][1] -= flowval
            node = parentarr[node][0]
        parentarr = []; visits = [0] * n
        flowval = pushbfs(start,sink,adjlist,n,visits,parentarr)
    return total

print(edmondskarp(0,len(tulist)-1,tulist,len(tulist)))
print(tulist)