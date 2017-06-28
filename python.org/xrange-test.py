import timeit

n = 10000
def test_range(n):
    for i in range(n):
        pass

def test_xrange(n):
    for i in xrange(n):
        pass

print 'Python',python_version()
print '\ntiming range()'
#%timeit test_range(n)

print '\ntiming xrange()'
#%timeit test_xrange(n)
