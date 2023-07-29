#Random Square Drawer
##This Python program uses the turtle module to draw squares at random positions on the screen. It provides a simple graphical representation using the turtle graphics environment.

#Prerequisites
##- Python 3.11.3
##- turtle module (usually comes pre-installed with Python)

#Usage

##When you run the script, it will draw 10 squares at random positions on the screen. Each square will have a side length of 100 pixels.
##The turtle moves quickly due to the 'fast' speed setting. You can modify the code to change the number of squares, their side length, or the speed of the turtle.



import turtle
import random

tortue = turtle.Turtle()

tortue.speed('fast')
tortue.shape('turtle')

def carre(longeur):
    cotes = 4
    angle = 90
    for i in range(cotes):
        tortue.forward(longeur)
        tortue.right(angle)

for i in range(10):
    x = random.randint(1, 200)
    y = random.randint(1, 200)
    tortue.goto(x,y)
    carre(100)
