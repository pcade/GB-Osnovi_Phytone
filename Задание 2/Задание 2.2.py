Mylist = list(map(int, input("введите числа через пробел - ").split(" ")))
print(f"{Mylist}  введенные данные")
s = 1; i = 0
if len(Mylist) % 2 == 0:
    while  i < len(Mylist):
        Mylist[i], Mylist[s] = Mylist[s], Mylist[i]
        i += 2; s += 2
    print(f"{Mylist}  полученный результат")
else:
    while i < len(Mylist) - 1:
        Mylist[i], Mylist[s] = Mylist[s], Mylist[i]
        i += 2; s += 2
    print(f"{Mylist}  полученный результат")
