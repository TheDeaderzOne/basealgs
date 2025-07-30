import math


#Hierholzer's Alg


edgarr = [[1],[2,4],[4],[0],[3]]

patharrsy = []

edgecountarr = [1,2,1,1,1]

#basically, count the outgoing number of edge, and choose the start node as the one with one more than the other,
#or some random edge


def hfs(startnode,outgoingedgearr,adlist,patharr):
    while outgoingedgearr[startnode]!=0:
        outgoingedgearr[startnode]-=1
        hfs(adlist[startnode][outgoingedgearr[startnode]],outgoingedgearr,adlist,patharr)
    patharr.append(startnode)

    return patharr

hfs(1,edgecountarr,edgarr,patharrsy)
patharrsy.reverse()
print(patharrsy)

#LCA




originalarraylist = [2,1,5,3,4,2]

segmenttreearr = [0]*(4*len(originalarraylist))


def segmenttreemaker(treenodestart,segmentlenstart,segmentlenend,segmenttreearr,originalarray):

    if segmentlenstart == segmentlenend:
        segmenttreearr[treenodestart]=originalarray[segmentlenstart]
        return segmenttreearr[treenodestart]

    else:
        bisectpoint = (segmentlenstart+segmentlenend)//2
        segmenttreemaker(2*treenodestart,segmentlenstart,bisectpoint,segmenttreearr,originalarray)
        segmenttreemaker(2*treenodestart+1,bisectpoint+1,segmentlenend,segmenttreearr,originalarray)
        segmenttreearr[treenodestart]=segmenttreearr[2*treenodestart]+segmenttreearr[2*treenodestart+1]


segmenttreemaker(1,0,len(originalarraylist)-1,segmenttreearr,originalarraylist)
print(segmenttreearr)

for x in range(len(segmenttreearr)):
    segmenttreearr[x]=[segmenttreearr[x],0]

print(segmenttreearr)

def topbottomsegmentsum(liststartnode,listendnode,treenode,liststart,listend,treearr,modification):
    if liststartnode>listend or listendnode < liststart:
        return 0
    print(liststart,listend,treenode)
    if liststartnode <= liststart and listendnode >= listend:
        return treearr[treenode][0]+((listend-liststart+1)*modification)
    bisectionpoint = (liststart+listend)//2
    return topbottomsegmentsum(liststartnode,listendnode,2*treenode,liststart,bisectionpoint,treearr,max(modification,treearr[2*treenode][1]))+topbottomsegmentsum(liststartnode,listendnode,2*treenode+1,bisectionpoint+1,listend,treearr,max(modification,treearr[2*treenode+1][1]))


# def sum(firstnum,secondnum,segmenttreelist):
#     sum = 0
#     lensy = int(len(segmenttreelist)/2)
#     firstnum+=lensy
#     secondnum+=lensy

#     while firstnum<=secondnum:
    
#         if firstnum & 1 == 1:
#             sum+=segmenttreelist[firstnum]
#             firstnum+=1

#         if secondnum & 1 == 0:
#             sum+=segmenttreelist[secondnum]
#             secondnum-=1
        
#         firstnum//=2
#         secondnum//=2

#     return sum

# print(sum(2,3,segmenttreearr))

# def add(newnumber,index,segmenttreelis):
#     lent = int(len(segmenttreelis)/2)
#     differential = newnumber-segmenttreelis[index+lent]
#     newind = int(index+lent)
#     while newind>0:
#         segmenttreelis[newind]+=differential
#         newind//=2
#     return segmenttreelis

# print(add(5,4,segmenttreearr))


#lazypropogate func

def lazypropogatechanges(liststartnode,listendnode,treenode,liststart,listend,treearr,increment):
    if liststartnode>listend or listendnode < liststart:
        return 0
    else:
        if liststartnode <= liststart and listendnode >= listend:
            treearr[treenode][1]=increment
            return treearr[treenode][1]
        bisectionpoint = (liststart+listend)//2
        lazypropogatechanges(liststartnode,listendnode,2*treenode,liststart,bisectionpoint,treearr,increment)
        lazypropogatechanges(liststartnode,listendnode,2*treenode+1,bisectionpoint+1,listend,treearr,increment)


# lazypropogatechanges(0,2,1,0,len(originalarraylist)-1,segmenttreearr,2)

print(segmenttreearr)

# segmenttreearr=[[0,0],[15,0],[8,0],[7,0],[2,0],[6,0],[3,0],[4,0],[1,0],[5,0]]
print(topbottomsegmentsum(0,2,1,0,len(originalarraylist)-1,segmenttreearr,0))



#Treap

