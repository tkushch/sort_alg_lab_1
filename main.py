from schedule import Schedule
from algorithms import insert_sort

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


a = read_schedule('out.txt')
insert_sort(a)
for elem in a:
    print(elem)
