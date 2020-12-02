def summ():
    summ = 0
    char = ""
    print("Специальный символ окончания подсчета - q")
    while char != "q" and char != "Q":
        string = list(input("Введите числа через пробeл "))
        string.append(" ")
        numb = "0"
        for i in range(len(string)):
            char = string[i]
            if char.isdigit():
                numb = numb + char
            else:
                summ = summ + int(numb)
                numb = "0"
                if char == "q" or char == "Q":
                    break
        print("общая cумма введеных чисел ", summ)

summ()