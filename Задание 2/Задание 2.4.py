call = input("Введите слова через пробел - ").split(" ")
y = 0
while y != len(call):
    if len(call[y]) <= 10:
        print(f"{y + 1}. {call[y]}")
        y += 1
    else:
        print(f"{y + 1}. {call[y] [0:10]}")
        y += 1
