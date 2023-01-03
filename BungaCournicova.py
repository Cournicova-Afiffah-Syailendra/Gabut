import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#262626')
t.pencolor('cyan')
t.speed(100)
for n in range(5):
     for x in range(8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(2)
            t.circle(80+n*20,90)
            t.lt(90)
        t.lt(45)
s.exitonclick()