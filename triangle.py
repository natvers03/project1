from turtle import *

class Triangle:

    def draw(self):

        pendown()
        left(30)
        forward(100)
        right(120)
        forward(100)
        right(120)
        forward(100)
        penup()
        return




t = Triangle()
t.draw()