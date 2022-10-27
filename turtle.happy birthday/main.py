import turtle
wm = turtle.Screen()
wm.bgcolor("black")
s = turtle.Turtle()
s.speed("fastest")
s.color("white")
rotate = int(188)

def circlest(t, size):
    for i in range(10):
        t.circles(size)
        size = size - 4