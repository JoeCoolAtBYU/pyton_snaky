import time
from turtle import Screen, Turtle

from food import Food
from scoreboard import ScoreBoard
from snake import Snake
import tkinter
import os

COLLISION_DISTANCE = 15

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "images", "snake.png")


game_is_on = True
screen = Screen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.setup(width=800, height=800)
img = tkinter.Image("photo", file=image_path)
screen._root.iconphoto(True, img)
screen.bgcolor("black")
screen.title("Snaky")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def create_border():
    border = Turtle()
    border.speed(0)
    border.color("white")
    border.penup()
    border.goto(-290, -290)
    border.pendown()
    border.pensize(3)
    for _ in range(4):
        border.fd(580)
        border.lt(90)
    border.hideturtle()

create_border()

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
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    if not game_is_on:
        play_again = screen.textinput("Play again?", "Would you like to play again (yes or no)", )
        if play_again.lower() == "yes":
            screen.reset()
            screen.tracer(0)
            screen.listen()
            screen.onkey(snake.up, "Up")
            screen.onkey(snake.down, "Down")
            screen.onkey(snake.left, "Left")
            screen.onkey(snake.right, "Right")
            snake.reset()
            scoreboard.reset()
            scoreboard = ScoreBoard()
            food = Food()
            create_border()
            game_is_on = True
        else:
            screen.bye()

screen.exitonclick()