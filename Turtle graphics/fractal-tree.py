# Import the Turtle module to use for drawing graphics

import turtle

# Set up the turtle window 
screen = turtle.Screen()
screen.bgcolor("black")       # Set the background color to black
turtle.speed(0)               # Set the turtle's speed to the maximum (fastest)
turtle.pensize(2)             # Set the width of the pen (turtle's drawing line)

# Function to draw the fractal tree
def draw_fractal_tree(branch_length, t):
    # Base case: If the branch length is too small, stop drawing (terminate recursion)
    if branch_length > 5:
        # Draw the main branch with a green color
        t.pencolor("green")
        t.forward(branch_length)

        # Draw the right sub-branch (with a smaller angle)
        t.right(20)
        draw_fractal_tree(branch_length - 15, t)

        # Return to the original position and orientation
        t.left(40)

        # Draw the left sub-branch (with a larger angle)
        draw_fractal_tree(branch_length - 15, t)

        # Return to the original position and orientation
        t.right(20)
        t.backward(branch_length)

# Set the starting position of the turtle
turtle.left(90)          # Turn the turtle 90 degrees to the left (facing upward)
turtle.up()              # Lift the pen up (stop drawing while moving)
turtle.setpos(0, -200)   # Set the turtle's position to the coordinates (0, -200) on the screen
turtle.down()            # Put the pen down (start drawing again)

# Draw the fractal tree with a starting branch length of 100
draw_fractal_tree(100, turtle)

# Hide the turtle (the drawing pen) and display the result on the screen
turtle.hideturtle()
screen.mainloop()        # Keep the turtle graphics window open and responsive
