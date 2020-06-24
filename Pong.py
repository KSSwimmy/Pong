import turtle #turtle module is a module that lets you do basic graphics
import os

#window
window = turtle.Screen() # 
window.title("Pong by @ksswimmy")
window.bgcolor("black")
window.setup(width=800, height=600) # The size of the window
window.tracer(0) # Lets us speed up the game and stops the window from updating

#Paddle A 
paddle_a = turtle.Turtle() 
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B 
paddle_b = turtle.Turtle() #The object
paddle_b.speed(0) # Speed of the animation. It sets the maximum speed otherwise it would be super slow
paddle_b.shape("square") # Using a built in shape
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # making the shape longer
paddle_b.penup()
paddle_b.goto(+350,0)

#Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0) # the ball is centered
# d means delta. dx and dy means everytime our ball moves it moves 2px
ball.dx = 1.0 # This moves to the right 2px
ball.dy = -1.0 # This moves up 2px
# allowing the ball to move diagonally 

# Pen - The default score on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() # hiding the object
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal")) 

# Score
score_a = 0 
score_b = 0

# Function for paddle A to go up
def paddle_a_up(): 
    y = paddle_a.ycor() # y coordinate (from turtle)
    y += 20
    paddle_a.sety(y)

#Keyboard binding 
window.listen() # An event listener for the window 
window.onkeypress(paddle_a_up, "w") # when "w" is pressed 


# Function for paddle to go up
def paddle_a_down(): 
    y = paddle_a.ycor() # y coordinate (from turtle)
    y -= 20
    paddle_a.sety(y)

#Keyboard binding 

window.onkeypress(paddle_a_down, "s") # when "w" is pressed 

#/////////////////////////////////////////////////////////////////////////

# Function for paddle B to go up
def paddle_b_up(): 
    y = paddle_b.ycor() # y coordinate (from turtle)
    y += 20
    paddle_b.sety(y)

#Keyboard binding 
window.onkeypress(paddle_b_up, "Up") # when "Up" (arrow key) is pressed 


# Function for paddle to go up
def paddle_b_down(): 
    y = paddle_b.ycor() # x coordinate (from turtle)
    y -= 20
    paddle_b.sety(y)

#Keyboard binding 

window.onkeypress(paddle_b_down, "Down") # when "Down" (arrow key) is pressed 


# Main Game Loop
while True: 
    window.update() # everytime the loop runs it updates the screen. With out this IT WILL NOT WORK! THE SCREEN WILL NOT SHOW!

    # Move the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # top order checking
    if ball.ycor() > 290: # if the current ycor is grater than 290
        ball.sety(290) # we set it back to 290
        ball.dy *= -1 # and this reverses the direction
        os.system("afplay bounce.wav&") # sound

    # bottom Border checking
    if ball.ycor() < -290: # if the current ycor is grater than 290
        ball.sety(-290) # we set it back to 290
        ball.dy *= -1 # and this reverses the direction
        os.system("afplay bounce.wav&")

    # right side border
    if ball.xcor() > 390: # if the ball is going past the paddle and it's off the screen
        ball.goto(0, 0) # then the ball will be put back to the center
        ball.dx *= -1 # and this reverses the direction
        score_a += 1 
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) 


    # left side border
    if ball.xcor() < -390: # if the ball is going past the paddle and it's off the screen
        ball.goto(0, 0) # then the ball will be put back to the center
        ball.dx *= -1 # and this reverses the direction
        score_b += 1
        pen.clear()
        pen.write("Player A: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) 


    #Paddle b and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40): 
            ball.setx(340)
            ball.dx *= -1 
            os.system("afplay bounce.wav&")


    #Paddle a and ball collisions
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40): 
            ball.setx(-340)
            ball.dx *= -1 
            os.system("afplay bounce.wav&")
