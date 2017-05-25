"""
12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print
"""

def parser(cmd,list):
    if (cmd == 'print'):
        print (list)
    else:
    
    return list

if __name__ == '__main__':
    N = int(input())
    list = []
    while(N):
        cmd = input()
        list = parser(cmd,list)
        N -= 1
    
