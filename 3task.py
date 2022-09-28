"""
Программа с помощью библиотеки random генерирует случайное число от 1 до 10,
задача пользователя угадать это число за 3 попытки.
В случае если пользователь указал больше загаданного числа,
то нужно вывести "Бери меньше" и наоборот.
На экране должно быть:
Попытка #1: <ввод тут>
Бери меньше
Попытка #2: <ввод тут>
Бери больше
Попытка #3: <ввод тут>
Ты угадал!
"""

from random import randint

a = randint(1, 10)
print(a)

for i in range(1, 4):
    N = int(input(f"Попытка #{i}: <ввод тут>"))
    if N > a:
        print(f"Бери меньше")
    elif N < a:
        print(f"Бери больше")
    else:
        print("Ты угадал!")
        break
else:
    print("Ты не угадал")