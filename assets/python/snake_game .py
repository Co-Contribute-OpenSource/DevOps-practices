import turtle
from random import randint
from time import sleep

#create screen

scr = turtle.Screen()
scr.bgcolor('black')
scr.title("Snake Game")
scr.setup(width=600, height=600)
scr.listen()
scr.tracer(0)


#create snake turtle
snake = turtle.Turtle()
snake.shape('square')
snake.color('green')
#user defined property
snake.direction = "stop"
snake.speed(0)
snake.up()

#create fruit turtle
fruit = turtle.Turtle()
fruit.shape('circle')
fruit.color('red')
fruit.shapesize(0.6)
fruit.up()
fruit.goto(50,100)
fruit.speed(0)

#create writer turtle
writer = turtle.Turtle()
writer.color('white')
writer.speed(0)
writer.hideturtle()
writer.up()
writer.score = 0
writer.highscore = 0

#variables
#score = 0
#highscore = 0

# snake body
body_parts = []


def write_score() :
    writer.goto(-250,200)
    writer.write(f'score : {writer.score}',font=("Comic Sans MS",15,"normal"))
    writer.goto(100,200)
    writer.write(f'High Score : {writer.highscore}',font=("Comic Sans MS",15,"normal"))

write_score()

def move():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    if snake.direction == "down":
        snake.sety(snake.ycor() - 20)
    if snake.direction == "right":
        snake.setx(snake.xcor() + 20)
    if snake.direction == "left":
        snake.setx(snake.xcor() - 20)

def move_right():
    if snake.direction != "left":
        snake.direction = "right"
def move_left():
    if snake.direction != "right":
        snake.direction = "left"
def move_up():
    if snake.direction != "down":
        snake.direction = "up"
def move_down():
    if snake.direction != "up":
        snake.direction = "down"



#declaration or definition
def control_score():
    if snake.distance(fruit) < 16 :
        fruit.goto(randint(-250,250),randint(-220,220))
        writer.clear()
        writer.score += 10
        if writer.score > writer.highscore:
            writer.highscore = writer.score
        write_score()

        # Adding segments
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.color("Red")
        new_part.shape("square")
        new_part.pu()
        body_parts.append(new_part)

def border_collission():
    if snake.xcor()>285 or snake.xcor()<-285 or snake.ycor()>285 or snake.ycor()<-285:
            sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"
            writer.clear()
            writer.score = 0
            write_score()
            last_index = len(body_parts) -1
            for i in range(last_index, -1, -1):
                body_parts[i].hideturtle()
            body_parts.clear()

# Snake Body control
def snake_body():
    last_index = len(body_parts) - 1
    for i in range(last_index, 0, -1):
        x = body_parts[i -1].xcor()
        y = body_parts[i -1].ycor()
        body_parts[i].goto(x, y)
    if len(body_parts) > 0:
        body_parts[0].goto(snake.xcor(), snake.ycor())


def body_collision():
    for i in body_parts:
        if snake.distance(i) < 20:
            sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"
            writer.clear()
            writer.score = 0
            write_score()
            last_index = len(body_parts) -1
            for i in range(last_index, -1, -1):
                body_parts[i].hideturtle()
            body_parts.clear()

scr.onkey(move_right,"Right")
scr.onkey(move_left,"Left")
scr.onkey(move_up,"Up")
scr.onkey(move_down,"Down")

game_mode = True
while game_mode:
    scr.update()
    sleep(0.1)
    control_score()
    snake_body()
    move()
    border_collission()
    body_collision()