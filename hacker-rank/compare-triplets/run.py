#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    a = [a0,a1,a2]
    b = [b0,b1,b2]
    a_score = []
    b_score = []
    count = len(a)
    for i in range(count):
        if (a[i] > b[i]):
            a_score.append(1)
        elif (b[i] > a[i]):
            b_score.append(1)
        elif (a[i] == b[i]):
            pass
    return [len(a_score), len(b_score)]
        
    
a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
