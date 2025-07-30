import math

#LCA Algorithm, Binary Lifting, O(NlogN) Preprocessing, O(logN) query time

#LCA Finds the lowest common ancestor of two nodes in a tree

#Binary Lifting does this by first using dfs to track the node parents and depths, finds the safe upper bound for a tree (log limit)

#Then, it finds the 2^kth parent for each node on line 26, and then lifts both nodes to be on the same depth

#Then it finds the greatest non-common ancestor for each power, until they converge

treeadjacencylist=[[1, 2, 3],[0, 4, 5],[0, 6, 7],[0, 8],[1, 9, 10],[1, 11],[2],[2, 12],[3, 13],[4],[4],[5, 14, 15],[7],[8],[11],[11, 16, 17],[15],[15, 18, 19],[17],[17]]
nodedeptharr=[0]*len(treeadjacencylist)
highestpowerancestor = math.ceil(math.log(len(treeadjacencylist),2))
parentlist = [[-1]*(highestpowerancestor+1) for _ in range(len(treeadjacencylist))]

def dfs(startnode,parent,tree,depthlist,lognum,parentarr):

    parentarr[startnode][0]=parent

    for i in range(1,lognum+1):
        if parentarr[startnode][i-1]>0:
            parentarr[startnode][i]=parentarr[parentarr[startnode][i-1]][i-1]

    for neighbornodes in tree[startnode]:
        if neighbornodes != parent:
            depthlist[neighbornodes]=depthlist[startnode]+1
            dfs(neighbornodes,startnode,tree,depthlist,highestpowerancestor,parentarr)

    return (parentarr,depthlist)

def logdecomp(nodedepthdif,parent,deepernode):
    ancestorpower = 0
    while nodedepthdif != 0:
        if nodedepthdif & 1 == 1:
            deepernode = parent[deepernode][ancestorpower]
        nodedepthdif>>=1; ancestorpower+=1
    return deepernode

def lca(node1,node2,log,parent,depths):

    if depths[node1]>depths[node2]:
        fulldiff = depths[node1]-depths[node2]
        node1=logdecomp(fulldiff,parent,node1)
    
    elif depths[node1]<depths[node2]:
        fulldiff = depths[node2]-depths[node1]
        node2=logdecomp(fulldiff,parent,node2)

    for i in range(log,-1,-1):
        if parent[node1][i]!=parent[node2][i]:
            node1,node2=(parent[node1][i],parent[node2][i])

    return parent[node1][0]

def lcaquery(firstnode,secondnode,nodedepths,ancestorpower,parentlist,treeadjlist):
    dfs(0,-1,treeadjlist,nodedepths,ancestorpower,parentlist)
    return lca(firstnode,secondnode,ancestorpower,parentlist,nodedepths)
