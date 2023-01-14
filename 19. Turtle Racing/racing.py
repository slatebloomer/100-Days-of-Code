from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

colours = ["red", "orange", "blue", "green", "pink", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == "user_bet":
                print("You win!")
            else:
                print(f"You lose! The winning colour was {winning_colour}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()


