import turtle as turtle_module
import random


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
colors_list = [(244, 242, 238), (124, 181, 211), (199, 174, 15),
           (247, 226, 234),(222, 232, 240), (26, 121, 168),
           (178, 13, 44),(237, 204, 87), (239, 148, 73),
           (220, 122, 162), (232, 241, 235), (25, 144, 72),
           (216, 80, 124), (7, 172, 211), (214, 59, 26),
           (66, 21, 54), (239, 77, 44), (247, 156, 189),
           (8, 184, 151), (161, 56, 107), (10, 30, 72),
           (74, 28, 23), (128, 208, 234), (13, 48, 132),
           (167, 193, 164), (101, 116, 184), (252, 156, 151),
           (167, 24, 19), (3, 88, 57), (111, 217, 215)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101
for dot_count in range(1,number_of_dots):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50 )

    if dot_count%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen  = turtle_module.Screen()
screen.exitonclick()