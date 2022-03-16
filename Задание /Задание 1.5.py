income = int(input("Введите сумму выручки : "))
costs = int(input("Введите издержки : "))

if income > costs:
    percent = income // costs * 100
    staff = int(input("Введите колличество работающих сотрудников : "))
    print(f"Рентабельность предприятия составляет : +{percent}  %")
    print(f"Рентабельность из рассчёта на одного сотрудника составляет : +{percent // staff} %")
elif income == costs:
    print(f"Рентабельность предприятия в данный момент : 0 %")
else:
    percent = costs // income * 100
    print(f"В данный момент Вы работаете в убыток, потери составляют : -{percent}  %")
