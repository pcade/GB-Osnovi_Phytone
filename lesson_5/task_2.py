print("\n2. Создать текстовый файл (не программно), сохранить в нем несколько строк,\n"
      "выполнить подсчет количества строк, количества слов в каждой строке.\n")
task = open('task2.txt')
print(task.read())
task = open('task2.txt')
count = 0; summ = 0
for line in task:
      count = count + 1
      size = len([i for i in line if i.isalpha()])
      print(f"строка  - №{count} колличество символов - {size} ")
      summ += size
size = len([i for i in task if i.isalpha()])
print(f"\nвсего строк - {count}, букв {summ}")
