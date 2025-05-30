from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('greenYellow')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-60, 250)
        self.write(self.left_score, align='center', font=('Courier', 50, 'bold'))
        self.goto(60, 250)
        self.write(self.right_score, align='center', font=('Courier', 50, 'bold'))

    def left_point(self):
        self.left_score +=1
        self.update_scoreboard()

    def right_point(self):
        self.right_score +=1
        self.update_scoreboard()

