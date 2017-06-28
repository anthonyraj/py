# matterport test
"""
Read and Refactor
=================

Let's say you come across this method somewhere in a codebase.  Maybe an
intern wrote it.  Maybe another team member wrote it.

It's not very well-named or readable nor is it very Python-ic or efficient.

1. Read through and describe what the code is doing.  Assume the passed-in
   "input" parameter is a string, such as "aabbbccccd".

2. Refactor the method to be more readable, Python-ic, and efficient.
"""


def foo(input):
    a = {}
    b = 0
    c = len(input)
    for i in xrange(c):
        if input[i] in a:
          a[input[i]] = a[input[i]] + 1
        else:
          a[input[i]] = 1
    for k, v in a.iteritems():
        if v > b:
          b = v
    return b

def foo1(input):
    a = {}
    b = 0
    c = len(input)
    for i in xrange(c):
        
        key = input[i] 
        # keep count of occurrance of alphabet key
        if key in a:
          a[key] += 1
        else:
          a[key] = 1
        # checks for max count of each alphabet key
        if (a[key] > b): b = a[key]
    return b

def max_letter(input):
    letter_counts = {}
    max_count = 0
    for key in input:
        # keep count of occurrance of alphabet key
        if key in letter_counts:
          letter_counts[key] += 1
        else:
          letter_counts[key] = 1
        # checks for max count of each alphabet key
        if (letter_counts[key] > max_count): max_count = letter_counts[key]
    return max_count

# Test cases
if __name__ == '__main__':
    print "Testing the code"
    assert(foo('aabbbccccd') == 4)
    assert(foo('ababccdddefg') == 3)
    assert(foo('mymatterport') == 3)
    
