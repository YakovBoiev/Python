year_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
year_dict = dict()
for i in range(len(year_list)):
    year_dict[i + 1] = year_list[i]
while True:
    month = int(input("Введите номер месяца: "))
    if 1 <= month <= 12:
        break
print("Время года", year_list[month - 1])
print("Время года", year_dict.get(month))
