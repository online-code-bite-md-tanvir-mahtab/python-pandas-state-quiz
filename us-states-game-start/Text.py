from turtle import Turtle


class Text(Turtle):

    def __init__(self):
        super().__init__()
        self.color('red')
        self.penup()
        self.hideturtle()

    
    def make_text(self,text,x,y):
        self.goto(x=x,y=y)
        self.write(f"{text}")

