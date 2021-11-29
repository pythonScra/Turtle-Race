from turtle import *
from random import *
import time

#Setup
setup(800, 500)
title("Turtle Race")
bgcolor("darkgreen")
speed(0)

#Heading
penup()
goto(-100, 205)
color("white")
write("TURTLE RACE", font=("Arial", 20, "bold"))

#Dirt
goto(-350, 200)
pendown()
color("chocolate")
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()
#===============================================

#Finish Line:
gap_size = 20
shape("square")
penup()

#Making squares
#Start line
color("white")
for i in range(10):
    goto(-276, (170 - (i * gap_size * 2)))
    stamp()
color("black")
for i in range(10):
    goto(-276, (190 - (i * gap_size * 2)))
    stamp()

#Finish Line
#White Squares 1
color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()
#White Squares 2
for i in range(10):
    goto(250 + gap_size, (210 - gap_size) - (i * gap_size * 2))
    stamp()

#Black Squares 1
color("black")
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()
#Black Squares 2
for i in range(10):
    goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    stamp()
#================================================================

#Making the stadiums
def draw_stadium1():
    hideturtle()
    speed(10)
    color("white")
    penup()
    goto(-320, -280)
    pendown()
    for i in range(1):
        forward(700)
    for i in range(18):
        right(-10)
        forward(50)
    for i in range(1):
        forward(700)
    for i in range(18):
        right(-10)
        forward(50)
def draw_stadium2():
    speed(10)
    color("white")
    penup()
    goto(-344, -315)
    pendown()
    for i in range(1):
        forward(750)
    for i in range(20):
        right(-9)
        forward(50)
    for i in range(1):
        forward(750)
    for i in range(20):
        right(-9)
        forward(50)
draw_stadium1()
draw_stadium2()
#=============================

# Spawning the turtles:
sub1 = Turtle()
sub1.color("cyan")
sub1.shape("turtle")
sub1.shapesize(1.2)
sub1.penup()
sub1.goto(-310, 150)
sub1.pendown()

sub2 = Turtle()
sub2.color("green")
sub2.shape("turtle")
sub2.shapesize(1.2)
sub2.penup()
sub2.goto(-310, 110)
sub2.pendown()

sub3 = Turtle()
sub3.color("magenta")
sub3.shape("turtle")
sub3.shapesize(1.2)
sub3.penup()
sub3.goto(-310, 70)
sub3.pendown()

sub4 = Turtle()
sub4.color("yellow")
sub4.shape("turtle")
sub4.shapesize(1.2)
sub4.penup()
sub4.goto(-310, 30)
sub4.pendown()

sub5 = Turtle()
sub5.color("purple")
sub5.shape("turtle")
sub5.shapesize(1.2)
sub5.penup()
sub5.goto(-310, -10)
sub5.pendown()

sub6 = Turtle()
sub6.color("red")
sub6.shape("turtle")
sub6.shapesize(1.2)
sub6.penup()
sub6.goto(-310, -50)
sub6.pendown()

sub7 = Turtle()
sub7.color("grey")
sub7.shape("turtle")
sub7.shapesize(1.2)
sub7.penup()
sub7.goto(-310, -90)
sub7.pendown()

sub8 = Turtle()
sub8.color("white")
sub8.shape("turtle")
sub8.shapesize(1.2)
sub8.penup()
sub8.goto(-310, -130)
sub8.pendown()

sub9 = Turtle()
sub9.color("orange")
sub9.shape("turtle")
sub9.shapesize(1.2)
sub9.penup()
sub9.goto(-310, -170)
sub9.pendown()
#===========================================

#Making the turtles twirl
for i in range(1):
    sub1.right(360)
    sub2.left(360)
    sub3.right(360)
    sub4.left(360)
    sub5.right(360)
    sub6.left(360)
    sub7.right(360)
    sub8.left(360)
    sub9.right(360)
#==========================================

#Pause before match
time.sleep(1)
#==========================================

#Start match
def start_match():
    color("white")
    penup()
    goto(-260, 178)
    write("GO!", font=("Arial", 15, "bold"))
    hideturtle()
    time.sleep(1)
start_match()
#============================================

# Match starts
def start():
    while sub1.xcor() <= 230 and sub2.xcor() <= 230 and sub3.xcor() <= 230 and sub4.xcor() <= 230 and sub5.xcor() <= 230 and sub6.xcor() <= 230 and sub7.xcor() <= 230 and sub8.xcor() <= 230:
        sub1.forward(randint(1, 10))
        sub2.forward(randint(1, 10))
        sub3.forward(randint(1, 10))
        sub4.forward(randint(1, 10))
        sub5.forward(randint(1, 10))
        sub6.forward(randint(1, 10))
        sub7.forward(randint(1, 10))
        sub8.forward(randint(1, 10))
        sub9.forward(randint(1, 10))
start()
#===============================================

#Pause after match
time.sleep(1)
#===============================================

