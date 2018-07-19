import sys

n = int(input())
stamps = set()
for i in range(n):
	name = raw_input()
	stamps.add(name)

print len(stamps)
