"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

"""
from itertools import permutations
import sys

number = raw_input("Enter 3 digit between 1 & 26 eg. 111 :: ")
n = int(number)
if n<100:
    print "error. need 3 digits"
    sys.exit()

no = range(1,26)
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lookup = zip(no,alpha)
#print lookup

a = n/10
b = n/100

perms = permutations([a,b])
for item in perms:
    print item

for item in perms:
    #print item
    msg = ''
    if (item[0] >0 and item[0] <27):
        msg += lookup[item[0]-1][1]
    if (item[1] >0 and item[1] <27):
        msg += lookup[item[1]-1][1]
    print msg
