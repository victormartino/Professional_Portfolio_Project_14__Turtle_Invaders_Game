from turtle import Turtle
import random
import turtle

ENEMIES_PER_ROW = 8
ROW_NUM = 3
SPACING = 31
BULLET_START_INCREASE = 10
SCREEN_LIMIT = - 350
BULLET_MOVE = 5


class Enemies(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.all_rows = []
        self.all_bullets = []
        self.new_enemy = None
        self.x_move = 3
        self.speed(0)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.row_y_start = self.screen_height / 2.4  # Tried some random numbers until I achieved the result I wanted
        self.row_x_start = self.screen_width / - 8
        self.create_enemies()

    def create_enemies(self):
        for i in range(3):
            enemy_row = []
            for enemy in range(ENEMIES_PER_ROW):
                new_enemy = Turtle()
                new_enemy.shape("turtle")
                new_enemy.color("green")
                new_enemy.penup()
                new_enemy.goto(self.row_x_start, self.row_y_start)
                new_enemy.setheading(-90)
                enemy_row.append(new_enemy)
            new_x_position = self.row_x_start
            for _ in enemy_row:
                _.goto(new_x_position, _.pos()[1])
                new_x_position += SPACING
            self.all_rows.append(enemy_row)
        new_vertical_spacing = SPACING
        for row in self.all_rows[1:]:
            for enemy in row:
                enemy.goto(enemy.pos()[0], enemy.pos()[1] - new_vertical_spacing)
            new_vertical_spacing += new_vertical_spacing
        self.set_weapon()

    def move_enemies(self):
        # If either the first enemy (on the left) of the first row or the last enemy (on the right) of the first row
        # reach the screen boundaries I set, they invert the side they are moving to
        if self.all_rows[0][0].xcor() <= -402 or self.all_rows[0][-1].xcor() >= 396:
            self.x_move *= -1
        for row in self.all_rows:
            for enemy in row:
                enemy.goto(enemy.xcor() - self.x_move, enemy.ycor())

    def set_weapon(self):
        num_rows = len(self.all_rows)
        random_row_index = random.randint(0, num_rows - 1)
        chosen_enemy = random.choice(self.all_rows[random_row_index])
        bullet = Turtle()
        bullet.hideturtle()
        bullet.speed(0)
        bullet.shape("square")
        bullet.penup()
        bullet.color("red")
        bullet.setheading(90)
        bullet.shapesize(0.1, 0.5)
        bullet.goto(chosen_enemy.xcor(), chosen_enemy.ycor() - BULLET_START_INCREASE)
        self.all_bullets.append(bullet)
        self.fire(bullet)
        turtle.ontimer(self.set_weapon, 700)

    def fire(self, bullet):
        if bullet:
            if bullet.ycor() < SCREEN_LIMIT:
                bullet.hideturtle()
                bullet.clear()
            else:
                bullet.showturtle()
                bullet.backward(BULLET_MOVE)
                try:
                    turtle.ontimer(lambda: self.fire(bullet), 1)
                except ValueError:
                    pass
