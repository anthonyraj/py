# Generate even numbers using generator
def generate_even_integers(n):
    for i in range(n):
        if (i%2==0):
            yield i

res = list(generate_even_integers(10))
print(res)

m = max(for i in range(100))
integers = generate_even_integers(100)
m1 = max(integers)
