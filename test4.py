n = int(input("Введите число "))
maxNum = n % 10
while n // 10 != 0:
    n = n // 10
    num = n % 10
    if num > maxNum:
        maxNum = num
print(maxNum)
