from turtle import Turtle


class GameBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.winner_msg = None
        self.end_game = None
        self.score_label = None
        self.score = 0
        self.penup()
        self.pencolor("green")
        self.goto(-425, -260)
        self.pendown()
        self.goto(450, -260)
        self.score_keeper()

    def score_keeper(self):
        self.score_label = Turtle()
        self.score_label.hideturtle()
        self.score_label.color("green")
        self.score_label.penup()
        self.score_label.goto(380, -297)
        self.score_label.write(f"Score: {self.score}", align="right", font=("Score Board", 18, "bold"))

    def update_score(self):
        self.score_label.clear()
        self.score_label.penup()
        self.score_label.write(f"Score: {self.score}", align="right", font=("Score Board", 18, "bold"))

    def game_over(self):
        self.end_game = Turtle()
        self.end_game.color("green")
        self.end_game.penup()
        self.end_game.hideturtle()
        self.end_game.write("GAME OVER!", align="center", font=("Score Board", 70, "bold"))

    def set_winner(self):
        if self.winner_msg is None:
            self.winner_msg = Turtle()
            self.winner_msg.color("green")
            self.winner_msg.penup()
            self.winner_msg.hideturtle()
        self.winner_msg.write("You win!", align="center", font=("Score Board", 70, "bold"))
