# selection sort

def selection(arr,order):
    #print("arr=",arr)
    #print("order=",order)
    
    start = len(arr)-1
    end = 0
    step = -1
    #print("n=",n)
    for i in range(start,end,step):
        #print("i=",i)
        first = 0
        for j in range(1,i+1):
            #print("j=",j)
            if order=="desc":
                if arr[j]<arr[first]:
                    first = j
            elif order=="asc":
                if arr[j]>arr[first]:
                    first = j
        #print("first=",first)
        arr[i],arr[first] = arr[first],arr[i]
        #print(arr)
    #print(arr)
    return arr

data = input().strip()
arr = [int(x) for x in data.split()]

#arr = [5, 4, 1, 2, 100, 45]

print("--- DESC ---")
print(arr)
arr1 = selection(arr.copy(),"desc")
print(arr1)

print("--- ASC ---")
print(arr)
arr2 = selection(arr1.copy(),"asc")
print(arr2)
