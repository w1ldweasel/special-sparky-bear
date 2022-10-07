from turtle import *
from random import *

def randomcolor():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0,255)
    color(red, green, blue)

def randomplace():
    penup()
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)
    pendown()

def randomheading():
    setheading(65)

colormode(255)

shape("turtle")
speed(5)

'''for i in range(30):
    randomcolor()
    randomplace()
    randomheading()
    stamp()'''



def drawrectangle():
    randomcolor()
    randomplace()
    hideturtle()
    length = randint(10, 100)
    height = randint(10, 100)
    begin_fill()
    forward(length)
    right(90)
    forward(height)
    right(90)
    forward(length)
    right(90)
    forward(height)
    right(90)
    end_fill()

clear()
setheading(0)

for i in range (40):
    drawrectangle()
