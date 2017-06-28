# twin arrays
#https://www.hackerrank.com/contests/w33/challenges/twin-arrays

def twin_arrays(a1,a2):
    m1 = min(a1)
    print("m1=",m1)
    m2 = min(a2)
    print("m2=",m2)
    s1 = m1 + m2
    print("s1=",s1)
    if a1.index(m1) != a2.index(m2):
        return s1

    s2 = 0
    for x in a1:
        for y in a2:
            if a1.index(x) != a2.index(y):
                if s2==0: s2 = x + y
                elif x+y < s2: s2 = x + y
    print("s2=",s2)
    return s2

#n = int(input().strip())
#row1 = [int(x) for x in input().strip().split()]
#row2 = [int(x) for x in input().strip().split()]

n = 100
row1 = [x for x in range(1,100)]
row2 = [x for x in range(1,1000,10)]
#row2 = [x for x in reversed(row1.copy())]

result = twin_arrays(row1,row2)
print(result)
