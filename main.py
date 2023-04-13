from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Сделай свой выбор", prompt="Какая черепаха победит?")
colors = ["red", "blue", "green", "orange", "purple", "black"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtel_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtel_index])
    new_turtle.goto(x=-230, y=y_positions[turtel_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("Твоя черепашка выиграла!")
            else:
                print("LOOSER!!!")

        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)

screen.exitonclick()



