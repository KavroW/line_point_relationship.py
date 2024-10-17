import turtle
d = ''
x0 = int(input("Enter point 1 x coordinate: "))
y0 = int(input("Enter point 1 y coordinate: "))
x1 = int(input("Enter point 2 x-coordinate: "))
y1 = int(input("Enter point 2 y-coordinate: "))
x2 = int(input("Enter point 3 x-coordinate: "))
y2 = int(input("Enter point 3 y-coordinate: "))

w = (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0)

if w > 0:
    d = 'p2 is on the left side of the line'
elif w == 0:
    d = 'p2 is on the same line'
else:
    d = 'p2 is on the right side of the line'

t = turtle.Turtle()
t.hideturtle()
t.home()
t.penup()
t.goto(x0,y0)
t.pendown()
t.dot(10)
t.write(f'({x0},{y0})')
t.goto(x1,y1)
t.dot(10)
t.write(f'({x1},{y1})')
t.penup()
t.goto(x2,y2)
t.pendown()
t.dot(10)
t.write(d)

input('Press any key to exit: ')

