from finch import Finch
import time
import datetime
robot = Finch()


def temperature_check():
    temperature = robot.temperature()

    print(str(((temperature * 9) / 5) + 32) + "  degrees Farenheit at the moment.\nThis program is going to update itself in the next 15 secs")

    print("This is as at " + time.ctime() + "\n\n")

    time.sleep(15)

    return temperature_check()
print(temperature_check())