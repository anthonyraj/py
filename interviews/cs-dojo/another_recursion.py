from datetime import datetime


def try_me(n):
	if (n>0):
		print n
		return try_me(n-1)
	else: return 0

def finding_peak(n):
	peak = 0
	print datetime.now().ctime()
	for i in range(n):
		if i>=peak: peak=i
	print datetime.now().ctime()
	return peak

n = input()
#print try_me(n)

print finding_peak(n)
