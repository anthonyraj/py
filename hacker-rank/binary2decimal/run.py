#decimal to binary

def dec2bin(n):
    binary = []
    while (n>0):
        r = n%2
        n = int(n/2)
        binary.append(r)
    binary.reverse() 
    #b = ''.join([str(x) for x in binary])
    return binary
    
def get_max_consecutive_ones(b):
    count = 0
    max_count = 0
    
    for x in b:
        #print(x)
        if x == 1:
            count += 1
        elif x == 0:
            if count>max_count:
                max_count=count
            count = 0
    #print("max_count=",max_count)
    return max_count

def bin2dec(c):
    pass

n = int(input().strip())
b = dec2bin(n)
print(b)
c = get_max_consecutive_ones(b)
print(c)
