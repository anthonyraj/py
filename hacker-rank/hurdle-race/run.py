# hurdle-race
#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
# your code goes here

diff = 0
for item in height:
    if (item > k and diff < item -k):
        diff= item - k
        
print (diff)
