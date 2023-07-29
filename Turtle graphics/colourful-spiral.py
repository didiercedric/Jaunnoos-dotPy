import turtle

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle.bgcolor('black')

for i in range(360):
    turtle.pencolor(colors[i % len(colors)])
    turtle.width(i / 100 + 1)
    turtle.forward(i)
    turtle.left(59)

turtle.done()
