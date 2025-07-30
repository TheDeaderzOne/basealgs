import sys
import math 
import random as rand

# The Miller Rabin Probabilistic Test for Primes

def flt(num, prime): 
    if pow(num, prime-1, prime) != 1:
        return False
    else: 
        return True

def primefunc(number):
    for _ in range(1000): 
        if flt(rand.randint(1,number-1), number) == False:
            return "Not Prime"
    return "Prime"
        
        
print(primefunc(41041))
        
    