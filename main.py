from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("#191919")
screen.setup(width=800, height=600)
screen.title("PyPong")

paddle = Turtle("square")
paddle.color("white")
paddle.penup()
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(350, 0)


def up():
    new_y = 0
    new_y += 200
    paddle.goto(350, new_y)


def down():
    new_y = 0
    new_y -= 200
    paddle.goto(350, new_y)


screen.listen()
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)



# game_on = True
# while game_on:
#     up()
#     down()

screen.exitonclick()
