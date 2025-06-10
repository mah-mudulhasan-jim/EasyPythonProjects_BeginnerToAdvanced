import turtle

from PIL.ImageChops import screen

from colors import color_list
from turtle import Turtle, Screen
import random

turtle.colormode(255)

def display():
    sc = Screen()
    sc.exitonclick()

def draw_hirst_paint(tim, color):
    tim.penup()
    tim.hideturtle()
    tim.speed("fastest")
    goto_beginning_point(tim)
    num_of_dots = 100
    for i in range(1, num_of_dots+1):
        # x, y = tim.pos()
        tim.dot(20, random.choice(color))
        tim.fd(50)
        # tim.goto(x, y)
        if i % 10 == 0:
            go_up(tim)

def go_up(tom):
    tom.setheading(90)
    tom.fd(50)
    tom.setheading(180)
    tom.fd(500)
    tom.setheading(0)

def goto_beginning_point(tom):
    tom.setheading(225)
    tom.fd(300)
    tom.setheading(0)


timmy = Turtle()
draw_hirst_paint(timmy, color_list)