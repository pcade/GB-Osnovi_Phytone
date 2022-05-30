print("\n1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.\n"
      "Об окончании ввода данных свидетельствует пустая строка.\n")

task_file = open("task_file.txt", "w")
flag = True
while flag:
      task_file = open("task_file.txt", "a")
      s = input("введите текст для создаваемого файла - ")
      task_file.write(s)
      task_file.write("\n")
      if s == "":
            flag = False
task_file.close()