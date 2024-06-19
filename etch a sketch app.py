from turtle import Turtle,Screen

tom = Turtle()
tom.color("green")

def forward():
    tom.forward(100)
def backward():
    tom.backward(100)
def turnright():
    new_heading = tom.heading() + 10
    tom.setheading(new_heading)
def turnleft():
    new_heading = tom.heading() - 10
    tom.setheading(new_heading)
def clear():
    tom.clear()
    

screen = Screen()
screen.listen()
screen.onkey(forward,"w")
screen.onkey(backward,"s")
screen.onkey(turnright,"a")
screen.onkey(turnleft,"d")
screen.onkey(clear,"c")


screen.exitonclick()