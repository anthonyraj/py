#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

#rev=' '.join([str(arr[i-1]) for i in range(len(arr),0,-1)])
rev=" ".join(map(str, arr[::-1]))

print(rev)
