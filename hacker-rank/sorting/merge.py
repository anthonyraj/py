#merge sort
#https://en.wikipedia.org/wiki/Merge_sort
# merge sort and timsort are used in Python & JDK

from math import log

def top_down_merge_sort(A, B, n):
    #B = copy_array(A, 0, n, B)
    top_down_split_merge(B,0,n,A)

def top_down_split_merge(B, begin, end, A):
    if(end-begin < 2):
        return;

    middle = int((end+begin)/2)
    top_down_split_merge(A, begin, middle, B)
    print(A,begin,middle,end,B)
    top_down_split_merge(A, middle, end, B)
    print(A,begin,middle,end,B)
    top_down_merge(B, begin, middle, end, A)
    print(A,begin,middle,end,B)
    #bigO+=1

def top_down_merge(A, begin, middle, end, B):
    i = begin
    j = middle
    
    #for (k=begin; k<end; k++):
    for k in range(begin,end):
        if (i<middle and (j>=end or A[i] <= A[j]) ):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1

def copy_array(A, begin, end, B):
    B = A.copy()
    return B

def print_big_o(n):
    print ("Serial Sort BigO")
    goodO = n*log(n)
    print("Good O(nlogn)",goodO)
    parallelGoodO=log(n)*log(n)
    print("Paralell sort O(logexp2*n)=",parallelGoodO)
    badO=n*n
    print("Bad O(n*n)=",badO)

bigO = 0   
A = [6,5,3,1,8,7,4,2]
print("Not Sorted A",A)
B = A.copy()
n = len(A)
top_down_merge_sort(A,B,n)
print("Merge Sorted A",A)
print("Merge Sorted B",B)
#print("BigO = ",bigO)

print("-----")
print_big_o(n)
