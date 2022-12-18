import turtle
t = turtle.Turtle(shape='turtle')
t.screen.bgcolor('black')
t.pensize(2)
t.color('green')
t.left(90)
# t.backward(100)
t.speed(100)
t.shape('turtle')


def tree(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.color('orange')
        t.circle(2)
        t.color('brown')
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)


def tree_f1(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.color('white')
        t.circle(2)
        t.color('red')
        t.left(30)
        tree_f1(3*i/4)
        t.right(60)
        tree_f1(3*i/4)
        t.left(30)
        t.backward(i)


def tree_f2(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.color('yellow')
        t.circle(2)
        t.color('blue')
        t.left(30)
        tree_f2(3*i/4)
        t.right(60)
        tree_f2(3*i/4)
        t.left(30)
        t.backward(i)


def tree_f3(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.color('gray')
        t.circle(2)
        t.color('green')
        t.left(30)
        tree_f3(3*i/4)
        t.right(60)
        tree_f3(3*i/4)
        t.left(30)
        t.backward(i)

tree(100)
for i in range(5):
    t.left(230)
    tree(100)


for i in range(6):
    t.right(150)
    tree(70)

for i in range(6):
    t.right(70)
    tree_f1(90)

for i in range(8):
    t.right(50)
    tree_f2(60)

for i in range(9):
    t.right(40)
    tree_f3(30)

turtle.done()
