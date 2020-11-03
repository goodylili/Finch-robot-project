from finch import Finch
from random import randint
robot = Finch()

def colourful():
    print("To exit code, just press a number")

    while True:
        prompter = input("Enter:")
        if prompter.isdigit():
            robot.close()
        a = randint(0, 255)
        b = randint(0, 255)
        robot.led(a, b, (255 - (a + b)))
        robot.led(255,255,255)



colourful()