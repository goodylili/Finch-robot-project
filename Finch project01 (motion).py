from finch import Finch
from time import sleep, time

robot = Finch()


def speed(time_=int(input("How long would you be running the finch::"))):
    start_time = time()
    robot.wheels(1, 1)
    sleep(time_)
    print(f"The program ran for approximately {time() - start_time}")
    print(f"The distance covered is {0.381 * time_} metres in {time_}  seconds")
    print("The speed of the robot is 15 inches per second which equals 0.381 metres per second ")


speed()
