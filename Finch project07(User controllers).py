from finch import Finch
from time import sleep
robot = Finch()

def foward():
    robot.wheels(0.5, 0.5)
    pass

def backward():
    pass


def left():
    pass


def right():
    pass


def arcleft():
    robot.wheels(1, 0)
    sleep(2)


def arcright():
    robot.wheels(0,1)
    sleep(2)
robot.wheels(-1,-1)
sleep(7)