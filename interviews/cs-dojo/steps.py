def num_ways(n):
	#print "n=",n
	if n==0 or n==1 : return 1
	else: return num_ways(n-1) + num_ways(n-2)


n = input()
print "total=",num_ways(n)
