from itertools import chain
from collections import defaultdict

mylist = []
Flag = True

while Flag:
    name = input("Введите наименование - ")
    price = input("Введите стоимость - ")
    numbers = input("Введите колличество - ")
    kinds = input("Введите систему измерения - ")
    if input("Желаете заполнить ещё ? Д/Н ") == "Н":
        Flag = False
    mydict = {"наименование": name, "цена": price, "количество": numbers, "ед": kinds}
    mycorteg = (mydict)
    mylist.extend([mycorteg])

superdict = {}
list_name, list_prise, list_amount, list_unit = [], [], [], []
for i in range(len(mylist)):
    list_name.append(mylist[i].get('наименование'))
    list_prise.append(mylist[i].get('цена'))
    list_amount.append(mylist[i].get('количество'))
    list_unit.append(mylist[i].get('ед'))

superdict['наименование'] = list_name
superdict['цена'] = list_prise
superdict['количество'] = list_amount
superdict['ед'] = list_unit

for k, v in superdict.items():
    print(k, v)
