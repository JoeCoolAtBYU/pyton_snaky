from turtle import Turtle

ALIGNMENT = "center"

FONT_BOLD_ = ("Courier", 15, "bold")
FONT_BOLD_LARGE = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(x=0, y=260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT_BOLD_)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,220)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_BOLD_LARGE)

    def new_game(self):
        self.__init__()