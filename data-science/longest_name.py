# using generators to find the longest name

def seperate_names(names):
    for fullname in names:
        for name in fullname.split(' '):
            yield name

full_names = (name.strip() for name in open('names.txt'))
#print(list(full_names))
names = seperate_names(full_names)

#lengths = ((name, len(name)) for name in full_names)
lengths = ((name, len(name)) for name in names)
#print(lengths)

longest = max(lengths, key=lambda x:x[1])
print(longest)

# several pipes can be linked together
# Items flow one by one through the entire pipeline
# Pipeline functionality can be packaged into callable functions
