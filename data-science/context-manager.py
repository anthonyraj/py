# this is a context manager

from contextlib import contextmanager

@contextmanager
def simple_context_manager(obj):
    try:
        obj.p += 1
        yield
    finally:
        obj.p -= 1

class A(object):
    def __init__(self, arg):
        self.p = arg

a = A(10)
with simple_context_manager(a):
    print(a.p)
