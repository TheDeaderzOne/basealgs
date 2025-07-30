import sys
import math

modulo = (10**15) + 37
base = 1009
# array of preprocessed polynomial powers under the modulo, using the pow() function
polynomialpowers = []
for i in range(10**5):
    polynomialpowers.append(pow(base, i, modulo))
# polynomial hash function


def hashdescend(string, powlist):
    powmount = len(string) - 1
    tot = 0
    for char in string:
        tot = (tot + ((ord(char) * powlist[powmount]) % modulo)) % modulo
        powmount -= 1
    return tot


def RabinKarp(test, pattern):
    matchedindices = []
    beginstr = test[: len(pattern)]
    patternnum = hashdescend(pattern, polynomialpowers)

    if len(pattern) > len(test):
        return 0

    testnum = hashdescend(beginstr, polynomialpowers)
    if testnum == patternnum:
        matchedindices.append(0)

    for i in range(len(test) - len(pattern)):
        testnum = (modulo + testnum - ((ord(test[i]) * polynomialpowers[len(pattern) - 1]) % modulo)) % modulo
        testnum = (base * testnum) % modulo
        testnum = (testnum + ord(test[i + len(pattern)])) % modulo
        if testnum == patternnum:
            matchedindices.append(i + 1)

    return matchedindices


print(RabinKarp("ababcabcababcabc", "abc"))
print(RabinKarp("abcdefg", "xyz"))
print(RabinKarp("match", "match"))
print(RabinKarp("aaaaa", "a"))
print(RabinKarp("abcdefabcxyz", "xyz"))
print(RabinKarp("hello world", "world"))
print(RabinKarp("hello world", "World"))
print(RabinKarp("abcabc", "cab"))


substrarr = []


# This generates the "prefix" hash array to use


def hashdescend2(string, strarr):
    strarr.append(ord(string[0]))
    for i in range(len(string) - 1):
        strarr.append((strarr[i] * base + ord(string[i + 1])) % modulo)


print(hashdescend2("xyzabc", substrarr))

# This queries the string hash for any substring in O(1) with O(n) preprocessing


def substrhash(a, b, strarr):
    if a > 0:
        return (strarr[b] - ((polynomialpowers[b - a + 1] * strarr[a - 1]) % modulo) + modulo) % modulo
    else:
        return strarr[b]


# test cases

print(substrhash(2, 5, substrarr), hashdescend("zabc", polynomialpowers))
