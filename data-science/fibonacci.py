def fibonacci():
    f1, f2 = 0,1
    print(f1)
    while True:
        #yield f1,f2
        yield f2
        f1,f2 = f2, f1+f2

f = fibonacci()
d = [next(f) for i in range(20)] #next(f) shorthand for f.__next__()
for i in d: print (i) 
