from turtle import Turtle, Screen
import time
import random

# Function to create a new food at a random location
def create_food():
    food = Turtle('circle')
    food.color('red')
    food.penup()
    food.shapesize(stretch_wid=0.5, stretch_len=0.5)
    food.setx(random.randint(-280, 280))
    food.sety(random.randint(-280, 280))
    return food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Welcome to Snake")
screen.tracer(0)

snake_body = []
for _ in range(3):
    body = Turtle('square')
    body.color('white')
    body.penup()
    snake_body.append(body)

food = create_food()

# Event handling functions
def go_up():
    if snake_body[0].heading() != 270:
        snake_body[0].setheading(90)

def go_down():
    if snake_body[0].heading() != 90:
        snake_body[0].setheading(270)

def go_left():
    if snake_body[0].heading() != 0:
        snake_body[0].setheading(180)

def go_right():
    if snake_body[0].heading() != 180:
        snake_body[0].setheading(0)

# Event bindings
screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')

score = 0

while True:
    screen.update()
    time.sleep(0.2)

    for i in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[i - 1].xcor()
        new_y = snake_body[i - 1].ycor()
        snake_body[i].goto(new_x, new_y)

    snake_body[0].forward(20)

    # Check for collision with food
    if snake_body[0].distance(food) < 15:
        food.hideturtle()
        food = create_food()
        new_body = Turtle('square')
        new_body.color('white')
        new_body.penup()
        snake_body.append(new_body)
        score += 1

    # Check for screen boundaries to exit the game
    if (
        snake_body[0].xcor() > 290
        or snake_body[0].xcor() < -290
        or snake_body[0].ycor() > 290
        or snake_body[0].ycor() < -290
    ):
        screen.bye()

    # Check for collision with the snake's own body
    for body in snake_body[1:]:
        if snake_body[0].distance(body) < 10:
            screen.bye()

# Close the window when the loop exits
screen.bye()
