# Bries Drawing book
# https://www.hackerrank.com/challenges/drawing-book?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

import sys

# not effective
def binary_search(l,p,count=0):
    #l=range(n)
    if (len(l)<=2 and (p in l)):
        return count
    else:
        if p > l[n/2]:
            count +=1
            #binary_search([len(l)/2:n],p,count)
        if p < l[n/2]:
            count +=1
            #binary_search([0:len(l)/2]),p,count)

def traverse_from_front(n,p):
    m = 0    
    if p%2==0: m=(p//2)
    elif (p-1)%2==0: m=((p-1)//2)
    return m

def traverse_from_back(n,p):
    m = 0
    s = n
    while (n/2>=p):
        s -= 1
        m+=1
        if s%p==0:
            return m
        elif (s-1)%p==0:
            return m
    return m

def solve(n, p):
    # Complete this function
    m = 0
    if p == 1 or p == n: return 0 
    if p<n/2:
        m = traverse_from_front(n,p)
    if p>n/2:
        m = traverse_from_back(n,p)
    
    return m

n = int(input().strip())
p = int(input().strip())

result = solve(n, p)
print(result)

#result = binary_search(range(n),p)
