#!/bin/python3

import sys

def solve(a):
    # Complete this function
    half = int(len(a)/2)
    count1 = 0
    count2 = 0

    for i in range(len(a)):
        if (i <half):
            print (a[i])
            count1 += a[i]
        elif (i >=half):
            print (a[i])
            count2 += a[i]
            
    diff = 0
    flag = ''
    if (count1-count2 >0):
        diff += (count1-count2)
        flag = "count2"
    elif (count1-count2 <0):
        diff += (count2-count1)
        flag = "count1"

    return diff
    
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = solve(a)

#a = [1,2,3,4,5,1]
#a = [1,2,1,2,1,3]
#sresult = solve(a)

print(result)
