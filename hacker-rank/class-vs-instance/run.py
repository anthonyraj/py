class Person:
    age = 0;
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge>0:
            self.setAge(initialAge)
        elif initialAge<0:
            self.setAge(0)
            print("Age is not valid, setting age to 0.")
            
    def setAge(self,newAge):
        self.age = newAge
        
    def getAge(self):
        return self.age
    
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.getAge()<13: print ("You are young.")
        elif 13<=self.getAge()<18: print ("You are a teenager.")
        else: print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.setAge(self.getAge()+1)

#stub code
t = int(input())
for i in range(0,t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0,3):
        p.yearPasses()
    p.amIOld()
    print("")
            
