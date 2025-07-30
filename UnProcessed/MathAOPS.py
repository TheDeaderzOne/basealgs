import sys
import math
import time
import cmath


sys.setrecursionlimit(10**5)

#Catalan Numbers

sequencearr = [1,1]

pairslist = [[0,0]]

def CatalanNumbers(ceasepoint,seqarr,prlist):
    ju = time.time()
    for _ in range(ceasepoint):
        teg = 0
        for x in prlist:
            x[1]+=1
        if (len(seqarr)-1)&1 == 0:
            prlist.append([int((len(seqarr)-1)/2),int((len(seqarr)-1)/2)])
        for x in prlist:
            if x[0]!=x[1]:
                teg+=int(2*(seqarr[x[0]])*(seqarr[x[1]]))
            else:
                teg+=int((seqarr[x[0]])*(seqarr[x[1]]))
        seqarr.append(teg)
    jd = time.time()
    hu = jd-ju
    return (seqarr, hu)

print(CatalanNumbers(100,sequencearr,pairslist))

#Simpson's

#e^-x^2

# math.exp(-1*(num**2))

def functionval(num):
    return (1/(math.log(num,math.exp(1))))

def Simpsons(xwidth,start,end):

    sumwalue = 0

    numintervals = abs((start-end)/xwidth)
    intnums = int(numintervals)

    for _ in range(intnums):
        
        endpoint = start+xwidth

        midpoint = start+(xwidth/2)

        sumwalue+=(1*functionval(start)+4*functionval(midpoint)+1*functionval(endpoint))

        start+=xwidth

    if start < end:
        endpoint = end

        midpoint = start+((end-start)/2)

        sumwalue+=(1*functionval(start)+4*functionval(midpoint)+1*functionval(endpoint))

    sumwalue*=(xwidth/6)

    return sumwalue


print(Simpsons(.001,3,4))


#Newton's Method of Roots (Let's use Quartic Polynomials)

#[1,1,9,2,-6]

polynomial = [float(x) for x in input().split(",")]

polynomiallistings = []

for h in range(len(polynomial)):
    tork = ''
    if polynomial[h]==1:
        pass
    else:
        tork = str(polynomial[h])
    if tork == '0':
        pass
    else:

        if h==len(polynomial)-1:
            polynomiallistings.append(str(tork))

        else:
            polynomiallistings.append(str(tork+"x^"+str(len(polynomial)-1-h))+" + ")


polynomiallistings[-1].replace("+","")

functionname = "".join(polynomiallistings)

CauchysBound = 1+(int(max(polynomial)/polynomial[0]))

deriv = []

for x in range(len(polynomial)-1):
    deriv.append(polynomial[x]*(len(polynomial)-1-x))

def derivf(delist,highestpower,j):
    number = 0
    for x in range(highestpower):
        number+=delist[x]*((j)**(highestpower-x))
    number+=delist[-1]
    return number

def normalf(delist,highestpower,j):
    number = 0
    for x in range(highestpower):
        number+=delist[x]*((j)**(highestpower-x))
    number+=delist[-1]
    return number

def NewtonRoots(iterations,initval):

    for _ in range(iterations):
        initval -= (normalf(polynomial,len(polynomial)-1,initval)/derivf(deriv,len(deriv)-1,initval))
    if round(normalf(polynomial,len(polynomial)-1,initval),3)==0:
        return initval
    else:
        return 't'

rootlist = set()

intervallength = 0.05
io = abs(CauchysBound)

while io>-1*abs(CauchysBound):

    newroot = NewtonRoots(32,io)
    
    io-=intervallength
    if newroot != 't':
        rootlist.add(round(newroot,10))

print("The zeroes of this function " +"["+functionname+"]  are  "+ str(rootlist))


#Chinese Remainder Thereom

#x=3 mod 5, x=4 mod 7, x=2 mod 3

equationslist = [(3,5),(2,7),(2,3)]

answer = 0

totalmoduli = 1

for x in equationslist:
    totalmoduli*=x[1]

for x in range(len(equationslist)):
    mot = int(totalmoduli/equationslist[x][1])
    answer+=(equationslist[x][0]*mot*((mot**(equationslist[x][1]-2))%equationslist[x][1]))

print(str(answer%totalmoduli)+" mod "+str(totalmoduli))

#MEX

#Most Games use Directed Graphs via toposort

#MEX (Segment Tree)




#update

#min

#GameMatrix

Game1 = [
    [1,1,0,1,1],
    [0,1,1,1,0],
    [1,1,0,1,1],
    [0,1,1,1,1],
    [1,1,1,1,1]
]

MexLim = (2*len(Game1))-1

mexconstcomp = 2**(MexLim+1)-1
VisitedGame1 = [
    [-1,-1,math.inf,-1,-1],
    [math.inf,-1,-1,-1,math.inf],
    [-1,-1,math.inf,-1,-1],
    [math.inf,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1]
]

LeftRightList = [
    [[0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0],[0,0],[0,0],[0,0],[0,0]]
]

