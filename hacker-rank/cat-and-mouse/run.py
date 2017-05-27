#!/bin/python3
"""
3
1 2 3
1 3 2
2 1 3
Cat B
Mouse C
Cat A

"""
import sys

def who_caught_the_mouse(a,b,c):
    result = ''
    if (abs(c-b)>abs(c-a) and abs(c-a)!=abs(c-b)):
        result = 'Cat A'
    elif (abs(c-a)>abs(c-b) and abs(c-a)!=abs(c-b)):
        result = 'Cat B'
    elif (abs(c-a)==abs(c-b)):
        result = 'Mouse C'
    return result

q = int(input().strip())
list = []
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    list.append((x,y,z))

for (x,y,z) in list:
    print (who_caught_the_mouse(x,y,z))
