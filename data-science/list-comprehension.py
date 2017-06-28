# list comprehension
collection = ["Yahoo","MOMO","alibaba"]
newlist = [item.upper() for item in collection]
print("collection=",collection)
print("newlist=",newlist)

# generator expression
gen_func = (item.upper() for item in collection)
data = list(gen_func)
print("data=",data)

# The trick is to get list() method to execute the generator.
# All generators are iterators, but all iterators are not generators

#list of mixed format numbers
numbers = [7,22,4.5,99.7,'3','5']

# convert numbers to integers using expression
integers = (int(n) for n in numbers)
l = list(integers)
print(l)

# list of names
names_list= ['Adam','Anne','Barry','Brianne','Charlie','Cassandra','David','Dana']
print(names_list)

# too long
print("--- Single Generator ---")
reverse_uppercase = (name[::-1] for name in (name.upper() for name in names_list))
l1 = list(reverse_uppercase)
print(l1)

# breaking it up
print("--- Multiple Generator ---")
uppercase = (names.upper() for names in names_list)
reverse_uppercase = (name[::-1] for name in uppercase)
l2 = list(reverse_uppercase)
print(l2)


