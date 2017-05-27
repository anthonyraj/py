#!/bin/python3

import sys

def add_road(r,lookup):
    #print ("r :",r)
    if ( lookup.__contains__(r[0]) ):
        lookup[r[0]].add(r[1])
    else:
        lookup[r[0]] = set()
        lookup[r[0]].add(r[1])
    return lookup

def new_road(x,d,lookup,cities):
    #print ("x=",x," d=",d)    
    #print ("cities",cities)
    n = max(cities)
    if d==0:
        lookup=add_road((x,n+1),lookup)
    if d==1:
        lookup=add_road((n+1,x),lookup)
    cities.add(n+1)
    return lookup,cities

def setup(roads):
    #print("setup roads ...")
    lookup = {}
    for r in roads:
        lookup=add_road(r,lookup) 
    return lookup

# check if one can move from city x -> y
def can_move(x,y,lookup):
    #print ("x=",x,"y=",y)
    response = "No"
    if (lookup.__contains__(x)):
        if y in lookup[x]:
            response = "Yes"
        else:
            for item in lookup[x]:
                response = can_move(item,y,lookup)
                if (response):break
    return response

def process_events(cities,events,lookup):
    #print("process events ...")    
    for e in events:
        #print ("event:",e)
        if e[0] == 1:
            x,d = e[1],e[2]
            lookup,cities=new_road(x,d,lookup,cities)
            
        elif e[0] == 2:
            x,y = e[1],e[2]
            #print("can_move:x=",x,"y=",y)
            print (can_move(x,y,lookup))
    #print ("lookup",lookup)

def hackerland(cities,roads,events):
    #print ("roads:",roads)
    #print ("events:",events)
    map = []
    lookup = setup(roads)           
    process_events(cities,events,lookup)
    #print ("lookup",lookup)
    
roads = []
events = []
cities = set()

#n, m = input().strip().split(' ')
#n, m = [int(n), int(m)]

#for a0 in range(m):
#    u, v = input().strip().split(' ')
#    u, v = [int(u), int(v)]
#    roads.append((u,v))
#    cities.add(u)
#    cities.add(v)

#q = int(input().strip())
#for a0 in range(q):
#    t, x, y = input().strip().split(' ')
#    t, x, y = [int(t),int(x), int(y)]
#    events.append((t,x,y))

#Test1
roads = [(1, 2), (1, 3), (2, 4), (3, 4)]
events = [(1, 2, 0), (2, 3, 5), (2, 1, 5), (1, 1, 1), (2, 6, 4)]   
cities = set({1,2,3,4})

hackerland(cities,roads,events)
