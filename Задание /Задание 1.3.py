number = int(input("Введите загаданное число - "))
unswer = (number + int(2 * str(number)) + int(3 * str(number)))
print(f"{number} + {number}{number} + {number}{number}{number} = {unswer}.")