from itertools import chain
from collections import defaultdict

print("\nРеализовать функцию, принимающую несколько параметров\n"
      "описывающих данные пользователя: имя, фамилия, год рождения, город проживания\n"
      "email, телефон. Функция должна принимать параметры как именованные аргументы.\n"
      "Реализовать вывод данных о пользователе одной строкой.\n")
flag = True
mylist = []
while flag:
    name = input("Введите имя - ")
    secondname = input("Введите фамилию - ")
    birthday = input("Введте дату рождения - ")
    location = input("Введите город проживания - ")
    email = input("Введите адресс электронной почты - ")
    phone = input("Введите номер мобильного телефона")
    if input("Желаете заполнить ещё ? Д/Н ") == "Н":
        flag = False
    mydict = {"имя": name, "фамилия": secondname, "день рождения": birthday, "город проживания": location,
              "почта": email, "номер телефона": phone}
    mycorteg = (mydict)
    mylist.extend([mycorteg])

i = len(mylist) - 1
while i >= 0:
    print(mylist[i])
    i -= 1
