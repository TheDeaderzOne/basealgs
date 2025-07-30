#Dynamic Programming
import math
import copy
import sys
import heapq
sys.setrecursionlimit(10**5)
# CoinsList = [5,8,17]     
    
# CoinOutputs = []

# DistinctStamping = []


# def coinchange(amount,coinlist,outputlist,stampinglist):
#     outputlist.append(0)
#     stampinglist.append([[0,0,0]])
#     for tempnum in range(1,amount+1):
#         optimalcoinnumber = math.inf
#         temporaryordering = None
#         for coins in range(len(coinlist)):
#             if tempnum-coinlist[coins]>=0:
#                 if outputlist[tempnum-coinlist[coins]]+1<optimalcoinnumber:
#                     temporaryordering = copy.deepcopy(stampinglist[tempnum-coinlist[coins]])
#                     for lol in temporaryordering:
#                         lol[coins]+=1
#                 elif outputlist[tempnum-coinlist[coins]]+1==optimalcoinnumber and optimalcoinnumber != math.inf:
#                     for sumtin in stampinglist[tempnum-coinlist[coins]]:
#                         temporaryordering.append(copy.deepcopy(sumtin))
#                         temporaryordering[-1][coins]+=1
#                 optimalcoinnumber = min(optimalcoinnumber,outputlist[tempnum-coinlist[coins]]+1)
#         outputlist.append(optimalcoinnumber)
#         if temporaryordering!=None:
#             stampinglist.append(copy.deepcopy(temporaryordering))
#         else: 
#             stampinglist.append(None)


# def realcoinchange(amount,coinlist,stampinglist):
#     stampinglist.append(1)
#     for bluh in range (1,amount+1):
#         stiggy = 0
#         for coins in range(len(coinlist)):
#             if bluh-coinlist[coins]>=0:
#                 stiggy+=stampinglist[bluh-coinlist[coins]]
#         stampinglist.append(stiggy)
#     return print(stampinglist)

# realcoinchange(120,CoinsList,DistinctStamping)


# def coinchange(amount,coinlist,stampinglist):
#     stampinglist.append([[0,0,0]])
#     for tempnum in range(1,amount+1):
#         temporaryordering = []
#         for coins in range(len(coinlist)):
#             if tempnum-coinlist[coins]>=0:
#                 if stampinglist[tempnum-coinlist[coins]] != None:
#                     for sumtin in stampinglist[tempnum-coinlist[coins]]:
#                         temporaryordering.append(copy.deepcopy(sumtin))
#                         temporaryordering[-1][coins]+=1
#         if temporaryordering!=[]:
#             stampinglist.append(copy.deepcopy(temporaryordering))
#         else: 
#             stampinglist.append(None)
#     for x in range(len(DistinctStamping)):
#         if DistinctStamping[x] != None:
#             for y in range(len(DistinctStamping[x])):
#                 DistinctStamping[x][y]=tuple(DistinctStamping[x][y])

#     for bt in range(len(DistinctStamping)):
#         if DistinctStamping[bt] != None:
#             DistinctStamping[bt]=set(DistinctStamping[bt])

#     return stampinglist

# coinchange(120,CoinsList,DistinctStamping)

# StampingNumber = []

# for z in range(len(DistinctStamping)):
#     if DistinctStamping[z] != None:
#         StampingNumber.append(len(DistinctStamping[z]))
#     else:
#         StampingNumber.append(0)

# print(StampingNumber)
    


# for xyzw in range(len(DistinctStamping)):
#     DistinctStamping[xyzw]=len(DistinctStamping[xyzw])

                # if outputlist[tempnum-coinlist[coins]]+1<optimalcoinnumber:
                #     temporaryordering = copy.deepcopy(stampinglist[tempnum-coinlist[coins]])
                #     for lol in temporaryordering:
                #         lol[coins]+=1
                # elif outputlist[tempnum-coinlist[coins]]+1==optimalcoinnumber and optimalcoinnumber != math.inf:



#Longest Increasing Subsequence


# LISarray = [6,2,5,1,7,4,8,3]

# def LIS(array,output):
#     for x in range(len(array)):
#         pass






# PathGriddy = [
#     [16, 12, 8, 4, 1],
#     [15, 11, 7, 3, 2],
#     [14, 10, 6, 5, 9],
#     [13, 9, 14, 1, 12],
#     [5, 4, 3, 2, 16]
#     ]

