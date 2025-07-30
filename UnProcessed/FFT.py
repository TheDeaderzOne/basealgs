import math
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