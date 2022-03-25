
mylist = []
Flag = True
counter = 1

while Flag:
    name = input("Введите наименование - ")
    price = input("Введите стоимость - ")
    numbers = input("Введите колличество - ")
    kinds = input("Введите систему измерения - ")
    if input("Желаете заполнить ещё ? Д/Н ") == "Н":
        Flag = False
    mydict = {"наименование": name, "цена": price, "колличество": numbers, "ед": kinds}
    mycorteg = (counter, mydict)
    mylist.extend([mycorteg])
    counter += 1
    print(mylist)
dict1 = mylist[0][1]
dict2 = (mylist[1][1])
dict1.update(dict2)
print(dict1)
print(dict2)






""""
i = len(mylist)
print(numbers_of_elements)
dict1 = (mylist[0][1])
dict2 = (mylist[1][1])
dict1.update(dict2)
print(dict1)
"""


"""
if input("Вы хотите заполнить стуктуру? Да/Нет - ") == 'Да':
    name = input("Введите наименование - ")
    price = input("Введите стоимость - ")
    numbers = input("Введите колличество - ")
    kinds = input("Введите систему измерения - ")
mylist = [("наименование", name), ("цена" , price), ("колличество" , numbers), ("ед" ,kinds)]
print(mylist)
"""