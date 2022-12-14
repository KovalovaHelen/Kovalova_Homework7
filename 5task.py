
"""
Задание 5:
Шифр Цезаря — это вид шифра подстановки, в котором каждый символ
в открытом тексте заменяется символом,
находящимся на некотором постоянном числе позиций левее
или правее него в алфавите.
Например, в шифре со сдвигом вправо на 3, А была бы заменена
на Г, Б станет Д, и так далее. Нужно реализовать шифрование с помощью Python.
Пользователь вводит строку которую хочет зашифровать
и число (сдвиг), нужно с помощью шифра Цезаря ее зашифровать и вывести на экран.
Выполнить задание нужно с помощью цикла for и строк,
для получения числового представления символа можно использовать ord,
а для преобразования числа в строку - chr..
"""

s = ""
for i in range(ord("А"), ord("Я"), +1):
    s += chr(i)

message = input("Введите строку для шифровки: ").upper()
shift = int(input("Введите число сдвига: "))
itog = ''

for i in message:
    place = s.find(i)
    new_place = place + shift
    itog += s[new_place]

print(itog)

for i in itog:
    print(ord(i), end=" ")
