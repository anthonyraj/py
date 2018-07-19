
def answer(x):
    if len(str(x)) == 1: return x

    total = 0
    for item in str(x):
        total += int(item)

    if total>9:
        total = answer(total)
    return total
        
x = 13
#print "x=",x," answer=",answer(x)
assert answer(x) == 4

x = 12345
#print "x=",x," answer=",answer(x)
#assert answer(x) == 2
assert answer(x) == 6

x = 111
#assert answer(x) == 1
assert answer(x) == 3

x = 999
assert answer(x) == 9
