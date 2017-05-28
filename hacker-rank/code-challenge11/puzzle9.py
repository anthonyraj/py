#puzzle-9
#https://www.hackerrank.com/contests/world-codesprint-11/challenges/puzzle-9

import sys, random

def compute_min_size(h,w):
    return h*w

def get_size(figure):
    max_row = 0
    max_col = 0
    for item in figure:
        #print(item)
        if item[0] > max_row: max_row=item[0]
        if item[1] > max_col: max_col=item[1]
    return max_row,max_col

def put_figure(figure,grid,i):
    for fig in figures:
        grid[fig[0]][fig[1]] = i
    print (grid)
    return grid

def get_largest_size(figures):
    pass    

def init_grid():
    grid = []
    colors = ['R','B','G']
    for i in range(15):
        elements = []
        for item in range(15):
            elements.append(random.choice(colors))
        grid.append(elements)
    print ("grid=",grid)
    return grid
        
def get_output(n,figures):
    grid = init_grid()
    largest = figures[0]
    for i in range(len(figures)):
        fig = figures[i]
        print (fig)
        if len(fig) > largest: largest = fig
        h,w = get_size(fig)
        print ("h=",h,"w=",w,"cell count=",len(fig))
        put_figure(fig,grid,i)

def get_input():
    n = int(input().strip())
    figures = []
    for figure in range(n):
        m = int(input().strip())
        figure=[]
        for c in range(m):
            x,y = input().strip().split(' ')
            cell = [int(x),int(y)]
            figure.append(cell)
        figures.append(figure)
    return n,figures

#n,figures = get_input()
n=3
figures = [[[1, 1], [2, 1]],
           [[1, 2], [2, 1], [2, 2], [2, 3], [3, 1]],
           [[1, 1], [1, 2]]
           ]

#print (figures)

get_output(n,figures)
