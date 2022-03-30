try:
    first = int(input("Введите первое число - "))
    second = int(input("Введите второе число - "))
    result = first / second
except ZeroDivisionError as error:
    error = "Уважаемый, деление на ноль мы не проходили "
    print(error)
else:
    print(f"полученный результат равен = {result}")



