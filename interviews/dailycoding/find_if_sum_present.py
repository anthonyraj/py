
def isSumOfNumbers(match, numbers):
	compliments = set()
	for i in numbers:
		if compliments.__contains__(match-i): return True
		else: compliments.add(i)
	return False

match = input()
numbers = map(int,(raw_input().split()))
print isSumOfNumbers(match, numbers)
