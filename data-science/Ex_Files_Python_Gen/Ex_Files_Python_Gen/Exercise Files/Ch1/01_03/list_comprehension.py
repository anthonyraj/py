# list comprehension
collection = 'dsadadsad'
newlist = [item.upper() for item in collection]
print(newlist)

# generator expression
g = (item.upper() for item in collection)
l = list(g)
print(l)
