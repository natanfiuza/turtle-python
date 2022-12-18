import turtle
loadWindow = turtle.Screen()
turtle.speed(2)
colors = ['blue', 'green', 'yellow', 'orange','red','black','gray','purple']
for i in range(100):
    turtle.pencolor(colors[i % 6])
    turtle.circle(5*i)
    turtle.pencolor(colors[i % 8])
    turtle.circle(-5*i)
    turtle.left(i)

turtle.exitonclick()
