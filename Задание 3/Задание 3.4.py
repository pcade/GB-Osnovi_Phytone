def my_func(X, Y):
    finder = X
    str = 1
    result = 0
    while str < Y:
        X = X * finder
        str += 1
    result = 1 / X
    return result

print("Данная программа принимает целое число X и возводит в отрицательную степень Y")
X = int(input("Введите целое число X "))
Y = int(input("Введите степенное число Y "))

print(my_func(X,Y))