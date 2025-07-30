from functools import cmp_to_key
import sys
import bisect
import math
from StringHashing import hashdescend2, substrhash

# template for hashing

modulo = (10**15)+37
base = 1009

# array of preprocessed polynomial powers under the modulo, using the pow() function

polynomialpowers = []

for i in range(10**5): polynomialpowers.append(pow(base,i,modulo))

# polynomial hash function

def hashdescend(string, powlist):
    powmount = len(string)-1; tot = 0
    for char in string:
        tot = (tot + ((ord(char) * powlist[powmount]) % modulo))%modulo
        powmount -=1
    return tot

# bisect function, that finds if a number exists in a list

def bisectin(arr,num):
    ind = bisect.bisect_left(arr,num)
    return ind < len(arr) and arr[ind] == num

#  this is the cyclic substring test

# Substring List

substrarr = []



# to retrieve a substring, from string[a ... b], use substrarr[b] - polynomialpowers[b-a+1]*substrarr[a-1]

# Usually, you have to binary search for numbers, from 1 to limit, something like this

# def binsearch(limitlen,func,string):
#     lo = 1
#     hi = limitlen+1
#     while lo != hi:
#         mid = (lo+hi)//2
#         if func(mid,string):
#             lo = mid+1
#         else:
#             hi = mid 
#     if hi == limitlen+1:
#         return limitlen
#     return lo


# Longest Common Substring of two substrings in O(nlogn)
# Same thing as the Longest Palindromic substring for a string and its reverse

string1arr = []
string2arr = []

def binsearch(limitlen,func,substrarr1,substrarr2):
    lo = 1
    hi = limitlen+1
    while lo != hi:
        mid = (lo+hi)//2
        if func(mid,substrarr1,substrarr2):
            lo = mid+1
        else:
            hi = mid 
    return lo-1

hashdescend2("bananas",string1arr)
hashdescend2("sananab",string2arr)

def searchLCS(size,stringarr1,stringarr2):
    hashset = set()
    for i in range(min(len(stringarr1),len(stringarr2))-size+1):
        set.add(hashset,substrhash(i,i+size-1,stringarr1))
        set.add(hashset,substrhash(i,i+size-1,stringarr2))
    if len(hashset) != (min(len(stringarr1),len(stringarr2))-size+1)*2:
        return True
    return False

print("The Longest Common Substring is of length " + str(binsearch(len("bananas"),searchLCS,string1arr,string2arr)))

# LPS, similar, but just switch around the bounds to this:

# switch around the bounds for palindromics

string1arr = []; string2arr = []

strz = "babad"

hashdescend2(strz,string1arr)
hashdescend2(strz[::-1],string2arr)

def searchLCS(size,stringarr1,stringarr2):
    hashset = set()
    for i in range(min(len(stringarr1),len(stringarr2))-size+1):
        # bounds switched
        set.add(hashset,substrhash(i,i+size-1,stringarr1))
        set.add(hashset,substrhash(len(strz)-1-(i+size-1),len(strz)-1-i,stringarr2))
    if len(hashset) != (min(len(stringarr1),len(stringarr2))-size+1)*2:
        return True
    return False

print("The Longest Palindromic Substring is of length " + str(binsearch(len(strz),searchLCS,string1arr,string2arr)))

# Longest Repeated Substring in O(nlogn)

str1 = []

def binsearch(limitlen,func,substrarr1):
    lo = 1
    hi = limitlen+1
    while lo != hi:
        mid = (lo+hi)//2
        if func(mid,substrarr1):
            lo = mid+1
        else:
            hi = mid 
    return lo-1

hashdescend2("ababcababc",str1)

def searchLRS(size,stringarr1):
    hashset = set()
    for i in range(len(stringarr1)-size+1):
        set.add(hashset,substrhash(i,i+size-1,stringarr1))
    if len(hashset) != (len(stringarr1)-size+1):
        return True
    return False

print("The Longest Repeating Substring has length " + str(binsearch(len("ababcababc"),searchLRS,str1)))

