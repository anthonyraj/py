# generator solution
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

g = (even_integers_generator(10))
l = list(g)
print(l)
