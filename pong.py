import math
import time
from turtle import Screen, Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.color("white")

    def game_over(self, p1_won):
        self.goto(0, 0)
        if p1_won:
            self.write("Player 1 WON", True, align="center", font=("", 40, ""))
        else:
            self.write("Player 2 WON", True, align="center", font=("", 40, ""))


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1


class Paddle(Turtle):
    def __init__(self, is_player1):
        super().__init__()
        self.penup()
        self.shape("square")
        # Each turtle starts at 20x20
        self.shapesize(5, 1)
        self.color("white")
        if is_player1:
            self.goto(350, 0)

        else:
            self.goto(-350, 0)

    def up(self):
        if self.ycor() - 20 > 225:
            return
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() - 20 < -225:
            return
        self.goto(self.xcor(), self.ycor() - 20)


class PongGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.title("PONG")
        self.move_speed = 0.3

        self.p1 = Paddle(True)
        self.p2 = Paddle(False)

        self.ball = Ball()

    def play(self):
        p1_won = False
        self.screen.onkey(self.p1.up, "Up")
        self.screen.onkey(self.p1.down, "Down")
        self.screen.onkey(self.p2.up, "w")
        self.screen.onkey(self.p2.down, "s")
        self.screen.listen()

        while True:
            self.ball.move()
            if self.ball.xcor() > 380:
                p1_won = True
                break
            if self.ball.xcor() < -380:
                p1_won = False
                break

            if math.fabs(self.ball.ycor()) > 280:
                self.ball.bounce_y()

            if self.ball.distance(self.p1) < 50 and self.ball.xcor() > 320 or \
                    self.ball.distance(self.p2) < 50 and self.ball.xcor() < -320:
                self.ball.bounce_x()
                self.move_speed *= 0.9

            # if self.ball.distance(self.p2.xcor(), self.ball.ycor()) < 10:
            #     self.ball.bounce_x()

            time.sleep(self.move_speed)
            self.screen.update()

        s = ScoreBoard()
        s.game_over(p1_won)
        self.screen.update()

        self.screen.exitonclick()
