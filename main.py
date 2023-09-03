from turtle import Screen
from gameboard import GameBoard
from player import Player
from walls import Walls
from enemies import Enemies

screen = Screen()
screen.bgcolor("black")
screen.setup(850, 630, starty=10)
screen.title("Turtle Invaders!")
screen.tracer(0)
screen.listen()
screen.cv._rootwindow.resizable(False, False)

board = GameBoard()
player = Player()
player.set_weapon()
walls = Walls()
enemies = Enemies(screen.window_width(), screen.window_height())
screen.update()


game_over = False
while not game_over:
    player.move_player()
    enemies.move_enemies()
    for bullet in enemies.all_bullets:
        for wall in walls.all_walls:
            for brick in wall:
                if bullet.distance(brick) < 4:
                    brick.clear()
                    brick.hideturtle()
                    brick.setposition(1000, -1000)
                    bullet.setposition(1000, -1000)
                    bullet.hideturtle()
        if bullet.ycor() < 200:
            if bullet.distance(player.player) < 12:
                bullet.setposition(1000, 1000)
                bullet.hideturtle()
                player.player.hideturtle()
                player.player.setposition(1000, -1000)
                player.bullet.hideturtle()
                screen.update()
                try:
                    player.extra_lives[-1].hideturtle()
                    player.extra_lives.remove(player.extra_lives[-1])
                except IndexError:
                    board.game_over()
                    screen.update()
                    game_over = True
                    break
                else:
                    player.create_player()
    for row in enemies.all_rows:
        for enemy in row:
            if enemy.distance(player.bullet) < 12:
                enemy.hideturtle()
                enemy.goto(1000, -1000)
                player.bullet.hideturtle()
                player.bullet.setposition(1000, 1000)
                board.score += 1
                board.update_score()
                if board.score == 24:
                    board.set_winner()
                    game_over = True
                    break
    screen.update()

screen.mainloop()
