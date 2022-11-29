from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# setup the difficulty of the game
def choose_level():
    speed = 0.1
    difficulty_level = ["easy", "normal", "hard", "extreme"]
    difficulty = screen.textinput(title="Select Difficulty", prompt="Easy / Normal / Hard / Extreme")
    while difficulty not in difficulty_level:
        difficulty = screen.textinput(title="Select Difficulty", prompt="Easy / Normal / Hard / Extreme")

    if difficulty.lower() == "easy":
        speed = 0.15
    elif difficulty.lower() == "normal":
        speed = 0.1
    elif difficulty.lower == "hard":
        speed = 0.08
    elif difficulty.lower() == "extreme":
        speed = 0.06
    return speed


# screen setup
screen = Screen()
speed = choose_level()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# call snake class and create snake in starting position, call food class and create the food, setup scoreboard
scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# game
game_on = True
while game_on:
    screen.update()  # make snake motion look smooth
    time.sleep(speed)
    snake.move()  # from Snake class

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset_snake()


    # Detect collision with tail
    for square in snake.all_squares[1:]:
        if snake.head.distance(square) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
