"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
My attempt to solve the problem with recurrsion did not work correctly
Went into endless recurrsion and reached max depth
"""
def serialize1(node):
    # without this check reaches max recurrsion
    if (node is None):
        return 'None'
    output = node.val

    if ((node.left == None) and (node.right == None)):
        output += '[ #, # ]'
        return output

    output += "[ "

    if node.left == None:
        output += '#'
    else:
        if isinstance(node.left,Node):
            #output += "LEFT_Node"
            output += serialize(node)
        else:
            output +=  node.left

    output += ","

    if node.right == None:
        output += '#'
    else:
        if isinstance(node.right,Node):
            #output += "RIGHT_Node"
            output += serialize(node)
        else:
            output += node.right
    output += " ]"

    return output

"""
    Another attempt to solve my way
"""
def deserialize1(string_data):
	list_data = string_data.split(":")
	if len(list_data)==1:
		root = list_data[0]
		return Node(root)
	elif len(list_data)==2:
		root = list_data[0]
		left = list_data[1]
		return Node(root,left)
	elif len(list_data)==3:
		root = list_data[0]
		left = list_data[1]
		right = list_data[2]
		return Node(root,left,right)
	else: return null

def serialize(node):
    if node == None:
        return '#'
    return '{} {} {}'.format(node.val,serialize(node.left),serialize(node.right))

def deserialize(string_data):
    def helper():
        item = next(vals)
        if item == '#':
            return None
        node = Node(item)
        node.left = helper()
        node.right = helper()
        return node

    vals = iter(string_data.split())
    return helper()

node = Node('root', Node('left', Node('left.left')), Node('right'))
print serialize(node)
print deserialize(serialize(node)).left.left.val

print "---"

node1 = Node('root', Node('left'), Node('right'))
print serialize(node1)
print deserialize(serialize(node1)).left.val

assert deserialize(serialize(node)).left.left.val == 'left.left'
