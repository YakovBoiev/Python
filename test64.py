class Car:

    def __init__(self, color=None, name=None):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_polise = False

    def go(self):
        self.speed = 5
        print(f"{self.name} поехала")

    def stop(self):
        self.speed = 0
        print(f"{self.name} остановилась")

    def run(self, direction):
        print(f"{self.name} поехала {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.name} {self.speed} км/ч")


class TownCar(Car):

    def show_speed(self):
        infospeed = f"Текущая скорость {self.name} {self.speed} км/ч "
        if self.speed > 60:
            infospeed = infospeed + "ПРЕВЫШЕНИЕ СКОРОСТИ!!!"
        print(infospeed)


class WorkCar(Car):

    def show_speed(self):
        infospeed = f"Текущая скорость {self.name} {self.speed} км/ч "
        if self.speed > 40:
            infospeed = infospeed + "ПРЕВЫШЕНИЕ СКОРОСТИ!!!"
        print(infospeed)


class SportCar(Car):
    pass


class PoliseCar(Car):
    def __init__(self, color=None, name=None):
        super().__init__(color=color, name=name)
        self.is_polise = True


car1 = PoliseCar(color="white", name="car1")
car1.go()
car1.show_speed()
car1.run("налево")
car1.run("направо")
car1.speed = 70
car1.show_speed()
car1.stop()
car1.show_speed()
car2 = TownCar(color="red", name="car2")
car2.go()
car2.show_speed()
car1.run("налево")
car1.run("направо")
car2.speed = 70
car2.show_speed()
car2.stop()
car2.show_speed()
car3 = WorkCar(color="black", name="car3")
car3.go()
car3.show_speed()
car1.run("налево")
car1.run("направо")
car3.speed = 45
car3.show_speed()
car3.stop()
car3.show_speed()
