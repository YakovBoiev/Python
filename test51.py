def record():
    with open("text51.txt", "w") as outf:
        print("Введите строки для записи в файл (для окончания - пустая строка)")
        str = None
        while str != "":
            str = input()
            print(str, file=outf)

record()