#11 Otc 2023



import turtle

turtle.screensize(1000,1000,"white")
turtle.setup(width=0.6,height=0.6)


turtle.pensize(1)
turtle.pencolor('black')
turtle.speed(10)

turtle.hideturtle()


turtle.fillcolor('red')
turtle.begin_fill()

turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)

turtle.end_fill()


turtle.penup()
turtle.sety(20)


turtle.fillcolor('red')
turtle.begin_fill()

turtle.left(40)
turtle.forward(100)
turtle.circle(50,210)
turtle.right(135)
turtle.circle(50,210)
turtle.forward(100)

turtle.end_fill()


turtle.mainloop()