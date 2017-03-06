# Maze Map 2
# TAKEN FROM: www.101computing.net/turtle-maze/

import turtle

screen = turtle.Screen()
screen.tracer(0)

mazeWidth=1

myMaze = turtle.Turtle()
myMaze.width(5)
myMaze.hideturtle()

myMaze.speed(0)

myMaze.penup()
myMaze.goto(-mazeWidth,190)


def drawMazeSection(color):
  myMaze.color(color)
  myMaze.pendown()
  myMaze.forward(mazeWidth)
  myMaze.penup()
  myMaze.forward(40)
  myMaze.pendown()
  myMaze.forward(mazeWidth)
  myMaze.right(90)
  myMaze.forward(100)
  myMaze.right(90)
  myMaze.forward(mazeWidth)
  myMaze.penup()
  myMaze.forward(40)
  myMaze.pendown()
  myMaze.forward(mazeWidth)
  myMaze.right(90)
  myMaze.forward(100)
  myMaze.right(90)
  x,y = myMaze.pos()
  myMaze.penup()  
  myMaze.goto(x, y-50)
  myMaze.pendown()
  myMaze.forward(30)
  myMaze.penup()
  myMaze.forward(40)
  myMaze.pendown()
  myMaze.forward(200)
  myMaze.penup()
  myMaze.forward(40)
  myMaze.pendown()
  myMaze.forward(30)
  myMaze.penup()
  myMaze.goto(x,y-110)

for color in ["#FF0000","#0000FF","#00FF00"]:
  drawMazeSection(color)

screen.tracer(1) # What does this do?

t = turtle.Turtle()

t.penup()
t.goto(20,-180)
t.pendown()
t.shape('turtle')
t.color("#DB148E")
t.width(5)
t.left(90)

# Start the maze code here!
t.forward(70)
t.right(90)
