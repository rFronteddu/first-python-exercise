import math
import random
import time
from turtle import Screen, Turtle

MOVE_DISTANCE = 20


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.color("white")
        self.update(0)

    def update(self, new_score):
        self.clear()
        self.score = new_score + self.score
        self.goto(0, 270)

        self.write(f"Score: {self.score}", True, align="center", font=("", 20, ""))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align="center", font=("", 40, ""))
        pass


class Snake:
    def __init__(self):

        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.title("SNAKE")

        self.food = Food()
        self.score_board = ScoreBoard()

        self.screen.onkey(self.up, "w")
        self.screen.onkey(self.down, "s")
        self.screen.onkey(self.left, "a")
        self.screen.onkey(self.right, "d")
        self.screen.listen()

        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.screen.update()
        for position in self.starting_positions:
            self.add_segment(position)

        self.head = self.segments[0]

    def up(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            return
        self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            return
        self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            return
        self.head.setheading(180)

    def right(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            return
        self.head.setheading(0)

    def move(self):
        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.move_forward()
            if self.head.distance(self.food) < 15:
                self.food.refresh()
                self.score_board.update(1)
                self.extend()
            if math.fabs(self.head.xcor()) > 280 or math.fabs(self.head.ycor()) > 280:
                break
            for segment in self.segments[1:]:
                if self.head.distance(segment) < 10:
                    game_is_on = False
                    break

        self.score_board.game_over()
        self.screen.exitonclick()

    def move_forward(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            last_x = self.segments[seg_num - 1].xcor()
            last_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(last_x, last_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        t = Turtle()
        t.penup()
        t.shape("square")
        t.shapesize = 10
        t.color("white")
        t.goto(position)
        self.segments.append(t)
