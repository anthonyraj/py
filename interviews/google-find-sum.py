'''
Find the addition of 2 numbers within an array

input:
1 2 3 9
1 2 4 4
'''

from itertools import permutations

def find_sum(data):
	if len(data)>1:
		for pair in permutations(data,2):
			if (pair[0] + pair[1] == 8):
				print pair
				return True
	else:
		return False

def isSumAvailable(data, sum):
	if len(data)>1:
		size = len(data)
		lowIndex = 0
		highIndex = size - 1

		while(lowIndex<highIndex):
			lowNum = data[lowIndex]
			highNum = data[highIndex]
			if (data[highIndex] + data[lowIndex] == sum):
				print lowNum,highNum
				return True
			elif (lowNum + highNum > sum):
				highIndex -= 1
			elif (lowNum + highNum < sum):
				lowIndex +=1

		return False

def hasPairWithSum(data,sum):
	comp = set()
	for item in data:
		if comp.__contains__(item):
			return True
		comp.add(sum-item)
	print comp
	return False

sum = input()
data = map(int, raw_input().split())
data.sort()

print isSumAvailable(data, sum)
print "Second approach ..."
print hasPairWithSum(data,sum)