def GameDFS(startnode1,startnode2,visitlist,gameadj,leftrightlist,mexconst):
    
    if startnode1 and startnode2 <= 0:
        pass
    
    elif startnode1 <= 0:
        leftrightlist[startnode1][startnode2][1]|=(leftrightlist[startnode1][startnode2-1][1])
    elif startnode2 <= 0:
        leftrightlist[startnode1][startnode2][0]|=(leftrightlist[startnode1-1][startnode2][0])
    else:
        leftrightlist[startnode1][startnode2][1]|=(leftrightlist[startnode1][startnode2-1][1])
        leftrightlist[startnode1][startnode2][0]|=(leftrightlist[startnode1-1][startnode2][0])

    if (startnode1 and startnode2 <= 0) or (startnode2 <= 0) or (startnode1 <= 0) or (visitlist[startnode1-1][startnode2] != -1 and visitlist[startnode1][startnode2-1] != -1):

        mexlist = (leftrightlist[startnode1][startnode2][1])|(leftrightlist[startnode1][startnode2][0])

        newvar = mexlist^mexconst
        
        teccy = 0

        while newvar>0:
            newvar>>=1
            teccy+=1
        teccy-=1
 
        leftrightlist[startnode1][startnode2][1]|=(2**teccy)
        leftrightlist[startnode1][startnode2][0]|=(2**teccy)
        visitlist[startnode1][startnode2]=((2*len(gameadj))-1)-teccy

        if startnode2 < len(gameadj)-1 and visitlist[startnode1][startnode2+1] == -1 and gameadj[startnode1][startnode2+1]==1:
            GameDFS(startnode1,startnode2+1,visitlist,gameadj,leftrightlist,mexconst)
        if startnode1 < len(gameadj)-1 and visitlist[startnode1+1][startnode2] == -1 and gameadj[startnode1+1][startnode2]==1:
            GameDFS(startnode1+1,startnode2,visitlist,gameadj,leftrightlist,mexconst)

    return (leftrightlist)


for x in range(len(Game1)):
    for y in range(len(Game1)):
        if VisitedGame1[x][y]==-1:
            GameDFS(x,y,VisitedGame1,Game1,LeftRightList,mexconstcomp) 

print(VisitedGame1)
#Rewrite all Games as graphs

#Stars and Bars

def Combinations(n,k):
    num = 1
    
    for ind in range(k):
        num*=(n-k+ind+1)/(ind+1)

    return int(round(num,1))


#Stars and Bars

def NormalStarsandBars(equality,termnum,zeropossibility):
    if zeropossibility == False:
        return Combinations(equality-1,termnum-1)
    else:
        return Combinations(equality+termnum-1,termnum-1)

print(NormalStarsandBars(7,3,False))
print(NormalStarsandBars(7,3,True))

#5+3x+2x^2+x^3

#FFT (Fast Fourier Transform)]
examplepolynomial = [1,3,9,5]

examplepolynomial2 = [1,3,3,1]

def FFTpolynomialrefitting(polynomiallist,poly2):

    totallength = len(polynomiallist)+len(poly2)-1

    huj = totallength

    tehu = 0

    while (huj>>1) > 0:
        huj>>=1
        tehu+=1
    tehu+=1
    for _ in range((2**tehu)-len(polynomiallist)):
        polynomiallist.append(0)
    
    for _ in range((2**tehu)-len(poly2)):
        poly2.append(0)

    highdeg = 2**tehu

    return highdeg


# FFTpolynomialrefitting(examplepolynomial)

def FFT(polynomiallist,inverts):

    listlen = len(polynomiallist)
    if listlen == 1:
        return polynomiallist
    
    if inverts == False:
        compnum = math.cos(((2*math.pi)/listlen))+(1j*math.sin(((2*math.pi)/listlen)))
    else:
        compnum = ((math.cos(((-2*math.pi)/listlen))+(1j*(math.sin(((-2*math.pi)/listlen))))))

    polyodd,polyeven = [],[]

    for x in range(listlen):
        if x&1 == 0:
            polyeven.append(polynomiallist[x])
        else:
            polyodd.append(polynomiallist[x])
    
    even,odds = FFT(polyeven,inverts), FFT(polyodd,inverts)

    fork = [0]*listlen
    
    for g in range(int(listlen/2)):
        fork[g] = (even[g] + 0j) + ((compnum**g)*odds[g])
        fork[g+int(listlen/2)] = (even[g] + 0j) - ((compnum**g)*odds[g])
    
    return fork



def PolynomialMultiplication(polynomial1,polynomial2):

    highestdegree = FFTpolynomialrefitting(polynomial1,polynomial2)

    poly1 = FFT(polynomial1,False)
    poly2 = FFT(polynomial2,False)

    newlist = [0]*(highestdegree)

    for x in range(highestdegree):
        newlist[x]=poly1[x]*poly2[x]

    hdy = FFT(newlist,True)

    hdy = [x/highestdegree for x in hdy]

    for ele in range(len(hdy)):
        hdy[ele] = round(hdy[ele].real,6) + round(hdy[ele].imag,6)*1j

        if hdy[ele].imag == 0:
            hdy[ele]=hdy[ele].real
 
    for _ in range(len(hdy)):
        if hdy[-1]!=0:
            break
        else:
            hdy.pop(-1)
        
    return hdy

N = 16
t = list(range(N))
signal = [math.sin((2*math.pi*1*t_i)/N) + math.sin((2*math.pi*4*t_i)/N + 0.5) for t_i in t]
for x in range(240):
    signal.append(0)

def SignalProcessing(signallist):
    hu = FFT(signallist,True)

    for ele in range(len(hu)):
        #complex module
        # hu[ele] = round(hu[ele].real,6) + round(hu[ele].imag,6)*1j

        # if hu[ele].imag == 0:
        #     hu[ele]=hu[ele].real
        
        #distance module
        hu[ele]=round((((hu[ele].real**2)+(hu[ele].imag**2))**.5),6)


    
    return hu

print(PolynomialMultiplication(examplepolynomial,examplepolynomial2))

print(SignalProcessing(signal))