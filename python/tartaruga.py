import turtle

t = turtle.Turtle()


t.color("orange")

for x in range(5):
    t.forward(100)
    t.left(90)

t.right(90)
t.penup()
t.forward(200)
t.pendown()

for x in range(2):
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)

t.right(90)
t.penup()
t.forward(200)
t.pendown()

for x in range(3):
    t.forward(100)
    t.left(120)

t.right(90)
t.penup()
t.forward(200)
t.pendown()

for x in range(8):
    t.forward(100)
    t.left(45)



input()