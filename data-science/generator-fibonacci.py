#fibonanci sequence generator
#keeps track of the number
#https://www.linkedin.com/learning/learning-python-generators/solution-fibonacci-sequence-fenerator
# 
def fib():
    f1,f2 = 0,1 # state of init
    while True:
        yield f2 # print the f2
        f1,f2= f2,f1+f2 # state of the next

f = fib()
#g = (next(f) for x in range(20))
#for item in g:
#    print(item)

# prints an infinite series
for _ in range(10):
    print(next(f))


#prints the generators. not good
#for item in (fib() for x in range(10)):
#    print(item)

#infinite series
#for item in fib():
#    print(item)
