import turtle #turtle module is a module that lets you do basic graphics

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
ball.goto(0,0)

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
window.listen() # An event listener for the window 
window.onkeypress(paddle_a_down, "s") # when "w" is pressed 




# Main Game Loop
while True: 
    window.update() # everytime the loop runs it updates the screen. With out this IT WILL NOT WORK! THE SCREEN WILL NOT SHOW!