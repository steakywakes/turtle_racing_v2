from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue']
STARTING_POSITIONS = [(-345, 300), (-345, 150), (-345, 0), (-345, -150), (-345, -300)]
MAX_SPEED = 10
ACCELERATION = random.randint(1, 5)

class Runner(Turtle):
    """A class for each turtle runner, with a move, game_over and user_bet method"""
    def __init__(self):
        self.runners = []
        self.winning_turtle = ''
        super().__init__()
        self.create_runner()

    def create_runner(self):
        for i in range(5):
            reptilian = Turtle()
            reptilian.shape("turtle")
            reptilian.color(COLORS[i])
            reptilian.penup()
            reptilian.goto(STARTING_POSITIONS[i])
            self.runners.append(reptilian)

    def run(self):
        for i in self.runners:
            i.forward(ACCELERATION * random.randint(1, MAX_SPEED))

    def turtle_has_won(self):
        for runner in self.runners:
            if runner.xcor() >= 365:
                self.winning_turtle = runner
                return True