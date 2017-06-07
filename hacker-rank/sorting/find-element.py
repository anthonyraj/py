#Find element in sorted array
def find_element(n,arr):
    p = -1
    for pos in range(len(arr)):
        if (arr[pos] == n):
            return pos
    
        
n = int(input().strip())
f = int(input().strip())
d = input()
arr = [int(x) for x in d.strip().split()]
p = find_element(n,arr)
print(p)
