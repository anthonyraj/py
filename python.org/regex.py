#https://developers.google.com/edu/python/regular-expressions
import re

def my_match(str):
    match = re.search(r'word:\w\w\w', str)
    # If-statement after search() tests if it succeeded
    if match:                      
        print ('found', match.group(0)) ## 'found word:cat'
        #print(match.group())
        
    else:
        print ('did not find')

str = 'an example word:cat!!'
my_match(str)
str = 'another example word:dog!!'
my_match(str)

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print (match.group()) ## 'alice-b@google.com'
