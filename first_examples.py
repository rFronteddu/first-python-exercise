import random
import turtle
from turtle import Turtle, Screen


class Turtle1:
    pass

    @staticmethod
    def draw_square():
        timmy = Turtle()
        timmy.color("green")
        timmy.shape("turtle")

        my_screen = Screen()
        for _ in range(4):
            timmy.forward(100)
            timmy.right(90)

        my_screen.exitonclick()

    @staticmethod
    def draw_dashed_line():
        timmy = Turtle()
        timmy.color("green")
        timmy.shape("turtle")

        my_screen = Screen()

        for _ in range(10):
            if timmy.isdown():
                timmy.up()
            else:
                timmy.down()
            timmy.forward(10)

        my_screen.exitonclick()

    @staticmethod
    def draw_multiple_shapes():
        timmy = Turtle()
        timmy.color("green")
        timmy.shape("turtle")

        my_screen = Screen()
        for sides in range(3, 12):
            angle = 360 / sides
            for _ in range(sides):
                timmy.forward(100)
                timmy.right(angle)

        my_screen.exitonclick()

    @staticmethod
    def draw_random_path():
        timmy = Turtle()
        timmy.shape("turtle")
        timmy.speed("fastest")
        my_screen = Screen()
        direction = [0, 90, 180, 270, -90, -180, -270]
        turtle.colormode(255)

        for _ in range(100):
            angle = random.choice(direction)

            timmy.color(random_color())
            timmy.setheading(angle)
            timmy.forward(100)

        my_screen.exitonclick()

    @staticmethod
    def draw_circles():
        timmy = Turtle()
        timmy.shape("turtle")
        timmy.speed("fastest")
        my_screen = Screen()
        turtle.colormode(255)

        for angle in range(0, 360, 10):
            timmy.color(random_color())
            timmy.setheading(angle)
            timmy.circle(100)

        my_screen.exitonclick()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
