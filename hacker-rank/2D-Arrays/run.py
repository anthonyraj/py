#hour glass max count
# 2D Arrays

import sys

def compute_max_hour_glass(arr):
    max_count = 0
    count = 0
    r  = int((len(arr)/2)+1)
    h = 0
    for i in range(r):
        for j in range(r):
            h += 1
            count = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            count += arr[i+1][j+1]
            count += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if count>max_count:
                max_count=count
                count = 0
    #print("max_count",max_count)
    #print("hour glasses count=",h)
    return max_count

#arr = []
#for arr_i in range(6):
#   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#   arr.append(arr_t)

arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

m = compute_max_hour_glass(arr)
print(m)    
    
