timeSec = int(input("Введите время в секундах "))
hour = timeSec // 3600
min = (timeSec - hour * 3600) // 60
sec = timeSec - hour * 3600 - min * 60
print(f'{hour:02}:{min:02}:{sec:02}')
