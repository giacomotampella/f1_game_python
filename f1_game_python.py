# F1 GAME in python 3.9
# Idea by @CristoferiNicolò - made by @TampellaGiacomo

import random
import os
import turtle
import winsound
import time
import platform
import tkinter

# SET UP THE SCREEN
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("F1 GAME")
wn.tracer(0)

# REGISTER THE SHAPES
wn.register_shape("player_a.gif")
wn.register_shape("player_b.gif")

# SCORE
score_a = 0
score_b = 0

# PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))

# DRAW BORDER
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# CREATE THE PLAYER A
player_a = turtle.Turtle()
player_a.color("red")
player_a.shape("player_a.gif")
player_a.penup()
player_a.speed(0)
player_a.setposition(100, -250)
player_a.setheading(90)
player_a.speed = 0

# CREATE THE PLAYER B
player_b = turtle.Turtle()
player_b.color("grey")
player_b.shape("player_b.gif")
player_b.penup()
player_b.speed(0)
player_b.setposition(-100, -250)
player_b.setheading(90)
player_b.speed = 0

# CREATE THE OBSTACLES
number_of_obstacles = 15
obs = []
obstacles_count = 0

# ADD OBSTACLES TO THE LIST
for i in range(number_of_obstacles):
    # CREATE THE ENEMY
    obs.append(turtle.Turtle())

for obstacles in obs:
    obs = turtle.Turtle()
    obs.color("grey")
    obs.shape("circle")
    obs.speed(0)
    obs.penup()
    xo = random.randint(-280, 280)
    yo = random.randint(-200, 280)
    obs.goto(xo, yo)

# MOVE THE PLAYER UP, DOWN, LEFT AND RIGHT
def move_down_a():
    player_a.speed = -0.2
def move_down_b():
    player_b.speed = -0.2

def move_up_a():
    player_a.speed = 0.2
def move_up_b():
    player_b.speed = 0.2

def move_left_a():
    player_a.speed = -0.2
def move_left_b():
    player_b.speed = -0.2

def move_right_a():
    player_a.speed = 0.2
def move_right_b():
    player_b.speed = 0.2

def move_player_a():
    y = player_a.ycor()
    y += player_a.speed
    player_a.sety(y)
    if y > 280:
        y = -280
    player_a.sety(y)
    if y < -280:
        y = -280
    player_a.sety(y)

def accelerate_a():
    player_a.speed += 0.2

def decelerate_a():
    player_a.speed -= 0.2

def move_player_a_right():
    x = player_a.xcor()
    x += 20
    player_a.setx(x)
    if x > 280:
        x = 280
    player_a.setx(x)

def move_player_a_left():
    x = player_a.xcor()
    x -= 20
    player_a.setx(x)
    if x < -280:
        x = -280
    player_a.setx(x)

def move_player_b_right():
    x = player_b.xcor()
    x += 20
    player_b.setx(x)
    if x > 280:
        x = 280
    player_b.setx(x)

def move_player_b_left():
    x = player_b.xcor()
    x -= 20
    player_b.setx(x)
    if x < -290:
        x = -290
    player_b.setx(x)

def move_player_b():
    y = player_b.ycor()
    y += player_b.speed
    player_b.sety(y)
    if y > 280:
        y = -280
    player_b.sety(y)
    if y < -280:
        y = -280
    player_b.sety(y)

    x = player_b.xcor()
    player_b.setx(x)

def accelerate_b():
    player_b.speed += 0.2

def decelerate_b():
    player_b.speed -= 0.2

def change_obs_position():
    ya = player_a.ycor()
    yb = player_b.ycor()
    if ya >= 280 or yb >= 280:
        for obstacles in range(20):
            xo = random.randint(-280, 280)
            yo = random.randint(-200, 280)
            obs.setx(xo)

# CREATE KEYBOARD BINDINGS
wn.listen()
wn.onkeypress(move_down_a, "Down")
wn.onkeypress(move_up_a, "Up")
wn.onkeypress(move_player_a_left, "Left")
wn.onkeypress(move_player_a_right, "Right")
wn.onkeypress(accelerate_a, "0")
wn.onkeypress(decelerate_a, "1")

wn.onkeypress(move_down_b, "s")
wn.onkeypress(move_up_b, "w")
wn.onkeypress(move_player_b_left, "a")
wn.onkeypress(move_player_b_right, "d")
wn.onkeypress(accelerate_b, "space")
wn.onkeypress(decelerate_b, "q")

while True:
    wn.update()
    move_player_a()
    move_player_b()
    move_player_a_left()
    move_player_a_right()
    move_player_b_left()
    move_player_b_right()
    accelerate_a()
    decelerate_a()
    accelerate_b()
    decelerate_b()
    change_obs_position()
