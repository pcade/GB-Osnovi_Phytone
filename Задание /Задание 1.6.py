a = float(input("Введите результат пробежки первого дня : "))
b = float(input("Введите желаемый результат : "))
day_str = 1
while a < b:
    print(f"{day_str}-й день :" '{0:.2f}'.format(a))
    a = a + a * 0.1
    day_str += 1
print(f"На {day_str}-й день Вы достигнете желаемого результата.")
