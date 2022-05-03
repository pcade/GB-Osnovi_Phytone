print("\nРеализовать два небольших скрипта:\n"
      "\nа) итератор, генерирующий целые числа, начиная с указанного,\n"
      "б) итератор, повторяющий элементы некоторого списка, определенного заранее.\n"
      "\nПодсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,\n"
      "что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.\n")

import itertools

first_point = int(input("Введите начальное целое число - "))
second_point = int(input("Введите конечное целое число - "))

for x in itertools.count(first_point):
      if x < second_point + 1:
            print(x)
      else:
            break

my_list = []
finish_list = []

for i in range(first_point, second_point + 1):
      my_list.append(i)
finish_list = itertools.cycle(my_list)
print(finish_list)