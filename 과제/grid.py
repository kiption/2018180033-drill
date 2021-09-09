Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> 
>>> a_count=6
>>> a=-300
>>> b=200
>>> turtle.penup()
>>> turtle.goto(a,b)
>>> turtle.pendown()
>>> while(a_count>0):
	turtle.forward(500)
	b=b-100
	turtle.penup()
	turtle.goto(a,b)
	turtle.pendown()
	a_count=a_count-1

>>> turtle.penup()
>>> b=200
>>> b_count=6
>>> turtle.goto(a,b)
>>> turtle.right(90)
>>> turtle.pendown()
>>> while(b_count>0):
	turtle.forward(500)
	a=a+100
	turtle.penup()
	turtle.goto(a,b)
	turtle.pendown()
	b_count=b_count-1

>>> turtle.exitonclick()
>>> 