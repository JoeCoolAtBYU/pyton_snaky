import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from src.snake import Snake

COLLISION_DISTANCE = 15
game_is_on = False
food = Food()
scoreboard = ScoreBoard()
screen = Screen()
snake = Snake()


class Game:
    def __init__(self):

        self.game_is_on = True
        self.screen = Screen()
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = ScoreBoard()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snaky")
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkey(snake.up, "Up")
        self.screen.onkey(snake.down, "Down")
        self.screen.onkey(snake.left, "Left")
        self.screen.onkey(snake.right, "Right")

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < COLLISION_DISTANCE:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect Collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            game_is_on = False
            scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    screen.exitonclick()
