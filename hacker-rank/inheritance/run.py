class Person:
    def __init__(self,firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName, ",",self.firstName)
        print("ID:", self.idNumber)
        
class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName,lastName, id, scores):
        self.scores = scores
        Person.__init__(self,firstName, lastName, id) # initialize base class
        

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        sum1 = 0
        average = 0
        grade = ""
        #print(self.scores)
        for score in self.scores:
            sum1 = sum1 + score
        average = sum1/len(self.scores)
        #print(average)
        if (90<=average<=100):
            grade = "O"
        elif (80<=average<90):
            grade = "E"
        elif (70<=average<80):
            grade = "A"
        elif (55<=average<70):
            grade = "P"
        elif (40<=average<55):
            grade = "D"
        elif (average<40):
            grade = "T"
            
        return grade

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:",s.calculate())