#Deciding who is the winner
win = 0
def winner():
  global win
  if sub1.xcor() > sub2.xcor() and sub1.xcor() > sub3.xcor() and sub1.xcor() > sub4.xcor() and sub1.xcor() > sub5.xcor() and sub1.xcor() > sub6.xcor() and sub1.xcor() > sub7.xcor() and sub1.xcor() > sub8.xcor() and sub1.xcor() > sub9.xcor():
    win = sub1
    for i in range(72):
        sub1.right(5)
        sub1.shapesize(2)
  elif sub2.xcor() > sub1.xcor() and sub2.xcor() > sub3.xcor() and sub2.xcor() > sub4.xcor() and sub2.xcor() > sub5.xcor() and sub2.xcor() > sub6.xcor() and sub2.xcor() > sub7.xcor() and sub2.xcor() > sub8.xcor() and sub2.xcor() > sub9.xcor():
    win = sub2
    for i in range(72):
        sub2.right(5)
        sub2.shapesize(2)
  elif sub3.xcor() > sub1.xcor() and sub3.xcor() > sub2.xcor() and sub3.xcor() > sub4.xcor() and sub3.xcor() > sub5.xcor() and sub3.xcor() > sub6.xcor() and sub3.xcor() > sub7.xcor() and sub3.xcor() > sub8.xcor() and sub3.xcor() > sub9.xcor():
    win = sub3
    for i in range(72):
        sub3.right(5)
        sub3.shapesize(2)
  elif sub4.xcor() > sub1.xcor() and sub4.xcor() > sub2.xcor() and sub4.xcor() > sub3.xcor() and sub4.xcor() > sub5.xcor() and sub4.xcor() > sub6.xcor() and sub4.xcor() > sub7.xcor() and sub4.xcor() > sub8.xcor() and sub4.xcor() > sub9.xcor():
    win = sub4
    for i in range(72):
        sub4.right(5)
        sub4.shapesize(2)
  elif sub5.xcor() > sub1.xcor() and sub5.xcor() > sub2.xcor() and sub5.xcor() > sub3.xcor() and sub5.xcor() > sub4.xcor() and sub5.xcor() > sub6.xcor() and sub5.xcor() > sub7.xcor() and sub5.xcor() > sub8.xcor() and sub5.xcor() > sub9.xcor():
    win = sub5
    for i in range(72):
        sub5.right(5)
        sub5.shapesize(2)
  elif sub6.xcor() > sub1.xcor() and sub6.xcor() > sub2.xcor() and sub6.xcor() > sub3.xcor() and sub6.xcor() > sub4.xcor() and sub6.xcor() > sub6.xcor() and sub6.xcor() > sub7.xcor() and sub6.xcor() > sub8.xcor() and sub6.xcor() > sub9.xcor():
    win = sub6
    for i in range(72):
        sub6.right(5)
        sub6.shapesize(2)
  elif sub7.xcor() > sub1.xcor() and sub7.xcor() > sub2.xcor() and sub7.xcor() > sub3.xcor() and sub7.xcor() > sub4.xcor() and sub7.xcor() > sub5.xcor() and sub7.xcor() > sub6.xcor() and sub7.xcor() > sub8.xcor() and sub7.xcor() > sub9.xcor():
    win = sub7
    for i in range(72):
        sub7.right(5)
        sub7.shapesize(2)
  elif sub8.xcor() > sub1.xcor() and sub8.xcor() > sub2.xcor() and sub8.xcor() > sub3.xcor() and sub8.xcor() > sub4.xcor() and sub8.xcor() > sub5.xcor() and sub8.xcor() > sub6.xcor() and sub8.xcor() > sub7.xcor() and sub8.xcor() > sub9.xcor():
      win = sub8
      for i in range(72):
          sub8.right(5)
          sub8.shapesize(2)
  else:
      win = sub9
      for i in range(72):
          sub9.right(5)
          sub9.shapesize(2)

winner()
#==================================================

#Tell who won
def tell_who_won():
    global win
    shape("arrow")
    if win == sub1:
        color("cyan")
        penup()
        goto(-130, 50)
        write("THE CYAN TURTLE WON", font=("Arial", 15, "bold"))
        hideturtle()
    if win == sub2:
        color("green")
        penup()
        goto(-130, 50)
        write("THE GREEN TURTLE WON", font=("Arial", 15, "bold"))
        hideturtle()
    if win == sub3:
        color("magenta")
        penup()
        goto(-130, 50)
        write("THE MAGENTA TURTLE WON", font=("Arial", 15, "bold"))
        hideturtle()
    if win == sub4:
        color("yellow")
        penup()
        goto(-130, 50)
        write("THE YELLOW TURTLE WON", font=("Arial", 15, "bold"))
        hideturtle()
    if win == sub5:
        color("purple")
        penup()
        goto(-130, 50)
        write("THE PURPLE TURTLE WON", font=("Arial", 15, "bold"))
        hideturtle()
    if win == sub6:
        color("red")
        penup()
        goto(-130,50)
        write("THE RED TURTLE WON", font=("Arial", 15, "bold"))
        hideturtle()
    if win == sub7:
        color("grey")
        penup()
        goto(-130, 50)
        write("THE GREY TURTLE WON", font=("Arial", 15, "bold"))
        hideturtle()
    if win == sub8:
        color("white")
        penup()
        goto(-130, 50)
        write("THE WHITE TURTLE WON", font=("Arial", 15, "bold"))
        hideturtle()
    if win == sub9:
        color("orange")
        penup()
        goto(-130, 50)
        write("THE ORANGE TURTLE WON", font=("Arial", 15, "bold"))
        hideturtle()
tell_who_won()
time.sleep(2)
#=============================================================================================