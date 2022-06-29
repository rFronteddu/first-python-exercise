from turtle import Turtle, Screen


class InteractiveTurtle:
    def __init__(self):
        self.tim = Turtle()
        self.screen = Screen()

    def run1(self):
        self.screen.listen()
        self.screen.onkey(key="space", fun=self.move_forward)
        self.screen.onkey(key="d", fun=self.turn_right)
        self.screen.onkey(key="a", fun=self.turn_left)
        self.screen.exitonclick()

    def move_forward(self):
        self.tim.forward(50)

    def turn_left(self):
        self.tim.left(10)

    def turn_right(self):
        self.tim.right(10)
