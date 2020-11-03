from finch import Finch

robot = Finch()


def anti_obs():
    zaxis = robot.acceleration()[2]

    while zaxis > -.7:
        leftie, rightie = robot.obstacle()
        if (leftie and rightie) == False:
            robot.wheels(1.0, 1.0)
            robot.led(0, 255, 0)
        elif leftie:
            robot.wheels(-0.3, 0.3)
            robot.led(255, 0, 0)
            robot.buzzer_with_delay(2, 9000)


        elif rightie:
            robot.wheels(0.3, -0.3)
            robot.led(255, 0, 0)
            robot.buzzer_with_delay(2, 9000)


anti_obs()
