def int_func(word):
    return word.capitalize()


string = input("Введите строку \n").split()
stringnew = []
for word in string:
    stringnew.append(int_func(word))
str = " ".join(stringnew)
print("Изменненая строка")
print(f"{str}")
