# http://www.secnetix.de/olli/Python/lambda_functions.hawk
# Executed in 2.6 environment

import itertools

# Example of filter + lambda
nums = range(2,50)
for i in range (2,8):
    nums = filter(lambda x: x == i or x % i, nums)

print nums

# Example of map + lambda
sentence = 'It is raining cats and dogs'
words = sentence.split()
print words
lengths = map(lambda word: len(word), words)
print lengths

# Convert the individual lists into a dict
#https://stackoverflow.com/questions/209840/map-two-lists-into-a-dictionary-in-python
data = dict(zip(words,lengths))
print data
adict = dict(itertools.izip(words,lengths))
print adict
# ERROR
#new_dict = {k: v for k, v in zip(words,lengths)}
#print new_dict

stuff = map(lambda w: [w.upper(),w.lower(), len(w)], words)
for i in stuff: print i
