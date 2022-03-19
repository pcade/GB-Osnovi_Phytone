from functools import reduce

call = int(input("Введите любое целое число - "))
mylist = [7, 5, 3, 3, 2]
print(mylist)
if call > reduce(max, mylist):
    mylist.insert(0, call)
    print(mylist)
elif call < reduce(min, mylist):
    mylist.append(call)
    print(mylist)
else:
    finder = mylist.index(call)
    mylist.insert(finder, call)
    print(mylist)



