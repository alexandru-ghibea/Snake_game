from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

#TODO 0: Set up the Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
#TODO 3. Control the Snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_one = True
while game_one:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #TODO 4 Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # TODO 6 Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.rest()
        snake.reset()
    #TODO 7 collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.rest()
            snake.reset()
screen.exitonclick()

