
"""
Задание №5
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

revenue = int(input('Введите выручку фирмы:'))
cost = int(input('Введите издержку фирмы:'))

if revenue > cost:
    print('Фирма работает с прибылью')
    profit = revenue - cost
    print('Рентабельность:', profit / revenue)
    staff = int(input('Сколько сотрудников в Фирме?'))
    print('Прибыль фирмы на 1 человека =', profit / staff)
else:
    print('В вашей фирме убытки')