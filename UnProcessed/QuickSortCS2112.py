# last element pivot
import sys
sys.setrecursionlimit(10000)
quicksortarr = [10, 5, 3, 3, 5, 7, 6]

quicksortarr = [1,2,3,4,5,6,7,8,9,10]

def swap(a,b):
    x = quicksortarr[a]
    quicksortarr[a]=quicksortarr[b]
    quicksortarr[b]=x

def Partition(startind,endind):
    partitioner = quicksortarr[endind]
    ogendind = endind
    endind -= 1
    while startind <= endind:
        if quicksortarr[startind] < partitioner:
            startind += 1
        elif quicksortarr[endind] > partitioner:
            endind -= 1
        else:
            swap(startind, endind)
            startind += 1
            endind -= 1
    swap(startind, ogendind)
    return startind

# def QuickSort(startind, endind):
#     if endind - startind <= 0:
#         return 
#     p = Partition(startind,endind)
#     QuickSort(0,p-1)
#     QuickSort(p+1,endind)
        
# QuickSort(0,len(quicksortarr)-1)
# print(quicksortarr)


# 3,3,5,6,7,10


def QuickSelect(startind, endind, n):
    if (endind - startind) <= 0:
        return quicksortarr[endind]
    p = Partition(startind,endind)
    if n < p:
        return QuickSelect(0,p-1,n)
    else:  
        return QuickSelect(p+1,endind,n)



print(QuickSelect(0,len(quicksortarr)-1, 9))