from pets import *

p = Pet("Pet1","Mammal")
print(p.getName())
print(p.getSpecies())
print(p.__str__())

d = Dog("Snoopy",True)
print(d.chasesCats())
print(d.getName())
print(d.getSpecies())
print(d.__str__())

c = Cat("Cherry",True)
print(c.hatesDogs())
print(c.getName())
print(c.getSpecies())
print(c.__str__())
