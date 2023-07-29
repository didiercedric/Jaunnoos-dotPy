import turtle

def draw_spiral():
    turtle.speed(0)  # Set the drawing speed to the fastest

    for i in range(360):
        turtle.forward(i)
        turtle.right(59)

    turtle.done()

draw_spiral()
