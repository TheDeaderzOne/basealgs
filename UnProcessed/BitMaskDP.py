import sys
import math
products = [[6,9,5,2,8,9,1,6],[8,2,6,2,7,5,7,2],[5,3,9,7,3,5,1,4]]

# Recurring product price, subset problem

subsetlist = []
daynum = len(products[0])
productnum = len(products)

for x in range(1<<productnum):
    if x == 0: 
        subsetlist.append([0]*daynum)
    else:
        subsetlist.append([math.inf]*daynum)
    
for h in range(productnum):
    subsetlist[1<<h][0] = products[h][0]
    
for d in range(1,daynum):
    for s in range((1<<productnum)):
        subsetlist[s][d] = subsetlist[s][d-1]
        for x in range(productnum):
            if (s & (1<<x) != 0):
                subsetlist[s][d] = min(subsetlist[s][d],subsetlist[s^(1<<x)][d-1]+products[x][d])
        
print(subsetlist)
        
#  Elevator rides

maxweight = 10
weightlist = [2,3,3,5,6]

bestrides = []
Nb = len(weightlist)

for x in range(1<<Nb):
    bestrides.append([0,0])
    
bestrides[0] = [1,0]

for i in range(1,1<<Nb):
    bestrides[i] = [Nb+1,0]
    for j in range(Nb):
        if (i&(1<<j)):
            potentialpair = list(bestrides[i^(1<<j)])
            if potentialpair[1]+weightlist[j] <= maxweight:
                potentialpair[1] += weightlist[j]
            else:
                potentialpair[0]+=1
                potentialpair[1] = weightlist[j]
            bestrides[i] = min(bestrides[i],potentialpair)

print(bestrides[-1])


# sum over subsets

valuelist = [3,1,4,5,5,1,3,3]
sumlist = []
Nt = 3
for x in range(1<<Nt):
    sumlist.append(valuelist[x])

for h in range(Nt):
    for j in range(1<<Nt):
        if (j&(1<<h)):
            sumlist[j]+=sumlist[j^(1<<h)]
    
print(sumlist)