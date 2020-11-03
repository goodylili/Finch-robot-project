from finch import Finch
import time

robot = Finch()


def buzzfortemp(threshold=30):
    temp = robot.temperature()

    def conversion_temp():
        temperature = robot.temperature()
        print("On value entry, you are to enter a the unit of the value you inputted")
        value_wanted = input("Enter (f) for farenheit value or any other value for the celcius::")
        if value_wanted.lower() == "f":
            print(str(((temperature * 9) / 5) + 32) + "  degrees Farenheit")
        else:
            print(str(temperature) + " degrees Celcius")

    conversion_temp()

    while True:
        if temp > threshold:
            robot.led(255, 0, 0)
            robot.buzzer_with_delay(1, 2100)
        else:
            robot.led(0, 255, 0)


buzzfortemp()
