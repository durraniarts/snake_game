''' score board module '''
from turtle import Turtle

class Score(Turtle):
    ''' Turtle main class '''
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0 ,y=260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        ''' display the updated score '''
        self.write(arg=f"Score: {self.score}", align='center', font=('Courier', 24, 'normal'))

    def game_over(self):
        ''' display the game over '''
        self.goto(0,0)
        self.write(arg='Game Over', align='center', font=('Courier', 24, 'normal'))

    def increase_score(self):
        ''' increase the score '''
        self.score += 1
        self.clear()
        self.update_score()
