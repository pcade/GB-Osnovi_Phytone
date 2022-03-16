from typing import Any

username = input("Как я могу к Вам обращаться?:")
brothers = int(input("Сколько братьев в Вашей семье?:"))
sisters = int(input("Сколько сестёр в Вашей семье?:"))
counter: Any = brothers + sisters + 1
print(f"{username} у Ваших родителей {counter} детей!")