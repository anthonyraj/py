# Stacks and Queues
# https://www.hackerrank.com/challenges/30-queues-stacks

class Stack(object):
    data = list()

    def __init__(self,str1=""):
        data = [y for y in str1]
        self.data = data

    def peek(self):
        return self.data[len(self.data)-1]

    def push(self,element):
        self.data.append(element)
        #return self.get_data()

    def pop(self):
        return self.data.pop()

    def get_data(self):
        return self.data

class Queue(object):
    data = list()

    def __init__(self,str1=""):
        data = [y for y in str1]
        self.data = data

    def enqueue(self,element):
        self.data.append(element)

    def dequeue(self):
        e = self.data[0]
        self.data.remove(e)
        return e

    def get_data(self):
        return self.data

str2 = "12345"
print("----- STACK ------")
s = Stack(str2)
print(s.get_data())
print(s.peek())
s.push(6)
print(s.get_data())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.get_data())

print("----- QUEUE ------")
q = Queue(str2)
print(q.get_data())
q.enqueue(6)
print(q.dequeue())
print(q.get_data())
print(q.dequeue())
print(q.get_data())    

print("----- PALINDROME ------")
str3 = input().strip()
s1 = Stack(str3)
q1 = Queue(str3)
i = 0
flag=True

while(flag and i<=len(str3)):
    e1 = s1.pop()
    e2 = q1.dequeue()
    if (e1 != e2):
        print("The word, "+str3+", is not a palindrome")
        flag=False
    i+=1
    
if flag:
    print( "The word, "+str3+', is a palindrome')
