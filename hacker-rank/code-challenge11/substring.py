#https://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Data/toBaseTen.html

#!/bin/python3

import sys

def convert_to_base(x,b):
    #convert from base b to base 10
    if (x == '0'):
        return 0
    c = [y for y in x]
    c.reverse()
    x10=0
    
    for i in range(len(c)):          
        if c[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            y = int(c[i])*(int(b)**i)
            #print ("y=",y)
        else :
            y = y + (9 + ord(c[i]))*(b**i) 
            #print ("y=",y)
        x10 += y
         
    #print ("c=",c," x10=",x10)
    return x10

def getMagicNumber(s, k, b, m):
    # Complete this function
    
    list,slist = [], []
    for item in s:slist.append(item)
        
    for i in range(len(slist)):
        start = i; end=i+k
        if (end<=len(slist)):
            list.append(slist[start:end])
        else:
            break
    res = 0
    for x in list:
        x10 = convert_to_base(x,b)
        res += x10%m
        
    return res

#s = input().strip()
#k, b, m = input().strip().split(' ')
#k, b, m = [int(k), int(b), int(m)]
#result = getMagicNumber(s, k, b, m)
#

#Test1
s='12212'
k, b, m = 3, 3, 5
result = getMagicNumber(s, k, b, m)
print(result)

#Test2
s='111101'
k, b, m = 4, 2, 15
result = getMagicNumber(s, k, b, m)
print(result)

#Test3
s='0111'
k, b, m = 2, 10, 100
result = getMagicNumber(s, k, b, m)
print(result)

