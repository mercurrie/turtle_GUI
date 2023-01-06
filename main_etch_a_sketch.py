from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def move_backward():
    tim.backward(10)


def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(clear_screen, "c")
screen.listen()
screen.exitonclick()
