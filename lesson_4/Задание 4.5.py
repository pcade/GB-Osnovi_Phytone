print("\nРеализовать формирование списка, используя функцию range() и возможности генератора.\n"
      "В список должны войти четные числа от 100 до 1000 (включая границы).\n"
      "Необходимо получить результат вычисления произведения всех элементов списка.\n"
      "\nПодсказка: использовать функцию reduce().\n")

for i in range(100, 1002):
      finder = int(i/2)
      if (i % 2) == 0:
            print(f"результат деление {i} на 2 равен {finder}")
