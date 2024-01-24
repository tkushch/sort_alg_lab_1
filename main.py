"""!
main.py

Файл для проведения замеров времени сортировки разных данных алгоритмами из algorithms.py
"""

import time
from schedule import Schedule
from random import randint
from algorithms import insert_sort, quick_sort, merge_sort
import matplotlib.pyplot as plt
import numpy as np


def read_schedule(path, n):
    """!
    Функция для чтения расписания из текстового файла (разделитель - пробел)
    @param n: количество строк, которое должно быть прочитано
    @param path: путь к текстовому файлу с расписанием (разделитель - пробел)
    @return список с объектами класса Schedule
    """
    try:
        f = open(path, 'r')
    except FileNotFoundError:
        print('\nEXCEPTION: No such file\n')
        return

    schedule_list = []
    for i in range(n):
        line = f.readline()
        schedule_list.append(Schedule(*line.split()))
    f.close()
    return schedule_list


def write_schedule(schedule_list, path):
    """!
    Функция для записи расписания в текстовый файл (разделитель - пробел) из списка с объектами класса Schedule
    @param schedule_list: список с объектами Schedule, из которого надо записать данные в файл
    @param path: путь к файлу
    """
    f = open(path, 'w')
    for list_elem in schedule_list:
        f.write(str(list_elem) + '\n')
    f.close()


def to_type(x):
    if x % 3 == 0:
        return 'пассажирский'
    elif x % 3 == 1:
        return 'скорый'
    else:
        return 'товарный'


def to_need_len(s, n):
    """!
    Функция, дополняющая строку до нужной длины, добавлением нулей в начало
    @param s: строка
    @param n: необходимая длина
    @return возвращает дополненную нулями строку
    """
    return '0' * (n - len(s)) + s


def rand_schedule_data():
    """!
    Функция, возвращающая объект класса Schedule со случайными данными
    """
    return Schedule(randint(1, 1000),
                    ':'.join(
                        (to_need_len(str(randint(1, 30)), 2), to_need_len(str(randint(1, 12)), 2),
                         str(randint(2000, 2023)))),
                    to_type(randint(1, 100)),
                    ':'.join((to_need_len(str(randint(0, 23)), 2), to_need_len(str(randint(0, 59)), 2),
                              str(randint(10, 59)))),
                    ':'.join((to_need_len(str(randint(0, 23)), 2), to_need_len(str(randint(0, 59)), 2),
                              str(randint(10, 59)))))


# Ниже находятся две строчки, с помощью которых был сгенерирован файл in.txt (150 тыс. строк)
# a = [rand_schedule_data() for i in range(150000)]
# write_schedule(a, 'in.txt')

sizes = [100, 1000, 5000, 10000, 20000, 50000, 70000, 100000, 120000, 150000]

# Быстрая сортировка

# quick_sort_results = []
# for size in sizes:
#     a = read_schedule('in.txt', size)
#     start_time = time.time()  # засекаем время
#     quick_sort(a)
#     quick_sort_results.append(time.time() - start_time)
#     # write_schedule(a, 'out.txt')  # ––– <в задании написано записывать отсортированный массив в файл>
# print(quick_sort_results)

# результаты:
'''[0.0009491443634033203, 0.023778915405273438, 0.08445596694946289, 0.18958592414855957, 0.39475512504577637, 
1.176802635192871, 2.93355393409729, 2.5385050773620605, 3.0803987979888916, 4.008557081222534]'''

# Сортировка слиянием

# merge_sort_results = []
# for size in sizes:
#     a = read_schedule('in.txt', size)
#     start_time = time.time()  # засекаем время
#     merge_sort(a)
#     merge_sort_results.append(time.time() - start_time)
#     # write_schedule(a, 'out.txt')  # ––– <в задании написано записывать отсортированный массив в файл>
# print(merge_sort_results)

# результаты:
'''[0.0005178451538085938, 0.008249044418334961, 0.05442500114440918, 0.12309789657592773, 0.275620698928833, 
0.7975671291351318, 1.1729211807250977, 1.7789530754089355, 2.1777520179748535, 2.803262948989868]'''

# Сортировка вставками

# insert_sort_results = []
# for size in sizes[:6]:
#     a = read_schedule('in.txt', size)
#     start_time = time.time()  # засекаем время
#     insert_sort(a)
#     insert_sort_results.append(time.time() - start_time)
#     # write_schedule(a, 'out.txt')  # ––– <в задании написано записывать отсортированный массив в файл>
# print(insert_sort_results)

# результаты:
'''[0.0019609928131103516, 0.17946696281433105, 4.519682168960571, 18.38012409210205, 78.48876190185547, 
529.2682859897614]

посчитаем теоретическое время и сравним с замерами, чтобы найти константу C в формуле времени выполнения 
t = C * (N^2 / 10^7), где N - размер списка, а 10^7 - количество операций python в секунду

получаем:
N=100 время=0.001 (по замерам 0.00196) ~ 1.96
N=1000 время=0.1 (по замерам 0.18) ~ 1.8
N=5000 время=2.5 (по замерам 4.5) ~ 1.8
N=10000 время=10 (по замерам 18) ~ 1.8
N=20000 время=40 (по замерам 78) ~ 1.95
N=50000 время=250 (по замерам 529) ~ 2.12

Получаем разницу в ~1.9  раз (причем с увеличением N коэффициент растет), тогда для оставшихся размеров (в силу 
ограниченных вычислительных возможностей и невероятной неэффективности алгоритма на данных такого размера), 
посчитаем время теоретически, используя формулу t = 2.5 * N^2 / 10^7

N=70000, t = 490 (8 минут)
N=100000, t = 1000 (17 минут)
N=120000, t = 1440 (24 минуты)
N=150000, t = 2250 (37 минут)
'''

# Построение графиков

quick = [0.0009491443634033203, 0.023778915405273438, 0.08445596694946289, 0.18958592414855957, 0.39475512504577637,
         1.176802635192871, 2.93355393409729, 2.5385050773620605, 3.0803987979888916, 4.008557081222534]
merge = [0.0005178451538085938, 0.008249044418334961, 0.05442500114440918, 0.12309789657592773, 0.275620698928833,
         0.7975671291351318, 1.1729211807250977, 1.7789530754089355, 2.1777520179748535, 2.803262948989868]
insert = [0.0019609928131103516, 0.17946696281433105, 4.519682168960571, 18.38012409210205, 78.48876190185547,
          529.2682859897614, 490, 1000, 1440, 2250]

plt.figure(figsize=(10, 6))
plt.plot(sizes, quick, label='Quick sort')
plt.plot(sizes, merge, label='Merge sort')
plt.plot(sizes, insert, label='Insert sort')
plt.xlabel('Размер массива')
plt.ylabel('Время сортировки (секунды)')
plt.title('Зависимость времени от размера массива для трех алгоритмов сортировки')
plt.legend()
plt.show()


plt.figure(figsize=(10, 6))
plt.plot(sizes, np.log(quick), label='Quick sort')
plt.plot(sizes, np.log(merge), label='Merge sort')
plt.plot(sizes, np.log(insert), label='Insert sort')
plt.xlabel('Размер массива')
plt.ylabel('Логарифм времени сортировки')
plt.title('Зависимость логарифма времени от размера массива для трех алгоритмов сортировки')
plt.legend()
plt.show()
