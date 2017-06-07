#bubble sorting
#insetion sort => small dataset
#large dataset => asymptomatically efficient sort ->
#               heap sort, merge sort, or quicksort

# Try the following algorithms
# merge sort
# tim sort
# tree sort

from math import log

a = [1,5,2,6,4,3,100,10,50,60]
n = len(a)
print( "n=",n )

print("un-sorted a=",a)
bigO = 0
for i in range(n):
    bigO+=1
    for j in range(i,n):
        bigO+=1
        if (a[i] > a[j]):
            a[i],a[j] = a[j],a[i] # without temp
            
print("sorted a=",a)
print("bigO=",bigO)

print ("Serial Sort BigO")
goodO = n*log(n)
print("Good O(nlogn)",goodO)
parallelGoodO=log(n)*log(n)
print("Paralell sort O(logexp2*n)=",parallelGoodO)
badO=n*n
print("Bad O(n*n)=",badO)
        
