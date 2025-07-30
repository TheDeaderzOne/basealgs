import math
import re

#Trie, O(N) preprocessing and O(N) space complexity

#a Trie works basically as a adjacencylist/tree, where each node points to another node for words, and stops once there is a "True", indicating a full word

#Basically, it checks words by traversing the adjacency list, and it builds the trie by leaving pointers

#It is imperative that it leaves pointers only when there hasn't been one before, and it it leaves pointers at the current end of the list

trielist = [[[-1]*26,False]]

def addstring(string,triearr):
    indextracker = 0
    for character in string:
        characternum = ord(character)-ord('a')
        if triearr[indextracker][0][characternum]==-1:
            triearr[indextracker][0][characternum] = len(triearr)
            triearr.append([[-1]*26,False])
        indextracker = triearr[indextracker][0][characternum]
    triearr[indextracker][1]=True

addstring('she',trielist)
addstring('hers',trielist)
addstring('he',trielist)
addstring('his',trielist)


# addstring('a',trielist)
# addstring('ab',trielist)
# addstring('bc',trielist)
# addstring('bca',trielist)
# addstring('c',trielist)
# addstring('caa',trielist)

def stringchecker(string,triearr):
    indextracker = 0
    for char in string:
        charindex = ord(char)-ord('a')
        if triearr[indextracker][0][charindex]==-1:
            return False
        indextracker = triearr[indextracker][0][charindex]
    return triearr[indextracker][1]

#Aho-Corasick
# Yes you could use an adjacency list, but it don't matter, it makes searching easier 

# add an explicit "suffix link"

# This gives the suffix links explicitly 

def ahocorasick(triearr):
    # Just assume the empty stirng can't be accepted lol
    queue = []
    for i in range(len(triearr)):
        triearr[i].append(0)
        triearr[i].append([])
    # remember that triearr is a 2d array (boolean)
    alphabetlen = len(triearr[0][0])
    queue.append((0,-1,-1,""))
    while len(queue)>0:
        # keep on referencing the parents 

        newindex, parentindex, letternum, accumulatedstring = queue.pop(0)
        
        # account for the "accumulated" string
        
        for x in range(alphabetlen):
            # makes a new (child, parent, letternum) node
            if triearr[newindex][0][x]!=-1:
                queue.append((triearr[newindex][0][x],newindex,x, accumulatedstring + chr(ord('a')+x)))

        if parentindex != 0:
            
            if triearr[parentindex][2] != 0 and triearr[triearr[parentindex][2]][0][letternum]!= -1:
                triearr[newindex][2] = triearr[triearr[parentindex][2]][0][letternum]
                newl = list(triearr[triearr[triearr[parentindex][2]][0][letternum]][3])
                triearr[newindex][3] = newl

            elif triearr[0][0][letternum]!= -1:
                triearr[newindex][2] = (triearr[0][0][letternum])
        
        if triearr[newindex][1] == True: 
            triearr[newindex][3].append(accumulatedstring)
            
    return triearr

# Multiple String Checker, You need terminal links as well 

# 0 indexed
def ahostringchecker(text,triearr):
    # outputs: words, endpoint
    text = re.sub(r'[^a-z]', '', text.lower())
    print(text)
    matcharr = []; indextracker = 0
    
    for i in range(len(text)):
        charindex = ord(text[i])-ord('a')
        
        # Need a while loop 
        
        if triearr[indextracker][0][charindex]==-1:
            while triearr[indextracker][0][charindex]==-1 and indextracker != 0:
                indextracker = triearr[indextracker][2]
            if triearr[indextracker][0][charindex] != -1:
                indextracker = triearr[indextracker][0][charindex]
    
        else:
            indextracker = triearr[indextracker][0][charindex]
            if triearr[indextracker][1] == True: 
                matcharr.append((triearr[indextracker][3], i))
    
    return matcharr
             
print(ahostringchecker("she is hers but he has his own way", ahocorasick(trielist)))

#Aho Corasick is basically trying to use a trie, but efficiently search a trie such that if you run into 
# a dead end, then you can transfer to another similar node, where the suffix matches with the prefix, to 
#eliminate the dead end prefix, which is done through bfs 