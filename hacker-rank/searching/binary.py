# binary search
# https://www.linkedin.com/learning/learning-java-2/searching-arrays

def binary(s,key):
    lower = 0
    upper = len(s)
    position = int((lower+upper)/2)
    print("position=",position)
    
    while( s[position]!=key and lower<=upper):
        if(s[position]>key):
            upper = position - 1
        elif (s[position]<key):
            lower = position + 1
        position = int((lower+upper)/2)
        print("position=",position)
    
    if(lower<=upper):
        print("Found")
    else:
        print("Not Found")
        position = -1
    return position

#s = input().strip()
#data = [int(x) for x in s.split()]
#k = int(input().strip())
data= [1, 15, 30, 45, 200, 1000, 40000]
k = 1000
print("data=",data)
print("key=",k)
pos = binary(data,k)
print("binary search of key=",k," pos=",pos)

data= [1, 15, 30, 45, 200, 1000, 40000]
k = 10
print("data=",data)
print("key=",k)
pos = binary(data,k)
print("binary search of key=",k," pos=",pos)
