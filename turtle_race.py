from turtle import Turtle,Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=800,height=400)
user_bet =screen.textinput(title="Make your bet😎" , prompt="Which turtle will win this race? Enter your color: ")

color = ["green","purple","orange","red","yellow","blue","pink"]
new_turtle = Turtle()
y_position = [-70 , -40 ,-10 , 20, 50 ,80 ,110]


all_turtle = []
for turtle_index in range(0,7):
    new_turtle = Turtle(shape="turtle")
    random_color = random.choice(color)
    new_turtle.color(random_color)
    color.remove(random_color)
    new_turtle.penup()
    new_turtle.goto(x=-310, y= y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
     is_race_on = True    

while is_race_on:
     for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False 
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
              print(f"you won this race by chossing {user_bet}")
            else:  
              print("you lose this game.🥲")
        random_distance = random.randint(0,20)
        turtle.forward(random_distance)

screen.exitonclick()