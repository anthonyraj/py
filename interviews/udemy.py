"""
You are given N objects of colored marbles in random color order.   Design an in-place sorting algo, to sort the marbles so that the same colored marbles are grouped together in a given order.


starting with 2 colors ("blue", "red")

m = Marble()
m.color = 'blue'  

[m1, m2, m3, m4, m5, m6, m7, m8, m9]
 b,  r,  r,  b,  r,  b,  b,  b,  r  

 r, b, b, r, b, r, r, r, b
 
 b,  r,  y,  b,  r,  b,  y,  b,  r 

sort_order = ['red', 'blue', 'yellow']

all reds followed by all blues
expected result: [m2, m3, m5, m9, m1, m4, m6, m7, m8]

Date: July 6th
"""

def sort(items,order):
    left = 0
    right = len(items)-1
    while (left<right):
        if (items[left] != order[0]):
            if (items[right] == order[0]):
                items[left], items[right] = items[right], items[left]          
                left += 1
                right -=1   
            else: right -=1
        else: left += 1        
                     
 