# LCP check

s1 = "prefixabc"
s2 = "prefihdef"
s1arr = []
s2arr = []

hashdescend2(s1,s1arr)
hashdescend2(s2,s2arr)

def binsearch(limitlen):
    lo = 0
    hi = limitlen+1
    while lo != hi:
        mid = (lo+hi)//2
        if s1arr[mid] == s2arr[mid]:
            lo = mid+1
        else:
            hi = mid 
    return lo-1

print("The longest common prefix index ends at index " + str(binsearch(min(len(s1),len(s2)))))

# then just look at the next letter to find the lcp

# Lexographically minimum cylic shifts

cyclicstring = "bananaban" * 2
cstringarr = []

hashdescend2(cyclicstring, cstringarr)

def binsearch(limitlen,startind1,startind2):
    lo = 0
    hi = limitlen+1
    while lo != hi:
        mid = (lo+hi)//2
        if substrhash(startind1,startind1+mid,cstringarr) == substrhash(startind2,startind2+mid,cstringarr):
            lo = mid+1
        else:
            hi = mid 
    return lo-1

def nextstr(startind1,startind2,midindex):
    if startind1+midindex+1 == len(cyclicstring):
        return startind1
    elif startind2+midindex+1 == len(cyclicstring):
        return startind2
    else:
        if ord(cyclicstring[startind1+midindex+1]) > ord(cyclicstring[startind2+midindex+1]):
            return startind2
        else:
            return startind1

initialsub = 0

for x in range(len(cyclicstring)//2 - 1):
    initialsub = nextstr(initialsub,x+1,binsearch(len(cyclicstring)//2,initialsub,x+1))

print("The Lexographically Minimum Cyclic Shift starts at index " + str(initialsub))


# "abacdfgdcaba", "aba"
# "abacdfgdcabba", "abba"
# "racecar", "racecar"
# "bananas", "anana"
# reformat it
# "#a#b#b#a#"

cyclicstring = "bananaban" * 2
cstringarr = []

hashdescend2(cyclicstring, cstringarr)

def binsearch(limitlen,startind1,startind2):
    lo = 0
    hi = limitlen+1
    while lo != hi:
        mid = (lo+hi)//2
        if substrhash(startind1,startind1+mid,cstringarr) == substrhash(startind2,startind2+mid,cstringarr):
            lo = mid+1
        else:
            hi = mid 
    return lo-1

def nextstr(startind1,startind2):
    midindex = binsearch(len(cyclicstring)//2,startind1,startind2)
    if startind1+midindex+1 == len(cyclicstring):
        return -1
    elif startind2+midindex+1 == len(cyclicstring):
        return 1
    else:
        if ord(cyclicstring[startind1+midindex+1]) > ord(cyclicstring[startind2+midindex+1]):
            return 1
        elif ord(cyclicstring[startind1+midindex+1]) == ord(cyclicstring[startind2+midindex+1]):
            return 0
        else:
            return -1

sortarr = [int(x) for x in range(len(cyclicstring)//2)]

sortarr.sort(key=cmp_to_key(nextstr))

print(sortarr)

# Number of sub-palindromes in O(nlogn)

palindrome = "#a#b#c#b#c#b#a#"
palindromereverse = palindrome[::-1]

p1arr = []; p2arr = []; manacherarr = []

hashdescend2(palindrome,p1arr)
hashdescend2(palindromereverse,p2arr)

def binsearch(limitlen,center):
    lo = 1
    hi = limitlen+1
    while lo != hi:
        mid = (lo+hi)//2
        if substrhash(center-mid+1,center+mid-1,p1arr) == substrhash(len(palindrome)-(center+mid-1)-1,len(palindrome) - (center-mid+1) - 1,p2arr):
            lo = mid+1
        else:
            hi = mid 
    return lo-1

for i in range(len(palindrome)):
    manacherarr.append(binsearch(min(i+1,len(palindrome)-i),i))
    
print(manacherarr)