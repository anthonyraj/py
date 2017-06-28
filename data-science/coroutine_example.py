
def coroutine_example():
    while True:
        x = yield
        #do something with x
        print(x)

c = coroutine_example()
c.__next__() # initial next is needed to prime up the co-routine
c.send(10)

