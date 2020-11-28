scroll = list(input("Введите элементы списка через пробел ").split())
print("Введеный список")
print(scroll)
for i in range(0, len(scroll) - 1, 2):
    scroll[i], scroll[i + 1] = scroll[i + 1], scroll[i]
print("Измененный список")
print(scroll)
