
"""
Задание №1
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""


my_list = [1, 1.1, '1', 'Hello', True, (1, 2, 3), [4, 5, 6], {7, 8, 9}, complex(1,2),
           bool(1),bytes(2)]

for i in my_list:

    print(i, 'Тип элемента:', type(i))