from prettytable import PrettyTable

import pong
import snake_game
from first_examples import Turtle1


class User:
    def __init__(self, age):
        self.age = age
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# Experimenting with creating classes, the turtle and pretty table libraries
if __name__ == '__main__':
    turtle_1 = Turtle1()

    # turtle_1.draw_random_path()
    # turtle_1.draw_circles()

    # turtle = interactive.InteractiveTurtle()
    # turtle.run1()

    # snake = snake_game.Snake()
    # snake.move()

    game = pong.PongGame()
    game.play()
