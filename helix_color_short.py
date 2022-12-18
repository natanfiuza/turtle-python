import turtle
loadWindow = turtle.Screen()
turtle.speed(2)
colors = ['blue', 'green', 'brown', 'orange',
          'red', 'black', 'gray', 'purple']
for i in range(100):
    turtle.pencolor(colors[i % 6])
    turtle.circle(2*i)
    turtle.pencolor(colors[i % 8])
    turtle.circle(-2*i)
    turtle.left(i)

turtle.exitonclick()
