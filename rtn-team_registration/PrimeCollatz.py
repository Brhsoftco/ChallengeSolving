#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def getPrimes(start, end):
    allPrimes = []
    
    for num in range(start, end, 2):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            allPrimes.append(num)
            
    return allPrimes
            
def filterPrimesWithCollatz(primes):
    collatzIterations = []
    
    for p in primes:
        #data calculation
        c = collatz(p)
        collatzIterations.append(c)
        
        #print outcome
        print((str(p) + ": " + str(c) + " iterations"))
    
    return collatzIterations

def collatz(n):
    iterations = 0
    
    while n > 1:
        iterations += 1
        
        if (n % 2):
            # n is odd
            n = 3 * n + 1
        else:
            # n is even
            n = n // 2
    
    return iterations

def averageArray(arr):
    num = len(arr)
    arrSum = 0
    
    for i in arr:
        arrSum += i
        
    return round(arrSum / num)

def doWork():
    #prime bounds
    start = 3
    end = 900
    
    #all prime numbers
    p = getPrimes(start, end)
    
    #get all collatz iterations of prime numbers
    f = filterPrimesWithCollatz(p)
    
    #calculate the average of all iterations
    a = averageArray(f)
    
    #print answer
    print("\nAnswer (average of iterations): " + str(a))
    
#execute the script
doWork()
