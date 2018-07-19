"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5},
you could climb 1, 3, or 5 steps at a time.
"""

def  climb(n):
    if (n == 0 or n == 1): return 1
    if (n == 2): return 2

    count = 0
    if (n > 2):
        count = climb(n-1) + climb(n-2)
        return count

def  climb_x(n,x):
    if (n == 0): return 1

    total = {}
    total[0] = 1
    #print "n=",n
    for step in range(1,n):
        #print "step=",step
        count = 0
        for i in x:
            if step-i >= 0:
                count += total[step-i]
        total[step]= count
    print total
    return total[n-1]

def run(n):
    print "n = ",n," count = ",climb(n)

def run1(n,x):
    print "n = ",n, "x = ",x," count = ",climb_x(n,x)

run(2)
run(3)
run(4)
run(5)
run(6)
run(7)

x=[1,3,5]
run1(3,x)
run1(5,x)
x = [5,10,15]
run1(100,x) # wrong result
