import sys

binheap = []

def swap(a,b):
    temp = binheap[a]
    binheap[a] = binheap[b]
    binheap[b] = temp

def insert(num):
    binheap.append(num)
    currentind = len(binheap)-1
    while (currentind-1)//2 >=0:
        if binheap[(currentind-1)//2] > binheap[currentind]:
            swap((currentind-1)//2, currentind)
            currentind = (currentind-1)//2
        else:
            break

# def heapify():
#     pass

def popfirst():
    newfirstelement = binheap.pop(-1)
    if len(binheap)>0:
        var = binheap[0]
        binheap[0] = newfirstelement
    currentind = 0
    while 2*currentind+1 < len(binheap):
        if binheap[2*currentind+1]<binheap[currentind]:
            swap(2*currentind+1,currentind)
            currentind = 2*currentind+1
        elif 2*currentind+2 < len(binheap) and binheap[2*currentind+2]<binheap[currentind]:
            swap(2*currentind+2,currentind)
            currentind = 2*currentind+1
        else:
            break

            
insert(9)
insert(1)
insert(10)
insert(3)
insert(12)
insert(6)
insert(5)
insert(4)
insert(7)
popfirst()
print(binheap)
