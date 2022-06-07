#TODO LIST for Snake Game:
    #TODO 0: Setup screen
    #TODO 1. Create Snake Body
    #TODO 2. Move the Snake
    #TODO 3. Control the Snake
    #TODO 4. Detect collision with food
    #TODO 5. Create Scoreboard
    #TODO 6. Detect collision with wall
    #TODO 7. Detect collision with tail/body of the snake
    #TODO 8. Keep track of high score

#TODO 0: Set up the Screen
from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

#TODO 1. Create Snake Body
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_one = True
while game_one:
    screen.update()
    time.sleep(0.1)
# TODO 2. Move the Snake
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)
screen.exitonclick()
