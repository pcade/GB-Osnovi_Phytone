print("\n3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.\n"
      "Подсказка: использовать функцию range() и генератор.\n")

print([i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0])