# import sys
import math

# newbgraph = [[],[],[],[],[],[],[],[],[],[],[],[]]

# matchedlist = [-1]*12

# # 6 bipartite nodes

# # greedily match the first few nodes

# for x in range(6):
#     for y in bipartitegraph[x]:
#         if matchedlist[y] == -1:
#             matchedlist[y]=x
#             matchedlist[x]=y
#             break

# visitlist = [0]*12

# def alternatingbfs():
#     for x in range(12): newbgraph[x] = []
#     queue = []
#     # find the first 
    
#     for x in range(6):
#         if matchedlist[x]==-1:
#             queue.append((x,0))
#             b = x
#             break
#         elif x == 5:
#             return False
    
#     alternator = 1
#     while len(queue)>0:
#         h = queue.pop(0)
#         for t in bipartitegraph[h[0]]:
#             if h[1] % 2 == 0:
#                 if matchedlist[t] != h[0] and visitlist[t] == 0:
#                     visitlist[t]=1
#                     if matchedlist[t] == -1:
#                         newbgraph[h[0]] = [t] 
#                     else:
#                         queue.append((t,alternator))
#                         newbgraph[h[0]].append(t)
#             else:
#                 if matchedlist[t] == h[0] and visitlist[t] == 0:
#                     queue.append((t,alternator))
#                     newbgraph[h[0]].append(t)
#                     visitlist[t]=1
#         alternator+=1
#     return b

# visit = [0]*12

# liste = []

# def topodfs(startnode):
#     visit[startnode]=1
#     for h in newbgraph[startnode]:
#         if visit[h] == 0:
#             topodfs(h)
#             break
#     liste.append(startnode)

# for x in range(6):
#     if matchedlist[x] == -1:
#         visit = [0]*12
#         visitlist = [0]*12
#         liste = []
#         topodfs(alternatingbfs())
#         print(newbgraph)
#         print(liste)
#         for x in range(len(liste)-1):
#             if x%2 == 0:
#                 matchedlist[liste[x]]=liste[x+1]
#                 matchedlist[liste[x+1]]=liste[x]

# print(liste)

# print(matchedlist)


n = 6
m = 6

bipartitegraph = [[6],[7,9],[6,10],[7],[8,9,11],[8,10],[0,2],[1,3],[4,5],[1,4],[2,5],[4]]

match = [False]*(n+m+1)
dist = [math.inf] * (n+m+1)


def bfs():
    queue = []
    for node in range(1,n+1):
        if not match[node]:
            queue.append(node)
            dist[node] = 0
        else:
            dist[node] = math.inf
    
    dist[0] = math.inf
    
    while len(queue) > 0:
        node = queue.pop(0)
        if dist[node] >= dist[0]:
            continue
        for son in bipartitegraph[node]:
            if (dist[match[son]] == math.inf):
                dist[match[son]] = dist[node] + 1
                queue.push(match[son])
    
    return dist[0] != math.inf

def dfs(node):
    if node == 0:
        return True
    
    dist[node] = math.inf
    return False