import turtle
import time
import random

delay = 0.1

# Initial Score
score = 0
highest_score = 0

# Setting up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake's head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)  # Position
head.direction = "stop"

# Snake's food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)

bodies = []

# Score Board
sb = turtle.Turtle()
sb.speed(0)
sb.shape("square")
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(0, 260)
sb.write("Score: 0  Highest Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# (Event-Handling)- Keyboard mappings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Checking for the collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the bodies
        for body in bodies:
            body.goto(1000, 1000)
        
        # Clear the bodies list
        bodies.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        sb.clear()
        sb.write("Score: {}  Highest Score: {}".format(score, highest_score), align="center", font=("Courier", 24, "normal")) 


    # Checking for the collision with the food
    if head.distance(food) < 20:
        # Moving the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Adding a body
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("grey")
        new_body.penup()
        bodies.append(new_body)

        # Shortening the delay (Increasing the Speed)
        delay -= 0.001

        # Increasing the score
        score += 10

        if score > highest_score:
            highest_score = score
        
        sb.clear()
        sb.write("Score: {}  Highest Score: {}".format(score, highest_score), align="center", font=("Courier", 24, "normal")) 

    # Moving the end bodies first in reverse order
    for index in range(len(bodies)-1, 0, -1):
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x, y)

    # Moving the bodies [0] to where the head is
    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x,y)

    move()    

    # Checking for the head collision with the bodies
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the bodies
            for body in bodies:
                body.goto(1000, 1000)
        
            # Clear the bodies list
            bodies.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Updating the scoreboard
            sb.clear()
            sb.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()