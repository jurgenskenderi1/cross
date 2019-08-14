#hello today will see how to create a cross
#first import turtle library
from turtle import *
frame=Screen()
frame.setup(500,500)
def v_point():
    s.right(45);s.forward(20)
    s.left(90);s.backward(20)
s=Turtle()
s.left(45);s.forward(20);s.right(90);s.forward(20)
s.right(45);s.forward(50);s.left(90);s.forward(50)
v_point();s.right(45);s.backward(50);s.right(90)
s.forward(100);v_point();s.left(135);s.forward(100)
s.left(90);s.forward(50);v_point();s.left(135)
s.forward(50);s.left(90);s.forward(50);s.hideturtle()
frame.exitonclick()
