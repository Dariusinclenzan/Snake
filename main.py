import time
import turtle
import snek
import food
from score import Score

screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Snek")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
snake = snek.Snek()
food = food.Food()
scoreboard = Score()





game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.movement()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.reset_food()
        snake.extend()
        scoreboard.new_score()

    # Detect collision with wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        game_on = False



    for segments in snake.parts[1:]:
        if snake.head.distance(segments) < 15:
            scoreboard.reset()
            game_on = False

scoreboard.game_over()
screen.update()
def continue_game():
    screen.clearscreen()
    exec(open(__file__).read())

def quit_game():
    screen.bye()

screen.onkey(continue_game, 'y')
screen.onkey(quit_game, 'n')


screen.mainloop()
