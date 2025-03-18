import turtle

try:

    with open("highscore.txt", mode="r") as highscore:
        current_hs = highscore.read()
except:
    with open('highscore.txt', mode='w') as highscore:
        highscore.write('0')
        current_hs = 0


class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.high_score = current_hs
        self.penup()
        self.sety(270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}   High Score: {self.high_score} ", False, align="center", font=("Arial", 14, "normal"))


    def new_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.sety(50)
        self.write('                Game Over\n\nWould you like to continue? Y / N', False, align='center', font=('Arial', 20, 'normal'))



    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("highscore.txt", mode="w") as highscore:
                highscore.write(f"{self.high_score}")

        self.sety(270)
        self.score = 0
        self.update_score()