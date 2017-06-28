# lowest triangle
#https://www.hackerrank.com/contests/infinitum18/challenges/lowest-triangle

def get_height(base,area):
    #area of triangle = 0.5*b*h
    height = 0
    if (base>0):
        height = 2*area/base
    return height

b,a = [int(x) for x in input().strip().split(' ')]
print("base b=",b)
print("area a=",a)
h = get_height(b,a)
print("height h=",h)
