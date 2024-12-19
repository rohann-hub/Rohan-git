import turtle
import time  

def draw_heart_shape(t, size, color):
    t.begin_fill()
    t.color(color)
    t.left(140)
    t.forward(size)
    t.circle(-size // 2, 200)
    t.left(120)
    t.circle(-size // 2, 200)
    t.forward(size)
    t.end_fill()
    t.setheading(0)

def draw_heart():
    screen = turtle.Screen()
    screen.bgcolor('lightpink')
    
    t = turtle.Turtle()
    t.speed(2)  
    t.width(3)

    sizes = [250, 200, 150, 100, 50]
    colors = ['#E57582', '#793A2E', '#008788', '#47381F', '#E793A2']

    
    for size, color in zip(sizes, colors):
        t.penup()
        t.goto(0, -size // 2)
        t.pendown()
        draw_heart_shape(t, size, color)
        time.sleep(0.1)  
    t.hideturtle()
    screen.mainloop()

