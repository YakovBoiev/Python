from sys import argv

def salary(productv, salaryhour, prize):
    salary = float(productv) * float(salaryhour) + float(prize)
    return salary

print(f"Заработная плата сотрудника {salary(argv[1], argv[2], argv[3]):.2f} рублей")
