def aversalary():
    with open("text53.txt", "r") as infile:
        firmsalary = {}
        print("Список сотрудников с зарплатой меньше 20 000.00: ")
        for str in infile:
            empl = str.split()
            surname = empl[0]
            salary = float(empl[1])
            firmsalary[surname] = salary
            if salary < 20000:
                print(surname)
        print(f"Средняя зарплата сотрудника организации - {sum(firmsalary.values())/len(firmsalary):.2f}")

aversalary()