# PathGriddyMax = [
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0]
#     ]

# PathTaken = [
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0]
#     ]

# def MaxPathGridSum(pathgridlist,maxlist):
#     for rows in range(len(pathgridlist)):
#         for elementnum in range(len(pathgridlist[rows])):
#             if rows-1 and elementnum-1 >= 0:
#                 maxlist[rows][elementnum]=max(maxlist[rows-1][elementnum]+pathgridlist[rows][elementnum],maxlist[rows][elementnum-1]+pathgridlist[rows][elementnum])  
#             elif rows-1>=0:
#                 maxlist[rows][elementnum]=maxlist[rows-1][elementnum]+pathgridlist[rows][elementnum]
#             elif elementnum-1>=0:
#                 maxlist[rows][elementnum]=maxlist[rows][elementnum-1]+pathgridlist[rows][elementnum]     
#             else:
#                 maxlist[rows][elementnum]=pathgridlist[rows][elementnum]

#     return maxlist


# def PathTakenProcess(maxlist,pathlist):
#     rownum = len(maxlist)-1
#     columnnum = len(maxlist[0])-1
#     for _ in range(len(maxlist)+len(maxlist[0])-1):
#         pathlist[rownum][columnnum]=1
#         if rownum-1<0:
#             columnnum-=1
#         elif columnnum-1<0:
#             rownum-=1
#         else:
#             if maxlist[rownum-1][columnnum]>maxlist[rownum][columnnum-1]:
#                 rownum-=1
#             else:
#                 columnnum-=1
#     return pathlist



# MaxPathGridSum(PathGriddy,PathGriddyMax)

# for x in PathGriddyMax:
#     print(x)

# PathTakenProcess(PathGriddyMax,PathTaken)

# for x in PathTaken:
#     print(x)

# checklist = []
# bezlist=[]
# wordlist = list("raping")
# chosen = [False,False,False,False,False,False]



# def realperms(arr,checkarr,temparr):
#     if len(temparr) == 6:
#         checkarr.append(list(temparr))
#         temparr=[]
#     for i in range(6):
#         if chosen[i]==False:
#             chosen[i]=True
#             temparr.append(arr[i])
#             realperms(wordlist,checklist,bezlist)
#             chosen[i]=False
#             temparr.pop()

#     return checkarr


# realperms(wordlist,checklist,bezlist)


# parallellist = [0]*len(checklist)

# # print(parallellist)

# for iternerary in range(len(checklist)):
#     parallellist[iternerary]=""
#     for abc in range(len(checklist[iternerary])):
#         parallellist[iternerary]= parallellist[iternerary]+str(checklist[iternerary][abc])


# for ghz in parallellist:
#     print(ghz)

distancearr = [math.inf]*9
eliminated = [0]*9
pq = []
adlist = [[],[],[],[],[],[],[],[],[]]
hx = [[0,1,4],[1,2,8],[2,3,7],[3,4,9],[4,5,10],[5,6,2],[6,7,1],[0,7,8],[3,5,14],[2,5,4],[2,8,2],[6,8,6],[7,8,7],[1,7,11]]

for x in hx:
    ind = x[0]
    ind2 = x[1]
    ind3 = x[2]
    adlist[ind].append([ind3,ind2])
    adlist[ind2].append([ind3,ind])

def Djikstras(priorqueue,distances,visiteddike,startnode,adjlist):
    heapq.heappush(priorqueue,(0,startnode))
    distances[startnode] = 0
    while len(pq)>0:
        dist,tempnode = heapq.heappop(pq)
        if visiteddike[tempnode]==0:
            visiteddike[tempnode]=1
            for s in adjlist[tempnode]:
                weight = s[0]
                snode = s[1]
                distances[snode] = min(dist+weight,distances[snode])
                heapq.heappush(priorqueue,(distances[snode],snode))
    return distances

print(Djikstras(pq,distancearr,eliminated,0,adlist))

#String Hashing

def basicstringhash(string):
    multiplier = 29
    mod = (10**9)+7
    hashvalue = 0
    stringarr = list(string)
    for c in stringarr:
        hashvalue = (hashvalue + ord(c)*multiplier) % mod
        multiplier = (multiplier*multiplier) % mod
        
    return hashvalue

print(basicstringhash('p'))

parentlist = [int(i) for i in range(5)]
sizes = [0]*5