number = int(input("Введите загаданное число - "))
value = 0

while (number):
    if (number % 10 > value):
        value = number % 10
    number //= 10

print(f"Наибольшее число {value}")