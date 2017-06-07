import turtle
wn = turtle.Screen()
anthony = turtle.Turtle()

def square(anthony,color,size):
     anthony.color(color)
     anthony.pensize(size)
     for i in range(4):
         anthony.forward(50)             # Make anthony draw a square
         anthony.left(90)
     

def triangle(anthony,color,size):
    anthony.color(color)
    anthony.pensize(5)
    for i in range(3):
        anthony.forward(80)             # Make anthony draw equilateral triangle
        anthony.left(120)

def circle(anthony,color,size):
    anthony.shape("turtle")
    anthony.color("blue")

    anthony.penup()                # This is new
    size = 20
    for i in range(30):
       anthony.stamp()             # Leave an impression on the canvas
       size = size + 3          # Increase the size on every iteration
       anthony.forward(size)       # Move anthony along
       anthony.right(24)

# drive home
def drive(anthony,color,size):
    anthony.penup()
    anthony.color(color)
    anthony.pensize(size)
    anthony.right(80)              # Turn anthony around
    anthony.forward(80)             # Move away from the origin
    anthony.pendown()    

def colorful_square(anthony,size):
    # Assign a list to a variable
    clrs = ["yellow", "red", "purple", "blue"]
    anthony.pensize(size)
    for c in clrs:
        anthony.color(c)
        anthony.forward(50)
        anthony.left(90)
    
anthony.shape("turtle")
anthony.speed(1)

square(anthony,"blue",5)
drive(anthony,"black",1)

triangle(anthony,"pink",5)
drive(anthony,"black",1)

colorful_square(anthony,5)
drive(anthony,"black",1)

#circle(anthony,"green",5)
anthony.stamp()




wn.onclick("pressed")

