
"""
Задание №2
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

my_time = input('Введите количество секунд: ') #ввод даты в секундах


hours = int(my_time)//(60*60)   # в переменную помещаются только часы
minutes = (int(my_time)%(60*60))//60    # в переменную помещаются только минуты
seconds = (int(my_time)%(60*60))%60     # в переменную помещаются только секунды


print('Намного лучше выглядит в формате чч:мм:сс -',
f'{hours:>02}:{minutes:>02}:{seconds:>02}')