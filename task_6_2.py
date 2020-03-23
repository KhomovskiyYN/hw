
"""
Задание №2
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""
class Road:
    _length = 0
    _width = 0
    # weight = 0
    # thick = 0

    def mass(self, l, w, m, h):
        self._length = l
        self._width = w
        # self.weight = m
        # self.thick = h

        total = (l * w * m * h) / 1000
        print(f"Масса асфальта\n {l} м * {w} м * {m} кг * {h} см = ", int(total), "т")

result = Road()
result.mass(20,5000,25,5)