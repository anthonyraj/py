"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

"""
	O(n)=n*n where n=size of list
"""
def list_multiplier(data):
	new_data = []
	size = len(data)
	for i in range(size):
		temp = 1
		for j in range(size):
			if (i!=j): temp = temp * data[j]	
		new_data.append(temp)
	return new_data

"""
Using division
"""
def product(data):
	new_data = []
	product = 1

	for i in range(len(data)):
		product = product * data[i]

	for i in range(len(data)):
		new_data.append(product//data[i])

	return new_data	

data = map(int, raw_input().split())
print("data=",data)
#print list_multiplier(data)
print product(data)

