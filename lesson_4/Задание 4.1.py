print("\n1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.\n"
      "В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.\n"
      "Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.\n")


flag = True

last_sallary = input("сколько Вы зароботали за прошлый месяц - ")
present_sallary = input("из них премия составила - ")
type_work = input("Введите по какому граффику Вы работаете(2/2, 5/2, 1/3) - ")
period = input("За какой пероид произвести рассчёт в дня - ")
answer = 0

if type_work == "2/2":
    answer = int(last_sallary)  // 15 * int(period)
    print(f"За {period} смен, Вы заработаете - {answer} руб.")
elif type_work == "5/2":
    answer = int(last_sallary) // 22 * int(period)
    print(f"За {period} смен, Вы заработаете - {answer} руб.")
else:
    answer = int(last_sallary) // 8 * int(period)
    print(f"За {period} смен, Вы заработаете - {answer} руб.")