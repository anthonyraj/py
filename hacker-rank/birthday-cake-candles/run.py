# birthday-cake-candles
#!/bin/python3

import sys

n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

def get_max(height):
    max1 = 0
    count = 0
    for item in height:
        if (item > max1):    
            max1 = item
            count = 1
        elif (item == max1):
            count += 1
        #print ('item = ',item,'max1 = ',max1)    
    return count

count = get_max(height)
print (count)

print height.count(max(height))
