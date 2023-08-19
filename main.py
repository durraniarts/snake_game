''' Main module file '''
from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score

snake = Snake()
food = Food()
score = Score()



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

screen.listen()
screen.onkey(snake.move_up,'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.move_left, 'Left')
screen.onkey(snake.move_right, 'Right')



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # for segment in snake.segments:
    #     if segment != snake.head:
    #         if snake.head.distance(segment) < 10:
    #             game_is_on = False
    #             score.game_over()

    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()



screen.exitonclick()
