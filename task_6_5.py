
"""
Задание №5
 Реализовать класс Stationery (канцелярская принадлежность).
 Определить в нем атрибут title (название) и метод draw (отрисовка).
 Метод выводит сообщение “Запуск отрисовки.”
 Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
 В каждом из классов реализовать переопределение метода draw.
 Для каждого из классов методы должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить,
 что выведет описанный метод для каждого экземпляра. методы экземпляров).
"""


class Stationery:
    title = 'Name'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


ex_one = Stationery()
print(ex_one.title)
ex_one.draw()

ex_two = Pen()
ex_two.draw()

ex_three = Pencil()
ex_three.draw()

ex_four = Handle()
ex_four.draw()
