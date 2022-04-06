def my_func(first, second, therd):
    i = float(max(first,second,therd))
    l = float(min(first,second,therd))
    k = float(first + second + therd) - i - l
    all = float(k + i)
    return all

first = float(input("Введите либое число - "))
second = float(input("Введите либое число - "))
therd = float(input("Введите либое число - "))

print(f"Полученный результат - {my_func(first,second,therd)}")
