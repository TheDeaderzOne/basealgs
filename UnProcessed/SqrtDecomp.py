import sys
import math

# Mo's Algorithm

offlinequeries = [(0, 4), (2, 6), (5, 8), (0, 8), (3, 5), (1, 7), (2, 3), (4, 4), (0, 2), (6, 8)]

array = [4,2,5,4,2,4,3,3,4]

constant = int(math.sqrt(len(array)))

offlinequeries.sort(key = lambda x: (math.floor(x[0]/constant),x[1]))

# count array 

count25 = [0]*6

querylist = []

startpointer = offlinequeries[0][0]
endpointer = offlinequeries[0][1]

tot = 0

for x in range(endpointer-startpointer+1):
    count25[array[startpointer+x]]+=1
    if count25[array[startpointer+x]] == 1:
        tot+=1
        
querylist.append(tot)

for h in range(len(offlinequeries)-1):
    
    if offlinequeries[h+1][0] - startpointer >= 0:
        for i in range(offlinequeries[h+1][0] - startpointer):
            count25[array[startpointer+i]]-=1
            if count25[array[startpointer+i]] == 0:
                tot-=1
        
    else:
        for i in range(startpointer-1, offlinequeries[h+1][0]-1 ,-1):
            count25[array[i]] += 1
            if count25[array[i]] == 1:
                tot+=1
                
    if offlinequeries[h+1][1] - endpointer >= 0:
        for i in range(offlinequeries[h+1][1] - endpointer):
            count25[array[endpointer+i+1]]+=1
            if count25[array[endpointer+i+1]] == 1:
                tot+=1
    
    else:
        for i in range(endpointer, offlinequeries[h+1][1] ,-1):
            count25[array[i]] -= 1
            if count25[array[i]] == 0:
                tot-=1

    startpointer = offlinequeries[h+1][0]
    endpointer = offlinequeries[h+1][1]
    querylist.append(tot)
    
print(querylist)
        
    
    
    
    
    
    
    
        







