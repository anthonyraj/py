"""
INPUT
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

"""
OUTPUT
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

def parser(cmd,list):
    param = cmd.split(' ')
    method = param[0]
    if (method == 'insert'):
        list.insert(int(param[1]),int(param[2]))
    if (method == 'remove'):
        list.remove(int(param[1]))
    if (method == 'append'):
        list.append(int(param[1]))
    if (method == 'print'):
        print (list)
    if (method == 'pop'):
        list.pop()
    if (method == 'reverse'):
        list.reverse()
    if (method == 'sort'):
        list.sort()
    return list

if __name__ == '__main__':
    N = int(input())
    list = []
    while(N):
        cmd = input()
        list = parser(cmd,list)
        N -= 1
    
