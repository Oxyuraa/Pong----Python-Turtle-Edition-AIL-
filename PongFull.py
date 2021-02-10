##--------------------------------
#--Modules
import turtle
from time import sleep as wait
import functools

##-------------------------------
#--Making the screen

window = turtle.Screen()
window.title("Pong! - Python Edition")
try:
    window.bgpic("background.png")
except:
    pass
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

##-----------------------------------------------------
#--Making a Text Turtle to draw all the text

text = turtle.Turtle()
text.speed(0)
text.color('white')
text.penup()

##----------------------------------------------------
#--Main Menu ball

displayball = turtle.Turtle()
displayball.speed(0)
displayball.shape("circle")
displayball.color("silver")
displayball.penup()

displayball.goto(0, 0)
displayball.dx = 0.5
displayball.dy = 0.5

##------------------------------------------------------
#--Functions
def  DisplayBallCollisions(ball):       #- only for the display ball

     while True:
        window.update()

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290 or ball.ycor() < -290 :
                ball.dy *= -1

        if ball.xcor() > 390 or ball.xcor() < -390:
                ball.dx *= -1	

def clearscreen():      #--Resetting everything 
    window.clear()
    try:
        window.bgpic("background.png")
    except:
        pass
    window.tracer(0)
    window.bgcolor('black')
	
def restart():
     PlayerNameTaker()
     
def mainGame(playerA, playerB, maxScore):
    clearscreen()

    #--Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("red")
    paddle_a.penup()
    paddle_a.goto(-350, 0)
    paddle_a.shapesize(5, 1)
    
    #--Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("blue")
    paddle_b.penup()
    paddle_b.goto(350, 0)
    paddle_b.shapesize(5, 1)


    #--Ball	(game ball)
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("silver")
    ball.penup()	
    ball.goto(0, 0)
    ball.dx = 0.75
    ball.dy = 0.75

    text.goto(0,30)
    text.write( playerA + " : 0  "+ playerB + " : 0", align='center', font=('Courier', 24, 'bold'))
    
    #--ScoreCounters
    scoreA = "0"
    scoreB = "0"
    
    #--Paddle Movement Functions
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 60
        paddle_a.sety(y)


    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 60
        paddle_a.sety(y)


    def paddle_b_up():
        y = paddle_b.ycor()
        y += 60
        paddle_b.sety(y)


    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 60
        paddle_b.sety(y)
        
    #-------------------------------------------------------
    #--Keybinds for the paddles

    window.listen()
    
    #-Paddle A
    window.onkeypress(paddle_a_up, "w")
    window.onkeypress(paddle_a_down, "s")

    #-Paddle B
    window.onkeypress(paddle_b_up, "Up")
    window.onkeypress(paddle_b_down, "Down")
    #------------------------------------------------------------------
    #--Main game (looped)

    while True:
        window.update()
        #--Move them ball
	
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
	
    #-------------------------------------------------------
        #--Border collision checks

        #--ball collisions
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.dy *= -1

    #-if ball is beyond the paddle limits     
        #--Paddle B's side
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            scoreA = int(scoreA) + 1
            text.clear()
            text.write(playerA + " : "+ str(scoreA) +"  " + playerB +" : " + str(scoreB), align='center', font=('Courier', 24, 'bold'))
            
        #--Paddle A's side
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            scoreB = int(scoreB) + 1
            text.clear()
            text.write(playerA + " : " + str(scoreA) +"  " + playerB +" : " + str(scoreB), align='center', font=('Courier', 24, 'bold'))
            
        #--Paddle collisions
        if paddle_a.ycor() >290:
            y = paddle_a.ycor()
            y -= 5
            paddle_a.sety(y)
        
        if paddle_a.ycor() < -290:
            y = paddle_a.ycor()
            y += 5
            paddle_a.sety(y)

        if paddle_b.ycor() > 290:
            y = paddle_b.ycor()
            y -= 5
            paddle_b.sety(y)
        
        if paddle_b.ycor() < -290:
            y = paddle_b.ycor()
            y += 5
            paddle_b.sety(y)
    
	
        #--Paddle and ball collisions  (the main stuff)
	
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
            ball.setx(-340)
            ball.dx *= -1

        #--If any of the player exceeds the score limit
        if maxScore <= int(scoreA) :
            clearscreen()
            text.write(playerA + " won the match after getting " + str(scoreA) + " point/s", align = 'center', font = ('courier',19,'bold'))
            print(playerA + " won the match after getting " + str(scoreA) + " point/s")
            text.sety(-50)
            text.color('silver')
            text.write("Press H to restart the game", align = 'center', font = ('courier',20,'bold'))
            text.color('white')

            window.listen()
            window.onkeypress(restart,'h')
            break
            
        if maxScore <= int(scoreB) :
            clearscreen()
            text.write(playerB + " won the match after getting " + str(scoreB) + " point/s", align = 'center', font = ('courier',19,'bold'))
            print(playerB + " won the match after getting " + str(scoreB) + " point/s")
            text.sety(-50)
            text.color('silver')
            text.write("Press H to restart the game", align = 'center', font = ('courier',20,'bold'))
            text.color('white')

            window.listen()
            window.onkeypress(restart,'h')
            break

def PlayerNameTaker():
    print("--" * 30)
    clearscreen()
    
    #--Writing the text, and taking player's names
    text.goto(-350,200)
    text.write("Player A = ", align = "left", font = ("courier",20, "bold"))
    text.sety(150)
    text.write("Player B = ", align = "left", font = ("courier",20, "bold"))
    text.sety(100)
    text.write("Score needed to win : ", align = "left", font = ('courier',20,"bold"))
    
    playerA = turtle.textinput("Player Names", "Enter Player A's name")
    if playerA == "" or playerA == None:
        playerA = "A"
    print("Player A = " + playerA )
    text.sety(200)
    text.write("Player A = " + playerA, align = "left", font = ("courier",20, "bold"))

    
    
    playerB = turtle.textinput("Player Names", "Enter Player B's name")
    if playerB == "" or playerB == None:
        playerB = "B"
    if playerA == playerB :
         playerB += "2"
    print("Player B = " + playerB )
    text.sety(150)
    text.write("Player B = " + playerB, align = "left", font = ("courier",20, "bold"))

    

    maxScore = turtle.textinput("Max Score", "Enter the max/winning score (integer only)")
    if  maxScore[0:1] == "" or maxScore == None:
         maxScore = 3
         print("MaxScore possibly had spaces, or was not an integer - Going with the default value of 3")
    print("Max Score for this round = " + str(maxScore))
    text.sety(100)
    text.write("Score needed to win : "+ str(maxScore), align = "left", font = ('courier',20,"bold"))


    
     
    text.color("silver")
    text.goto(0,-45)
    text.write("Press H to Start", align = "center", font = ("courier",23,"bold"))
    text.color("white")

    window.listen()
    window.onkeypress( functools.partial( mainGame , playerA , playerB, int(maxScore))  , "h")

def helpScreen():
    clearscreen()

    text.goto(0,80)
    text.write("Pong!", align = "center" , font = ('Courier',40,"bold"))
    text.sety(-30)
    text.write("The rules are similar to the orignal pong game,\nthe one to score the most points wins!\nThe game was made using the Turtle Library in Python",align = "center" , font = ('Courier',15,"bold"))
    text.goto(-180, -150)
    text.color("silver")
    text.write("Keybinds -- \nLeft Paddle \n W - Go Up \n S - Go Down",align = "center" , font = ('Courier',12,"bold"))
    text.goto(200,-145)
    text.write("Right Paddle\n Arrow Key Up - Go Up\n Arrow Key Down - Go Down", align='center', font=('Courier', 12, 'bold'))
    text.goto(0,-200)
    text.color("white")
    text.write("Project By Jay Sharma", align='center', font=('Courier', 15, 'bold'))
    text.sety(-230)
    text.color("silver")
    text.write("Press H to Start The Game", align='center', font=('Courier', 15, 'bold'))
    window.onkeypress(PlayerNameTaker,"h")

##-----------------------------------------------------

#--Keybind (mainMenu)

window.listen()

window.onkeypress(PlayerNameTaker,"h")
window.onkeypress(helpScreen,"j")

##------------------------------------------------------
#--Menu Starter Screen

text.write("Pong!", align='center', font=('Courier', 40, 'bold'))
text.goto(0,-60)
text.color("silver")
text.write("Press H to Start", align = "center" , font = ('Courier',20,"bold"))
text.goto(0,-80)
text.write("Press J for the Game's Guide and Description", align = "center" , font = ('Courier',10,"bold"))
text.color("white")
text.hideturtle()

DisplayBallCollisions(displayball)
