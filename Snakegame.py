#snake game #1

import turtle #screen bana k liye ya square,shapes,pictures etc create krne k liye
import time 
import random #for random no. like for food

#screen
x = turtle.Screen()
x.bgcolor("grey")
x.title("The Snake Game")
x.setup(width=500,height=500)

bodies = []
score = 0
highestscore = 0
# delay = 0.1

#head
h =turtle.Turtle()
h.shape("circle")
h.fillcolor("blue")
h.color("black")
h.penup() #turtle move kre toh draw naho
h.goto(0,0)
h.speed(4)
h.direction="stop" #initially stop hoga

#food
khana = turtle.Turtle()
khana.shape("triangle")
khana.fillcolor("black")
khana.color("brown")
khana.speed(0)
khana.penup()
khana.ht() #hide turtle
khana.goto(0,200)
khana.st() #show

#board
b = turtle.Turtle()
b.color("white")
b.fillcolor("black")
b.penup()
b.ht()
b.goto(100,230)
b.write("score: 0   & Highest score: 0 ")

def Gup():
    if h.direction != "down":
        h.direction = "up" 
def Gdown():
    if h.direction != "up":
        h.direction = "down"
def Gleft():
    if h.direction != "right":
        h.direction = "left"
def Gright():
    if h.direction != "left":
        h.direction = "right"

def Gstop():
    h.direction = "stop"

def move():
    if h.direction == "up":
        yno = h.ycor()
        h.sety(yno + 20)
    if h.direction == "down":
        yno = h.ycor()
        h.sety(yno - 20)
    if h.direction == "left":
        xno = h.xcor()
        h.setx(xno - 20)
    if h.direction == "right":
        xno = h.xcor()
        h.setx(xno + 20)        


x.listen() #to set focus on screen
x.onkey(Gdown,"Down")
x.onkey(Gup,"Up")
x.onkey(Gleft,"Left")
x.onkey(Gright,"Right")
x.onkey(Gstop,"space")

#main loop
while True :
    x.update() #screen regular update ho
    #wall collison
    if h.xcor() > 240:
        h.setx(-240)
    if h.xcor() < -240:
        h.setx(240)
    if h.ycor() > 240:
        h.sety(-240)
    if h.ycor() < -240:
        h.sety(240)
    # if h.xcor() > 240 or h.xcor() < -240 or h.ycor() > 240 or h.ycor() < -240:
    #     break

    #food collision
    if h.distance(khana) < 20:
        a1 = random.randint(-240,240)
        b1 = random.randint(-240,240)
        khana.goto(a1,b1)

        #snake body
        body = turtle.Turtle()
        body.shape("square")
        body.color("black")
        body.fillcolor("yellow")
        body.penup()
        body.speed(0)
        bodies.append(body)
        h.speed(0)

        score += 10
        # delay =- 0.001 #delay kam speed jyada

        if score > highestscore :
            highestscore = score
        b.clear()
        b.write("score: {} & Highestscore: {}".format(score,highestscore))

    #to move
    for i in range(len(bodies)-1,0,-1):
        a2 =bodies[i-1].xcor()
        b2 =bodies[i-1].ycor()
        bodies[i].goto(a2,b2)

    if len(bodies) > 0:
          a2 = h.xcor()
          b2 = h.ycor()    
          bodies[0].goto(a2,b2)

    move()
    # time.sleep(delay)
    # x.mainloop()    