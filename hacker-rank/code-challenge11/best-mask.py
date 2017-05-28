#best mask
#https://www.hackerrank.com/contests/world-codesprint-11/challenges/best-mask
#https://en.wikipedia.org/wiki/Bitwise_operation#AND
#https://stackoverflow.com/questions/699866/python-int-to-binary
#!/bin/python3

import sys

# bitwise AND between ai & x is >0
# no. of 1s in bin exp of x is min
# smallest of the x

get_bin = lambda x:"{0:b}".format(x) # convert into binary
get_dec = lambda y:int(y,2)
get_count = lambda z: get_bin(z).count('1')

def print_bin(a):
    for item in a:
        print (item,get_bin(item))
    
#not perfect
def compute_and(a):
    #print ("a=",a)
    results = []
    results_set = set()
    compute_and_results = set()
    flag=False

    #get the result set 
    for x in (a):
        results_set = set()
        #need function to get the actual list instead of a high number
        for i in range(1000):
            if x & i > 0:
                results_set.add(i)
        results.append(results_set)

    compute_and_results = results.pop()
    for results_set in results:
            compute_and_results=compute_and_results.intersection(results_set)
    #print("compute_and_results=",compute_and_results)  
    return compute_and_results

#not perfect
def compute_min_no(compute_and_results):
    results = compute_and_results.copy()
    #print("compute_min_no->results=",results)
    min_no_results = set({results.pop()})
    for item in range(len(results)):
        if item+1 < len(results):
            min_no_results = min_no_results.intersection(set({item}))
    #print ("min_no_results=",min_no_results)
    return min_no_results

#perfect
def compute_min_ones(compute_and_results):
    results = compute_and_results.copy()
    #print("compute_min_ones->results=",results)
    min_count = results.pop()
    for item in results:
        item_bin = get_bin(item)
        item_count = item_bin.count('1')
        #print ("item_count=",item_count,"min_count=",min_count,"item_bin=",item_bin)
        if item_count < min_count:
            min_count = item_count
    #print ("min_count=",min_count)
    return min_count

def solve(a):
    # Complete this function
    compute_and_results = compute_and(a)
    if (len(compute_and_results)):
        min_no_results = compute_min_no(compute_and_results)      
        min_ones_results = compute_min_ones(compute_and_results)  
        return min_ones_results
    else: return 0

def assertTest(expected,current):
    print ("expected:",expected,"output=",current)
    if (expected != current): return False
    else : return True

#n = int(input().strip())
#a = list(map(int, input().strip().split(' ')))

def run_test(a,expected):
    print("a=",a)
    print_bin(a)
    print ("expected bin=",get_bin(expected))
    result = solve(a)
    print (assertTest(expected,result))

a = [1,2,3]; expected=3
run_test(a,expected)

a = [1,2,4,8,16,32,64,256,512,128]
expected = 1023
run_test(a,expected)

a = [7,14,28]; expected=4
run_test(a,expected)
