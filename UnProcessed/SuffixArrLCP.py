import math

string1 = 'ushers'

#Suffix Array


def CountingSortArrStr(alphabetlength,string):
    countingsortarr = [[] for _ in range(alphabetlength)]; finalsortarr = []
    equivalenceclassarr = [0]*len(string)
    stringarr = list(string); equivalenceclassnumber=0

    for k in range(len(string)):
        charnum = ord(stringarr[k])-ord('a')
        if charnum >= 0:
            countingsortarr[charnum].append(k)
        else:
            finalsortarr.append(k)
            equivalenceclassarr[k]=equivalenceclassnumber
            equivalenceclassnumber+=1
        
    for x in range(alphabetlength):
        if len(countingsortarr[x])>0:
            for k in countingsortarr[x]:
                finalsortarr.append(k)
                equivalenceclassarr[k]=equivalenceclassnumber
            equivalenceclassnumber+=1
    
    return equivalenceclassarr

def CountingSortArrEquiv(equivalencelist,currentcyclicstringlen,stringlen):

    tesslist = []; originalarr = []; zeg=[[] for _ in range(stringlen)]

    for i in range(stringlen):
        newsuffixind = (i + (currentcyclicstringlen>>1))%stringlen
        originalarr.append((equivalencelist[i], equivalencelist[newsuffixind]))
        zeg[equivalencelist[newsuffixind]].append(i)

    for x in range(stringlen):
        if len(zeg[x])>0:
            for b in zeg[x]:
                tesslist.append(b)

    zeg=[[] for _ in range(stringlen)]

    for i in range(stringlen):
        zeg[equivalencelist[tesslist[i]]].append(tesslist[i])

    tesslist = []

    for x in range(stringlen):
        if len(zeg[x])>0:
            for b in zeg[x]:
                tesslist.append(b)
    
    equivalencelist = [0]*stringlen; timer = 0

    for x in range(len(tesslist)-1):
        if originalarr[tesslist[x]]!=originalarr[tesslist[x+1]]:
            timer+=1
        equivalencelist[tesslist[x+1]]=timer

    return (tesslist,equivalencelist)

lcpaccess = []

def SuffixArray(alphabetlen,string):
    equivfir = CountingSortArrStr(alphabetlen,string)
    lcpaccess.append(equivfir)
    length = 2
    stringconst = 2**math.ceil(math.log(len(string),2))
    while length<=stringconst:
        besslist,equivfir = (CountingSortArrEquiv(equivfir,length,len(string))) 
        lcpaccess.append(equivfir)  
        length*=2

    return besslist

suffixarrsy = SuffixArray(26,'banana$')

print(lcpaccess)
print(suffixarrsy)

def lcpineff(suffixnum1,suffixnum2,str):
    maxlength = max(len(str)-suffixnum1,len(str)-suffixnum2)
    const = math.ceil(math.log(maxlength,2))
    diff = len(lcpaccess)-const
    newconst = int(const)-1; lcplength = 0

    for x in range(-(1+diff),-(len(lcpaccess)+1),-1):
        if lcpaccess[x][suffixnum1]==lcpaccess[x][suffixnum2]:
            lcplength+=(2**newconst)
            suffixnum1=(suffixnum1+(2**newconst))%len(str); suffixnum2=(suffixnum2+(2**newconst))%len(str)
        newconst-=1
    return lcplength

def lcparray(equivalencelist,suffixarr):
    lcparr = [0]*len(suffixarr); maxh=0
    for i in range(len(suffixarr)):
        if equivalencelist[i]-1>=0:
            lcparr[equivalencelist[i]] = lcpineff((suffixarr[equivalencelist[i]-1]+maxh)%len(suffixarr),(i+maxh)%len(suffixarr),suffixarr)+maxh
            maxh = max(0,lcparr[equivalencelist[i]]-1)
    return lcparr

print(lcparray(lcpaccess[-1],suffixarrsy))

#(old suffix, new cyclic suffix)
#first sort the new, then sort the old
#stringlen is used as the limit, because that's the limit of the equivalenceclassnumber

#new cylic suffix == i + (currentcyclicstringlen/2) for i in range stringlenth

#equivalence classes: