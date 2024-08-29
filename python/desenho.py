import turtle as t
import random

t.width(50)
x = False

t.speed(0.1)
while x == False:
    ale = random.randint(0, 180)
    t.forward(ale)
    t.left(ale)

    cor = random.randint(1,3)
    if cor == 1:
        t.color("yellow")
    elif cor == 2:
        t.color("pink")
    else:
        t.color("black")
 
