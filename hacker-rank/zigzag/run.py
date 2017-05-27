#!/bin/python3

import sys

def minimumDeletions(a):
    # Complete this function
    #print (a)
    count = 0
    curr_flag = ''
    prev_flag = ''
    
    for i in range( len(a) ):
        if (i == len(a)-1):
            break
        current_val = a[i]
        next_val = a[i+1]
        
        prev_flag = curr_flag
        curr_flag = ''
        
        #print ("current_val="+str(current_val)+" | next_val="+str(next_val))
        #print ("curr_flag="+curr_flag+" | prev_flag="+prev_flag)

        if (next_val > current_val):
            #print ("Its an upward trend")
            curr_flag = 'up'

        if (next_val < current_val):
            #print ("Its a downward trend")
            curr_flag = 'down'

        if ( (next_val == current_val) or (curr_flag == prev_flag) ):
            count += 1
            
    return count
    
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# Return the minimum number of elements to delete to make the array zigzag
result = minimumDeletions(a)
print(result)

