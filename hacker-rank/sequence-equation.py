#sequence equation

def convert_to_dict(data):
    data_dict = {}
    for item in range(len(data)):
        data_dict[item+1] = data[item]
    return data_dict

def calc_equation(dd):
    while True:
        x = yield
        if isinstance(x,int):
            #if x in dd.values():
            #    for k,v in dd.items():
            #        if x == v :
            #            print(k)
            k = p1(x,dd[x],dd)
            print('k=',k)
            
def p1(x,p,dd):
    print("x=",x,"p=",p,"dd=",dd)
    if x in dd.values():
        for k,v in dd.items(): # need a better way to get k for a value
            #print("k=",k,"v=",v)
            if v==x :
                print("k=",k,"v=",v)
                if v!=p:
                    return p1(k,p,dd)
                else: return k
        return 1

def reverse_dict(dd):
    rdd = {}
    for k,v in dd.items():
        rdd[v] = k
    return rdd

def get_p(x,dd,rdd):
    if x in dd.values():
        return rdd[x]                

n = int(input().strip())
data = [int(x) for x in input().strip().split()]
#data = [1,2,3]

dd = convert_to_dict(data)
#print("dd=",dd)
rdd = reverse_dict(dd)
#print("rdd=",rdd)

#c = calc_equation(dd)
#next(c)

#for x in range(len(data)):
#    c.send(x+1)

for i in range(len(dd)):
    y = i + 1
    #print(p1(y,dd[y],dd))
    p1 = get_p(y,dd,rdd)
    p2 = get_p(p1,dd,rdd)
    print(p2)
