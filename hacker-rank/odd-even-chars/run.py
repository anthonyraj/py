#format strings
#print the even and odd indexed characters as 2 space-separated strings

def compute(string):
    even,odd = '',''
    i=0
    for s in string.strip():
        if i%2 ==0: even+=s
        else: odd+=s
        i+=1
    print(even,odd)

def compute1(string):
    print(string[::2],string[1::2])
        
n = int(input())
string_list = []
for s in range(n):
    string = input()
    string_list.append(string)

#string_list = ['Hacker', 'Rank']
#print(string_list)

for string in string_list:
    compute1(string)
