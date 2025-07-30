import math
import sys

sys.setrecursionlimit(10**5)

def division(x,y):
    assert y!=0, "Divide By 0 Error"
    return x/y

# print(division(6,0))
print(division(6,2))

def trydiv(x,y):
    try:
        result = x/y
    except:
        raise Exception('div by 0')
    return result


# print(trydiv(5,0))

trydiv(5,6)
print(trydiv(6,5))

def modulo(x,y=2):
    return x % y

print(modulo(5))

class Bird:

    def fly(self):
        print('This Bird is absolutely soaring')
    
class Chicken:
    def fly(self):
        print('This Bird is struggling')

def flying(obj):
    obj.fly()

flying(Chicken())
flying(Bird())


count = 0

def countess():
    global count
    count=5
def getcount():
    global count
    count+=5
    return count
countess()
print(getcount())



class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.math = 'Linear Algebra'
    def __repr__(self):
        return (self.x,self.y)
    def __add__(self,point1):
        return (self.x+point1.x,self.y+point1.y)
    def mathtype(self):
        print(self.math)

firstpoint = point(5,5)
secondpoint = point(3,4)
secondpoint.mathtype()

a = [5]

b = [5]

print(a is b)

c = 5
d = 5

print(c is d)



class Animal:
    def __init__(self,age,color):
        self.age = age
        self.color = color
    def screech(self):
        print('TTTTTTT')
    def scream(self):
        print("ah")

class Dog(Animal):
    def __init__(self,age,color):
        self.age = age
        self.color = color
    def screech(self):
        super().screech()
    def scream(self):
        print("woof")

dog = Dog(17,'blue')
dog.screech()
dog.scream()


key = ["W","X","Y","Z"]

def perms(length,inputlist,keyslist):
    if length == 4:
        print(inputlist)
    else:
        for x in range(len(keyslist)):
            tex = keyslist[x]
            inputlist.append(tex)
            keyslist.pop(x)
            perms(length+1,list(inputlist),list(keyslist))
            inputlist.pop()
            keyslist.insert(x,tex)

print(perms(0,[],key))

lissy = [1,2,4,3,2,8,3,5,1,6,7,2]
def checkmin(start,stop):
    if start == stop:
        return lissy[start]
    bisect = (start+stop)//2
    return min(checkmin(start,bisect),checkmin(bisect+1,stop))

print(checkmin(0,len(lissy)-1))

def issorted(stop1,start2,listarr):
    if type(stop1) == bool or type(start2) == bool:
        return (False, False)
    if listarr[stop1]>listarr[start2]:
        return (False, False)
    return (stop1,start2)

def sortcheck(start,stop,listarr):
    if start == stop:
        return (start,stop)
    bisect = (start+stop)//2
    return issorted(sortcheck(start,bisect,listarr)[1],sortcheck(bisect+1,stop,listarr)[0],listarr)

print(sortcheck(0,len(lissy)-1,lissy))

testarr = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10]

def merge(list1,list2):
    newarr = []; pointer1 = 0; pointer2 = 0

    while pointer1<len(list1) and pointer2<len(list2):
        if list1[pointer1]<=list2[pointer2]:
            newarr.append(list1[pointer1])
            pointer1+=1
        else:
            newarr.append(list2[pointer2])
            pointer2+=1

    newarr.extend(list1[pointer1:]); newarr.extend(list2[pointer2:])
    return newarr

def mergesort(listarr):
    if len(listarr)==1:
        return listarr
    
    bisect = len(listarr)//2

    return merge(mergesort(listarr[:bisect]),mergesort(listarr[bisect:]))

print(mergesort(testarr))


def lettersearch(string,start,stop,keyletter):
    if start == stop:
        if keyletter == string[start]:
            return 1
        return 0
    
    bisect = (start+stop)//2

    return lettersearch(string,start,bisect,keyletter)+lettersearch(string,bisect+1,stop,keyletter)

print(lettersearch('enemeye',0,len('enemeye')-1,'e'))

def subsets(listarr,kest,totalarr):

    if len(listarr)==0:
        totalarr.append(kest)
        return kest

    kest.append(listarr[0])
    listarr.pop(0)
    subsets(list(listarr),list(kest),totalarr)
    kest.pop()
    subsets(list(listarr),list(kest),totalarr)
    return totalarr
    
print(subsets(key,[],[]))

def permmodular(listarr):
    if len(listarr)==0:
        return [[]]
    totallist = []

    for i in range(len(listarr)):
        current = listarr[i]
        newlist = listarr[:i]+listarr[i+1:]
        for x in permmodular(newlist):
            totallist.append([current]+x)
    return totallist

def subsetmodular(listarr):
    
    if len(listarr)==0:
        return [[]]
    totalite = []
    firstelement = listarr[0]
    rest = subsetmodular(listarr[1:])
    for x in rest:
        totalite.append([firstelement]+x)
        totalite.append(x)
    
    return totalite

print(permmodular(key))
print(subsetmodular(key))

#use recursion in the modular method
listy = ['4','0','0','0']

def complement(numlist,tes):
    
    if len(numlist)==1:
        if tes:
            return (9-int(numlist[-1]))%10
        else:
            return (10-int(numlist[-1]))%10
    if tes:
        firstnum = (9-int(numlist[-1]))%10
    else:
        firstnum = (10-int(numlist[-1]))%10
    if firstnum!=0:
        tes = True
    secondnum = complement(numlist[:len(numlist)-1],tes)
    
    return 10*secondnum + firstnum

print(complement(listy,False))


#Think about recursion legit, it can be just a divide and conquer in secret, with divides everywhere

def foo():
    return 5

x = foo()
y = foo



def couponify(stringsy):
    if len(stringsy)<4:
        return ''
    if len(stringsy)==4:
        return stringsy.upper()
    first = stringsy[:4].upper()
    second = couponify(stringsy[4:])
    if len(second)>0:
        return first + "-"+second
    else:
        return first

print(couponify('KBSH8'))


# def insert(num,listarr):
#     zes = 0
#     if len(listarr)<=1:
#         return listarr
    
#     first = [listarr[0]]
#     if first[0]>=num and zes == 0:
#         zes+=1
#         first = [num,listarr[0]]
#     second = insert(num,listarr[1:])
    
#     return first + second

# print(insert(3,[1,2,3,7]))

#LOL TAKE ADVANTAGE OF THE RECURSION BUILT IN WHILE ITERATING

def oddlist(listicle):
    if len(listicle)<1:
        return []
    if listicle[0]%2 == 0:
        return oddlist(listicle[1:])
    else:
        return [listicle[0]]+oddlist(listicle[1:])
    

# print(oddlist([4,3,5,6,3,1,2,4]))


def emitvowels(stringsy):
    counter = 0
    vowellist = 'aeiou'
    for x in stringsy:
        if x in vowellist:
            yield x
        elif x == 'y' and counter > 0:
            yield x
        counter+=1

for vowel in emitvowels("examination"):
    print(vowel)

def fold_head(input,n):
    pass



# def insert(nums,x):
#     if len(nums)==0:
#         return [x]
#     if len(nums)==1:
#         return nums
#     if nums[0]>=



