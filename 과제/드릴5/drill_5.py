import turtle

def turtle_upmove():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_rightmove():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def turtle_leftmove():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def turtle_downmove():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def escape():
    turtle.reset()
    
turtle.shape("turtle")
turtle.onkey(turtle_upmove,'w')
turtle.onkey(turtle_rightmove,'d')
turtle.onkey(turtle_leftmove,'a')
turtle.onkey(turtle_downmove,'s')
turtle.onkey(escape,'e')
turtle.listen()
