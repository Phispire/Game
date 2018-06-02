import turtle
import os



#Create game window
turtle.setup(700, 700)
Main = turtle.Screen()
Main.bgcolor("black")
Main.title("Space Invaders")



#Draw game border
border_pen = turtle.Turtle()
border_pen.hideturtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

#Create enemy
enemy = turtle.Turtle()
enemy.setposition(-275, 275)
enemy.color("Red")
enemy.shape("square")
enemy.turtlesize(.5)
enemy.speed(0)
enemy.penup()



#Create player
player = turtle.Turtle()
player.setposition(0, -275)
player.setheading(90)
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)


#Give player power to move left and right
playerspeed = 15
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -285:
        x = -285
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 285:
        x = 285
    player.setx(x)

#Keyboard Bindings
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")

enemyspeed = 2
while True:
    x = enemy.xcor()
    x += enemyspeed
    if x > 290:
        enemyspeed *= -1
    if x < -290:
        enemyspeed *= -1
    enemy.setx(x)

Main.mainloop()