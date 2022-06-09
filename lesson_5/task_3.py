print("\n3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов\n"
      "(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,\n"
      "вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.\n"
      "Пример файла:\n"
      "Иванов 23543.12\n"
      "Петров 13749.32\n")
task = open('task3.txt', 'r')
count = 0; summ = 0
for line in task:
      task = open('task3.txt', 'r')
      finder = task.readlines()[count].split(" ")[1].strip()
      if finder < str(20000):
            task = open('task3.txt', 'r')
            print(f"зарплата меньше 20 000 руб. у - {task.readlines()[count]}")
      count = count + 1
      task = open('task3.txt', 'r')
      summ +=int(finder)
midle = summ/count
print(f"средняя зарплата равняется {midle}")
