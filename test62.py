class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def massofasphalt(self):
        thickness = int(input("Введите толщину покрытия "))
        mass = (self.__length * self.__width * thickness * 25) / 1000
        print(f"Масса асфальта необходимого для покрытия дороги - {mass} т")


length = int(input("Ведите длину дороги "))
width = int(input("Введите ширину дороги ")  )
a = Road(length, width)
a.massofasphalt()
