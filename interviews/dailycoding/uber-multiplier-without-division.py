
def products(data):
	prefix_data = []
	for num in data:
		if prefix_data:
			prefix_data.append(prefix_data[-1] * num)
		else: prefix_data.append(num)
	print "prefix_data=",prefix_data

	suffix_data = []
	for num in reversed(data):
		if suffix_data:
			suffix_data.append(suffix_data[-1] * num)
		else: suffix_data.append(num)
	suffix_data.reverse()
	print "suffix_data=",suffix_data

	result = []
	for i in range(len(data)):
		if i == 0: 
			result.append(suffix_data[i+1])			 
		elif i == len(data)-1:
			result.append(prefix_data[i-1])
		else:
			result.append(prefix_data[i-1] * suffix_data[i+1])
	return result	

data = map(int, raw_input().split())
print products(data)
