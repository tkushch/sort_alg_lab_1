"""!
schedule.py

Класс расписания, его методы, вспомогательные функции (компараторы полей класса)

"""
import datetime


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


def to_type(x):
    """!
    Функция преобразования числа в тип поезда в зависимости от его остатка на 3 (для случайной генерации данных)
    """
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


class Schedule:
    """!
    Класс расписания поездов
    """

    def __init__(self, num=0, date='00:00:0000', typ='-', time='00:00:00', dur='00:00:00'):
        """!
        Конструктор

        @param num: номер поезда :int
        @param date: дата отправления дд:мм:гггг :str
        @param typ: тип поезда (скорый, пассажирский, товарный):str
        @param time: время отправления чч:мм:сс :str
        @param dur: время в пути чч:мм:сс :str
        """
        # date in format '00:00:0000' to datetime type
        self.date = datetime.datetime.strptime(date, '%d:%m:%Y')
        # time in format '00:00:00' to datetime type
        self.time = datetime.datetime.strptime(time, '%H:%M:%S')
        # duration in format '00:00:00' to datetime type
        self.dur = datetime.datetime.strptime(dur, '%H:%M:%S')

        self.num = num
        # self.date = date
        self.typ = typ
        # self.time = time
        # self.dur = dur

    def __eq__(self, other):
        """!
        Оператор сравнения ==

        Сравнение по полям:
        дата отправления, время отправления, номер поезда, время в пути (по убыванию приоритета)
        """
        if not isinstance(other, (int, Schedule)):
            raise TypeError("Операнд справа должен иметь тип Scedule")

        return (self.date == other.date and
                self.time == other.time and
                self.num == other.num and
                self.dur == other.dur)

    def __lt__(self, other):
        """!
        Оператор сравнения <

        Сравнение по полям:
        дата отправления, время отправления, номер поезда, время в пути (по убыванию приоритета)
        """
        if not isinstance(other, (int, Schedule)):
            raise TypeError("Операнд справа должен иметь тип Scedule")

        if self.date != other.date:
            return self.date < other.date

        if self.time != other.time:
            return self.time < other.time
        if self.num != other.num:
            return self.num < other.num
        return self.dur < other.dur

    def __gt__(self, other):
        """!
        Оператор сравнения >

        Сравнение по полям:
        дата отправления, время отправления, номер поезда, время в пути (по убыванию приоритета)
        """
        return not (self < other) and not (self == other)

    def __le__(self, other):
        """!
        Оператор сравнения <=

        Сравнение по полям:
        дата отправления, время отправления, номер поезда, время в пути (по убыванию приоритета)
        """
        return self < other or self == other

    def __ge__(self, other):
        """!
        Оператор сравнения >=

        Сравнение по полям:
        дата отправления, время отправления, номер поезда, время в пути (по убыванию приоритета)
        """
        return not self < other

    def __ne__(self, other):
        """!
        Оператор сравнения !=

        Сравнение по полям:
        дата отправления, время отправления, номер поезда, время в пути (по убыванию приоритета)
        """
        return not self == other

    def __str__(self):
        """!
        Метод преобразования в строку
        """
        date_str = self.date.strftime("%d:%m:%Y")
        time_str = self.time.strftime("%H:%M:%S")
        dur_str = self.dur.strftime("%H:%M:%S")

        return ' '.join((str(self.num), date_str, self.typ, time_str, dur_str))
