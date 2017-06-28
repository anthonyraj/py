
def coroutine_example():
    while True:
        x = yield
        #do something with x
        print(x)

c = coroutine_example()
c.__next__()
c.send(10)

