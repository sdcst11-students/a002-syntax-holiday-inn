import turtle
import time


t = turtle.Turtle()
t.speed(10)
t.hideturtle()
s = turtle.Turtle()
s.speed(10)
s.hideturtle()
s.pencolor("red")
m = turtle.Turtle()
m.speed(10) 
m.hideturtle()
m.pensize(2)
h = turtle.Turtle()
h.speed(10)
h.hideturtle()
h.pensize(5)
t.penup()
t.goto(0,-200)
t.pendown()
t.begin_fill()
t.circle(200)
def seconds():
    s.clear()
    s.setheading(90+(-sec*6))
    s.forward(190)
    s.backward(190)
def minutes():
    m.clear()
    m.setheading(90+(-min*6))
    m.forward(190)
    m.backward(190)
def hours():
    h.clear()
    h.setheading(90+(-hour*30))
    h.forward(130)
    h.backward(130)

while True:
    ti = time.localtime()
    sec = int(time.strftime("%S",ti))
    min = int(time.strftime("%M",ti))
    hour = int(time.strftime("%H",ti))
    seconds()
    minutes()
    hours()
