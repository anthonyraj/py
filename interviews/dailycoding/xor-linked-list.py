"""
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both,
which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end,
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer functions
that converts between nodes and memory addresses.

url: https://www.geeksforgeeks.org/xor-linked-list-a-memory-efficient-doubly-linked-list-set-1/
solution: https://www.dailycodingproblem.com/solution/6?token=b4b7bc554dc49a86cb0908e384645ae2dde0ddd2f4777c535f669888cfeaa456f6140610

"""
import math # for xor function
class Node():
    def __init__(self,value,xor_ptr):
        self.value = value
        self.xor_ptr = xor_ptr

class xorLinkedList():
    def __init__(self):
        self.list = []

    """
        -2 -> means get me a pointer to an element that I want to add after LAST_INDEX
    """
    def get_pointer(self,index=None):
        # TODO: xor the index of the previous and next element
        START = -1
        END = -2
        LAST_INDEX = len(self.list) -1


        if len(self.list) == 0:
                return START ^ END
        if len(self.list) == 1:
                return 0 ^ END
        if index == -2:
            return LAST_INDEX ^ END

        if (index == None or index == LAST_INDEX):
            return LAST_INDEX -1 ^ END
        else:
            return index -1 ^ index +1

    def dereference_pointer(self,xor_ptr):
        xor_ptr = -3
        return xor_ptr

    def add(self,element):
        # add new element
        xor_ptr = self.get_pointer(-2)
        node = Node(element, xor_ptr)
        self.list.append(node)

        # update ptr for previous element
        if len(self.list)>1:
            prev_index = len(self.list)-2
            node = self.get(prev_index)
            node.xor_ptr = self.get_pointer(prev_index)
        x.dump()


    def get(self,index):
        return self.list[index]

    def dump(self):
        print "...."
        for i in range(len(self.list)):
            item = self.list[i]
            print "({},{})".format(item.value,item.xor_ptr)
            print "get_pointer(",i,")",self.get_pointer(i)
        print "..."

x = xorLinkedList()
x.add(10)
x.add(20)
x.add(30)
x.add(40)
