# Regex
# https://www.hackerrank.com/challenges/30-regex-patterns/problem
import re
import sys

#m = re.search('(?<=abc)def','abcdef')
#print(m.group(0))

def search_pattern(data):
    res = []
    pat = r'[\w.-]@gmail.com'
    for item in data:
        #print(item)
        match = re.search(pat,item[1])
        if match:
            res.append(item[0])
    return sorted(res)

N = int(input().strip())
data = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    data.append((firstName,emailID))

#print(data)
res = search_pattern(data)
for item in res: print(item)
