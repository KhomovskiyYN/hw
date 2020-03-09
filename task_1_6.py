"""
Задание №6
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""


distance = int(input('Введите количество километров на первой пробежке:'))
top_dist = int(input('Введите количество километров. больше которого лучше отдохнуть:'))
num_of_day = 1

while distance < top_dist:
    print(f'{num_of_day}-й день:{distance:.2f}')        # Формат ":.2f"  для вывода 2 знаков после запятой
    distance = distance * 1.1
    num_of_day += 1
print(f'{num_of_day}-й день:{distance:.2f}')            #Вне цикла выводим последнее значение, с превышением
print(f'Ответ: на {num_of_day}-й день спортсмен достиг результата — не менее {top_dist} км.')