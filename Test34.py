def my_func(x, y):
    elev = x ** y
    elev1 = 1
    for i in range(abs(y)):
        elev1 *= x
    return  elev, 1 / elev1


print(my_func(5, - 2))