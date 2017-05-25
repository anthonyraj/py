#!/bin/python
#https://www.hackerrank.com/challenges/divisible-sum-pairs

import sys

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int, raw_input().strip().split(' '))
# write your code here
def cal(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if (i!=j and i<j and (a[i]+a[j])%k==0 ):
                #print a[i],a[j]
                count += 1
            else: pass
    return count

print cal(a)
