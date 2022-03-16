input_seconds = int(input("Введите колличество секунд"))
seconds = input_seconds % 60
minuts_hours = input_seconds // 60
hours = minuts_hours // 60
minuts = minuts_hours % 60
print(f"ЧЧ:{hours} ММ:{minuts} СС{seconds}")