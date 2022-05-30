def my_func(first, second, therd):
    i = float(max(first,second,therd))
    l = float(min(first,second,therd))
    k = float(first + second + therd) - i - l
    all = float(k + i)
    return all
print("\nРеализовать функцию my_func()\nкоторая принимает три"
      " позиционных аргумента, и возвращает сумму наибольших двух аргументов.\n")
first = float(input("Введите любое число - "))
second = float(input("Введите любое число - "))
therd = float(input("Введите любое число - "))

print(f"Полученный результат - {my_func(first,second,therd)}")
