from turtle import Turtle

ALIGNMENT = "center"

FONT_BOLD_ = ("Courier", 15, "bold")
FONT_BOLD_LARGE = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as datafile:
            self.high_score = int(datafile.read())
        self.penup()
        self.color("white")
        self.goto(x=0, y=260)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT_BOLD_)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as datafile:
                datafile.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def new_game(self):
        self.__init__()