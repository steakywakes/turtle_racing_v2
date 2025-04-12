from turtle import Turtle, Screen
from runners import Runner, COLORS
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.title("THE TURTLE AND TH-...MORE TURTLES")
screen.screensize(600, 400)
screen.tracer(0)

invalid_input = True

while invalid_input:
    user_bet = screen.textinput("Place your bet!", "Which turtle's got the turbo legs?").lower()
    if user_bet not in COLORS:
        print("Please enter a valid bet, loser. :p")
    else:
        invalid_input = False

turbo_legs = Runner()
game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    turbo_legs.run()  # Make a class for the racers, and call a run method here
    if turbo_legs.turtle_has_won():
        game_on = False
        if user_bet == turbo_legs.winning_turtle.fillcolor():
            print(f"The winner is the {turbo_legs.winning_turtle.fillcolor()} turtle! You win :)")
        else:
            print(f"The winner is the {turbo_legs.winning_turtle.fillcolor()} turtle! You lose :(")

        screen.exitonclick()