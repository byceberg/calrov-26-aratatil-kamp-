import turtle as t
import time
import logging


def draw_square(_square, x, y, color, kenar):
    _square.hideturtle()
    _square.penup()
    _square.setpos(x-kenar/2, y-kenar/2)
    _square.pendown()
    _square.pencolor(color)
    _square.fillcolor(color)
    _square.begin_fill()
    _square.setx(square.xcor() + kenar)
    _square.sety(square.ycor() + kenar)
    _square.setx(square.xcor() - kenar)
    _square.sety(square.ycor() - kenar)
    _square.end_fill()
    logging.info("The square was drawn!")


def draw_target_square(_square, x, y, color, kenar):
    _square.hideturtle()
    _square.penup()
    _square.setpos(x - kenar / 2, y - kenar / 2)
    _square.pendown()
    _square.pencolor(color)
    _square.fillcolor(color)
    _square.begin_fill()
    _square.setx(square.xcor() + kenar)
    _square.sety(square.ycor() + kenar)
    _square.setx(square.xcor() - kenar)
    _square.sety(square.ycor() - kenar)
    _square.setpos(x, y)
    _square.end_fill()
    logging.info("The target square was drawn!")


def draw_circle(_circle, x, y, color, _radius):
    _circle.hideturtle()
    _circle.penup()
    _circle.setpos(x, y - _radius)
    _circle.pendown()
    _circle.color(color)
    _circle.begin_fill()
    _circle.circle(_radius)
    _circle.end_fill()
    logging.info("The circle was drawn!")
    return _radius


def start_position(vehicle, color):
    vehicle.hideturtle()
    vehicle.color(color)
    vehicle.penup()
    vehicle.setpos(-250, 225)
    vehicle.showturtle()
    vehicle.pendown()
    logging.info("The vehicle went to the starting point!")


def algorithm_movement(vehicle, _forward=0):
    vehicle.showturtle()
    vehicle.seth(270)
    time.sleep(1)
    vehicle.sety(-200)
    logging.info("The vehicle went to the algorithm start point!")
    time.sleep(1)
    heading = 90
    logging.info("The search algorithm has started!")

    while True:
        if vehicle.distance(square) < 5:
            time.sleep(3)
            logging.info("Clue point found!")
            return True
        vehicle.fd(_forward)
        vehicle.seth(heading)
        heading += 10
        _forward += 0.025


def draw_triangle(vehicle):
    circle_position = return_coordinate()
    vehicle.seth(45)
    vehicle.setpos(circle_position+(0, radius))
    logging.info("The vehicle went to the center of the circle!")
    vehicle.seth(240)
    vehicle.color("black")
    vehicle.begin_fill()
    logging.info("The triangle is being drawn.")
    vehicle.fd(60)
    for i in range(2):
        vehicle.left(120)
        vehicle.fd(60)
    logging.info("The triangle was drawn!")
    vehicle.end_fill()
    time.sleep(1)
    vehicle.color("red")
    logging.info("The vehicle is returning to the starting point.")
    vehicle.seth(165)
    vehicle.setpos(-250, 225)
    logging.info("The vehicle returned to the starting point!")


def return_coordinate():
    if value:
        circle_position = circle.pos()
        logging.info("The coordinates of the circle were found!")
        return circle_position
    else:
        logging.info("The coordinates of the circle could not be found!")
        pass


logging.basicConfig(level=logging.INFO)
rov = t.Turtle()
rov.hideturtle()
square = t.Turtle()
square.hideturtle()
circle = t.Turtle()
circle.hideturtle()
logging.info("The screen has been created.")
t.Screen().screensize(600, 500, "lightblue")
t.Screen().title("Ocean Navigation")
draw_square(square, 0, -175, "yellow", 50)
draw_target_square(square, 0, -175, "black", 2.5)
radius = draw_circle(circle, 200, 175, "red", 20)
time.sleep(2)
start_position(rov, "red")
value = algorithm_movement(rov, 0)
draw_triangle(rov)
t.Screen().mainloop()
