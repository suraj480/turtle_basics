import turtle
t=turtle.Turtle()
t.speed(1)
#provide window color
wn=turtle.Screen()
wn.bgcolor("#99FFCC")
t.begin_fill()
t.fillcolor("#FF8000")
#Drawing sqaure
for i in range (4):
    t.forward(150)
    t.left(90)
t.end_fill()
t.fillcolor("#FF8000")
t.hideturtle()
#it will stop screen after completion
t.goto(200,200)
list=["purple","red","orange","blue","green"]
for i in range(200):
    t.color(list[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)

turtle.done()