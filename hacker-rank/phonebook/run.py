#Dictionaries and Maps
phonebook = dict()

# Save the phonebook
#n = int(input())
#for i in range(n):
#    data = input().strip().split(' ')
#    phonebook[data[0].lower()] = data[1]

#print(phonebook)
phonebook = {'sam':'99999', 'tom':'88888', 'harry':'77777'}

search = []
# Read the search terms
try:
    name = input()
    while(len(name.strip())):
        search.append(name.lower().strip())
        try:
            name = input()
        except EOFError:
            name=''
except EOFError:
    name=''

# Execute the search
for name in search:
    if phonebook.__contains__(name):
        print(name+'='+phonebook[name])
    else:
        print('Not found')
    
