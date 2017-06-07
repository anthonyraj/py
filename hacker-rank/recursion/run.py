#recursion

def test(value):
    if (value>0):
        print(value)
        test(value-1)
    else:
        print("reached base case")

n = int(input().strip())
test(n)
