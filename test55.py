def numrecord():
    with open("text55.txt", "w") as f:
        print("Введите числа через пробел для записи в файл :")
        print(input(), file=f)

    with open("text55.txt", "r") as f:
        print("Cумма чисел записанных в файл :")
        print(sum(list(map(int, f.read().split()))))

numrecord()