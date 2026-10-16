
import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Pink Recursive Tree")

# Faster animation, keeping the original design
screen.tracer(8, 0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)

def tree(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.color("pink")
        t.circle(2)
        t.color("brown")

        t.left(20)
        tree(4 * i / 5)

        t.right(40)
        tree(4 * i / 5)

        t.left(20)
        t.backward(i)

# Position the turtle at the bottom
t.penup()
t.goto(0, -300)
t.setheading(90)
t.pendown()

# Draw the tree
tree(100)

screen.update()
turtle.done()
