from time import sleep
import sys


class TraficLight:

    def __init__(self):
        self.__color = None

    def running(self):
        color = [("Красный", 7), ("Желтый", 2), ("Зеленый", 5)]
        for col in color:
            self.__color = col[0]
            print(self.__color)
            sleep(col[1])


a = TraficLight()
for _ in range(3):
    a.running()


