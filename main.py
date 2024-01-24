from schedule import Schedule
from random import randint
from algorithms import insert_sort, quick_sort, merge_sort


def read_schedule(path='in.txt'):
    """!
    Функция для чтения расписания из текстового файла (разделитель - пробел)

    @param path: путь к текстовому файлу с расписанием (разделитель - пробел), по умолчанию in.txt
    @return список с объектами класса Schedule
    """
    try:
        f = open(path, 'r')
    except FileNotFoundError:
        print('\nEXCEPTION: No such file\n')
        return

    schedule_list = []
    for line in f:
        schedule_list.append(Schedule(*line.split()))
    f.close()
    return schedule_list


def write_schedule(schedule_list, path='out.txt'):
    """!
    Функция для записи расписания в текстовый файл (разделитель - пробел) из списка с объектами класса Schedule
    @param schedule_list: список с объектами Schedule, из которого надо записать данные в файл
    @param path: путь к файлу, по умолчанию out.txt
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


a = [rand_schedule_data() for i in range(1000)]
quick_sort(a)
for elem in a:
    print(elem)
