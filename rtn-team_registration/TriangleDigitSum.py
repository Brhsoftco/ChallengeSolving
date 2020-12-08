#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def doWork():
    #loop bounds
    start = 200
    end = 1800
    
    #digit sum must equal this number
    limit = 10
    
    #used for average calculation
    sumOfAllMatches = 0
    numOfAllMatches = 0
    
    for i in range(start, end + 1):
        #calculate T[n]
        t = (i ** 2 + i) // 2
        
        #calculate digit sum
        d = digitSum(t)
        
        #verify
        if (d == limit):
            sumOfAllMatches += t
            numOfAllMatches += 1
            
            print("Digit sum correct: " + str(t))
         
    avg = math.floor(sumOfAllMatches / numOfAllMatches)     
    
    print("\nAnswer (average of matched triangle numbers): " + str(avg))

def digitSum(n):
    r = 0
    while n:
        (r, n) = (r + n % 10, n // 10)
    return r

#execute the script
doWork()
