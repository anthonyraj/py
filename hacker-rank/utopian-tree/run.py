#!/bin/python

import sys

initial_height = 1
cycle_array = []

#Compute the height for N cycles    
def compute(n):
    even = n/2
    odd = n%2
    height=initial_height
    
    for i in range(even):
        height = computeBothCycles(height)

    if (odd == 1):
        height = computeSpringCycle(height)

    return height

# Compute the height for 2 cycles spring & summer        
def computeBothCycles(height):
    height_cycle=height
    height_cycle = computeSpringCycle(height_cycle)
    height_cycle = computeSummerCycle(height_cycle)
    return height_cycle

def computeSpringCycle(height):
    factor = 2
    return (height*factor)

def computeSummerCycle(height):
    step = 1
    return (height+step)

def run():
    t = int(raw_input().strip())

    for a0 in xrange(t):
        n = int(raw_input().strip())
        cycle_array.append(n)

    for n in cycle_array:
        print compute(n)

run()
