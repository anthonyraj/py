#breaking-best-worst-ends
#!/bin/python3
"""
INPUT
9
10 5 20 20 4 5 2 25 1
OUTPUT
2 4

INPUT
10
3 4 21 36 10 28 35 5 24 42
OUTPUT
4 0

"""
import sys

def getRecord(s):
    # Complete this function
    max1=max(s)
    best=0
    best_val=-1
    worst=0
    worst_val=-1
    for item in range(len(s)):
        
        if (item != len(s)-1):
            #print (item)
            current = s[item]
            next1 = s[item+1]
            
            if (worst_val == -1):
                worst_val = current
            if (best_val == -1):
                best_val = current
                
            #print ("current=",current," | next1=",next1," | best_val=",best_val," | worst_val=",worst_val," | worst=",worst)
            if (next1 > current):
                if (next1>best_val):
                    best_val = next1
                    best +=1
                #print ("found best")
            elif (next1 < current):
                if (next1<worst_val):
                    worst_val = next1
                    worst +=1
                #print ("found worst")
    return best,worst

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
