# number summation using recursion

def sum(no,s):
    print("no=",no,"s=",s)
    if(no>0):
        s += no
        no -=1
        sum(no,s)

def sum1(no):
    print(no)
    if (no>0):
        return no + sum1(no-1)
    else:
        return no

no=5
s=0
sum(no,s)

t = sum1(5)
print(t)
