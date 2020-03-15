
"""
Задание №7
Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fibo_gen().
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from math import factorial

def fibo_gen (num):
    for i in range(1, num):  #нет смысла брать факториал числа 0, пожтому начинаю с 1
        yield factorial(i)   # yield возвращает генератор вместо значения. НЕ RETURN


for idx, el in enumerate(fibo_gen(16), 1):
    print(f'{idx}! = {el}')