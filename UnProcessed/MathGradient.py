import math
import random
import heapq


# def MultivarFunc(x,y):
#     return ((x**2)+y-11)**2 + (x+(y**2)-7)**2


# def GradientTaker(iterations,startingpointx,startingpointy,steptaker):

#     gradx = (MultivarFunc(startingpointx+.0001,startingpointy)-MultivarFunc(startingpointx,startingpointy))/(.0001)
#     grady = (MultivarFunc(startingpointx,startingpointy+.0001)-MultivarFunc(startingpointx,startingpointy))/(.0001)
#     moduli = math.sqrt(gradx**2+grady**2)
#     startingpointx-=((gradx/moduli)*steptaker)
#     startingpointy-=((grady/moduli)*steptaker)
    
#     for x in range(iterations):
#         startingpointx-=((gradx/moduli)*steptaker*.9)
#         startingpointy-=((grady/moduli)*steptaker*.9)
#         gradx = (MultivarFunc(startingpointx+.0001,startingpointy)-MultivarFunc(startingpointx,startingpointy))/(.0001)
#         grady = (MultivarFunc(startingpointx,startingpointy+.0001)-MultivarFunc(startingpointx,startingpointy))/(.0001)
#         moduli = math.sqrt(gradx**2+grady**2)
#         startingpointx-=((gradx/moduli)*steptaker)
#         startingpointy-=((grady/moduli)*steptaker)

#     return (startingpointx,startingpointy,MultivarFunc(startingpointx,startingpointy))

# print(GradientTaker(100000,random.randint(-1000,1000),random.randint(-1000,1000),.05))












# def newfunc(x,liste,power):
#     totalj = 0
#     for i in range(len(liste)-1):
#         totalj+=(liste[i]*(x**(len(liste)-1-i)))
#     totalj+=liste[-1]

#     return (totalj-math.sin(x))*(x**power)

# def newfuncsy(x,liste):
#     totalj = 0
#     for i in range(len(liste)-1):
#         totalj+=(liste[i]*(x**(len(liste)-1-i)))
#     totalj+=liste[-1]

#     return (totalj-math.sin(x))**2

# # math.sinh(math.exp(1)*x)
# def SimpsonsRule(intervals,start,stop,gradlist,power):
#     totalcounter = 0
#     holder = int(stop-start)
#     for x in range(intervals):

#         totalcounter+=(newfunc(start+((x*holder)/intervals),gradlist,power))+4*(newfunc((start+(((x+.5)*holder)/intervals)),gradlist,power))+(newfunc((start+(((x+1)*holder)/intervals)),gradlist,power))

#     totalcounter *= ((holder/intervals)*(1/3))

#     return totalcounter




# def SimpsonsRuleSpecial(intervals,start,stop,gradlist):
#     totalcounter = 0
#     holder = int(stop-start)
#     for x in range(intervals):

#         totalcounter+=(newfuncsy(start+((x*holder)/intervals),gradlist))+4*(newfuncsy((start+(((x+.5)*holder)/intervals)),gradlist))+(newfuncsy((start+(((x+1)*holder)/intervals)),gradlist))

#     totalcounter *= ((holder/intervals)*(1/6))

#     return totalcounter


# #*2

# def GradientTaker2(iterations,steptaker):

#     gradients = [random.randint(-10000,10000)/10000,random.randint(-10000,10000)/10000,random.randint(-10000,10000)/10000,random.randint(-10000,10000)/10000,random.randint(-10000,10000)/10000,random.randint(-10000,10000)/10000]
#     total = 0
#     temp = [0]*len(gradients)
#     for x in range(iterations):


#         for j in range(len(gradients)):
            
#             temp[j]=(SimpsonsRule(210,-3,3,gradients,len(gradients)-1-j)*steptaker)-(.9*temp[j])
    

#         for x in range(len(gradients)):
#             total += (temp[x]/steptaker)**2
        
#         total = math.sqrt(total)

#         for _ in range(len(gradients)):
#             temp[_]=(temp[_]/total)
#             gradients[_]-=temp[_]
        
#     return (gradients,SimpsonsRuleSpecial(150,-3,3,gradients))

# best = 100000
# listh = []
# for x in range(100):
    
#     print(x)
#     g = GradientTaker2(2000,.001)
#     print(g[1])
#     if g[1]<best:
#         best = g[1]
#         listh.append(g[0])
# print(listh)
# print(best)

#FFT



#DFS retread

edges = [[1,3],[2,4],[1,4],[0,4],[1,2,3]]
visited = [0]*5
def dfs(visited,edges,node):
    visited[node]=1

    for x in edges[node]:
        if visited[x]==0:
            dfs(visited,edges,x)

    return visited


print(dfs(visited,edges,0))


#cycle detection




#bin search

monotone = [True,True,True,True,False,False,False]

def binsearch():
    leftpointer = 0

    pass

#Dijkstra's
listlenst = 5
visited = [0]*listlenst
distlist = [math.inf]*listlenst


#BFS Bipartiteness check

edges = [[1,2],[0,3],[0,3,4],[1,2,4],[2,3]]
visited = [0]*5
queue = []
def BFS(startnode,visitlist,queue,edges):

    pass




#Ternary Search

#Dijkstra's


#Sum Queries

