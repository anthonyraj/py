"""
998001 == (998+001)^2

abcxyz == (abc + xyz)*(abc + xyz)
how numbers in a range of 6 digit from


100000 < x < 999999

100

Architecture
  2 pictures on cats
  user click and select cats
  10 tuple of cats
  popular cat of the day =>
  ads
  upload A PIC ->
---
"""
count = 0
start = 100000
current = start
end = 999999
while(start <= current <= end):
    lv = current /1000
    rv = current %1000
    sum = lv+rv
    square = sum * sum
    if (square == current):
        print "current=",current," lv=",lv," rv=",rv," square=",square
        count += 1
    current +=1

print count
