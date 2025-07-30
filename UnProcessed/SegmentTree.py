import sys
sys.setrecursionlimit(10**5)

array = [2,1,5,3,4,2]

segmentarray = [0]*(4*len(array))

def SegmentTreeInitializer(startind,endind,arraynode):
    if startind < 0 or endind >= len(array):
        return 0
    elif startind == endind:
        segmentarray[arraynode] = array[startind]
        return array[startind]
    bisect = (startind+endind) // 2
    segmentarray[arraynode] = SegmentTreeInitializer(startind, bisect,2*arraynode+1)+SegmentTreeInitializer(bisect+1, endind,2*arraynode+2)
    return segmentarray[arraynode]
    
SegmentTreeInitializer(0,len(array)-1,0)


# if currentindend>sumend or currentindstart < sumend:


def SegmentTreeSum(sumstart, sumend, currentindstart, currentindend, segmenttreenode):
    if currentindend < sumstart or currentindstart > sumend:
        return 0
    elif currentindstart >= sumstart and sumend >= currentindend:
        return segmentarray[segmenttreenode]
    bisect = (currentindstart+currentindend)//2
    return SegmentTreeSum(sumstart,sumend,currentindstart,bisect,2*segmenttreenode+1)+SegmentTreeSum(sumstart,sumend,bisect+1,currentindend,2*segmenttreenode+2)


# 
# def topbottomsegmentsum(liststartnode,listendnode,treenode,liststart,listend,treearr,modification):
#     if liststartnode>listend or listendnode < liststart:
#         return 0
#     print(liststart,listend,treenode)
#     if liststartnode <= liststart and listendnode >= listend:
#         return treearr[treenode][0]+((listend-liststart+1)*modification)
#     bisectionpoint = (liststart+listend)//2
#     return topbottomsegmentsum(liststartnode,listendnode,2*treenode,liststart,bisectionpoint,treearr,max(modification,treearr[2*treenode][1]))+topbottomsegmentsum(liststartnode,listendnode,2*treenode+1,bisectionpoint+1,listend,treearr,max(modification,treearr[2*treenode+1][1]))


print(SegmentTreeSum(0,3,0,len(array)-1,0))


print(segmentarray)


    