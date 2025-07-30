import sys

adjlist = [[1,2],[],[3,4],[],[]]
dplist = []


for i in range(len(adjlist)):
    dplist.append([0,0])

def dfs(startnode):
    for x in adjlist[startnode]:
        dfs(x)
        dplist[startnode][0] += max(dplist[x][0],dplist[x][1])
    for x in adjlist[startnode]:
        dplist[startnode][1] = max(dplist[startnode][1],dplist[startnode][0]-max(dplist[x][0],dplist[x][1])+1+dplist[x][0])

dfs(0)

print(max(dplist[0][0],dplist[0][1]))
        
    
