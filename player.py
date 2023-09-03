import turtle
from turtle import Turtle

MOVE_DISTANCE = 6
BULLET_START_INCREASE = 18
BULLET_MOVE = 5
SCREEN_LIMIT = 315


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.extra_lives = []
        self.bullet = None
        self.hideturtle()
        self.player = None
        self.extra_live = None
        self.can_fire = True
        self.create_player()
        self.create_extra_lives()

    def create_player(self):
        self.player = Turtle()
        self.player.speed(0)
        self.player.shape("triangle")
        self.player.penup()
        self.player.color("green")
        self.player.goto(0, -230)
        self.player.setheading(90)
        self.set_weapon()

    def create_extra_lives(self):
        for i in range(2):
            self.extra_live = Turtle()
            self.extra_live.shape("triangle")
            self.extra_live.penup()
            self.extra_live.color("green")
            self.extra_live.setheading(90)
            self.extra_lives.append(self.extra_live)
        self.extra_lives[0].goto(-380, -286)
        self.extra_lives[1].goto(-344, -286)

    def move_left(self):
        if self.player.xcor() <= -402.00:
            pass
        else:
            self.player.goto(self.player.xcor() - MOVE_DISTANCE, self.player.ycor())

    def move_right(self):
        if self.player.xcor() >= 396.00:
            pass
        else:
            self.player.goto(self.player.xcor() + MOVE_DISTANCE, self.player.ycor())

    def move_player(self):
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")
        self.screen.onkey(self.fire, "space")

    def set_weapon(self):
        self.bullet = Turtle()
        self.bullet.hideturtle()
        self.bullet.speed(0)
        self.bullet.shape("square")
        self.bullet.penup()
        self.bullet.color("white")
        self.bullet.setheading(90)
        self.bullet.shapesize(0.1, 0.5)
        self.bullet.goto(self.player.xcor(), self.player.ycor() + BULLET_START_INCREASE)

    def fire(self):
        if self.can_fire:
            self.set_weapon()
            self.move_bullet()
            self.can_fire = False

    def move_bullet(self):
        if self.bullet.ycor() > SCREEN_LIMIT:
            self.bullet.hideturtle()
            self.set_weapon()
            self.can_fire = True
        else:
            self.bullet.showturtle()
            self.bullet.forward(BULLET_MOVE)
            turtle.ontimer(self.move_bullet, 1)
