#insertion sort
# works well with small arrays

def insertion_sort(arr):
    ele = arr.pop()
    print(ele)
    item =0
    #for item in range(0,len(arr)):
    while(item+1 < len(arr)):   
        current = arr[item]
        next1 = arr[item+1]
        print("current=",current,"next1",next1)
        if current<ele and ele<next1:
            print("yes")
        #else: print("no")
        item +=1

def insertion(arr):
    for j in range(1,len(arr)):
        #print("j=",j)
        key = arr[j]
        i = j-1
        #print("i=",i)
        #print("key=",key)
        while(i>=0):
            if(key<arr[i]):
                arr[i+1] = arr[i]
            i-=1
        arr[i+1] = key
        #print("arr=",arr)
    return arr
        
#s = input().strip()
#arr = [int(x) for x in s.split()]

arr=[5,4,3,2,1]
print("before arr=",arr)
arr1 = insertion(arr.copy())
print("insertion sort arr=",arr1)
