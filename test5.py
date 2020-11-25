incm = int(input("Введите выручку фирмы "))
costs = int(input("Введите издержки фирмы "))
profit = incm - costs
if profit >= 0:
    print("Прибыль", profit)
    profTab = profit / incm
    print("Рентабельность", profTab)
    numEmpl = int(input("Введите численность сотрудников фирмы "))
    profEmpl = profit / numEmpl
    print("Прибыль фирмы в расчете на одного сотрудника", profEmpl)
else:
    print("Убыток", profit)
