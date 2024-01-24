"""!
schedule.py

Класс расписания, его методы, вспомогательные функции (компараторы полей класса)

"""


def time_cmp(a, b):
    """!
    Функция сравнения двух строк содержащих время
    формата чч:мм:сс

    @param a: время 1 чч:мм:сс
    @param b: время 2 чч:мм:сс

    @return -1 если a < b, 0 если a = b, 1 если a > b
    """
    for i in 0, 1, 3, 4, 6, 7:
        if a[i] > b[i]:
            return 1
        if a[i] < b[i]:
            return -1
    return 0


def date_cmp(a, b):
    """!
    Функция сравнения двух строк содержащих даты
    формата дд.мм.гггг

    @param a: дата 1 дд.мм.гггг
    @param b: дата 2 дд.мм.гггг

    @return -1 если a < b, 0 если a = b, 1 если a > b
    """
    for i in 6, 7, 8, 9, 3, 4, 0, 1:
        if a[i] > b[i]:
            return 1
        if a[i] < b[i]:
            return -1
    return 0


class Schedule:
    """!
    Класс расписания поездов
    """

    def __init__(self, num=0, date='00.00.0000', typ='-', time='00:00:00', dur='00:00:00'):
        """!
        Конструктор

        @param num: номер поезда :int
        @param date: дата отправления дд.мм.гггг :str
        @param typ: тип поезда (скорый, пассажирский, товарный):str
        @param time: время отправления чч:мм:сс :str
        @param dur: время в пути чч:мм:сс :str
        """

        self.num = num
        self.date = date
        self.typ = typ
        self.time = time
        self.dur = dur

    def __eq__(self, other):
        """!
        Оператор сравнения ==

        Сравнение по полям:
        дата отправления, время отправления, номер поезда, время в пути (по убыванию приоритета)
        """
        if not isinstance(other, (int, Schedule)):
            raise TypeError("Операнд справа должен иметь тип Scedule")

        if (date_cmp(self.date, other.date) != 0 or
                time_cmp(self.time, other.time) != 0 or
                self.num != other.num or
                time_cmp(self.dur, other.dur) != 0):
            return False
        return True

    def __lt__(self, other):
        """!
        Оператор сравнения <

        Сравнение по полям:
        дата отправления, время отправления, номер поезда, время в пути (по убыванию приоритета)
        """
        if not isinstance(other, (int, Schedule)):
            raise TypeError("Операнд справа должен иметь тип Scedule")

        temp = date_cmp(self.date, other.date)
        if temp > 0:
            return False
        if temp < 0:
            return True

        temp = time_cmp(self.time, other.time)
        if temp > 0:
            return False
        if temp < 0:
            return True

        if self.num > other.num:
            return False
        if self.num < other.num:
            return True

        if time_cmp(self.dur, other.dur) >= 0:
            return False
        return True

    def __gt__(self, other):
        """!
        Оператор сравнения >

        Сравнение по полям:
        дата отправления, время отправления, номер поезда, время в пути (по убыванию приоритета)
        """
        if not isinstance(other, (int, Schedule)):
            raise TypeError("Операнд справа должен иметь тип Scedule")

        temp = date_cmp(self.date, other.date)
        if temp < 0:
            return False
        if temp > 0:
            return True

        temp = time_cmp(self.time, other.time)
        if temp < 0:
            return False
        if temp > 0:
            return True

        if self.num < other.num:
            return False
        if self.num > other.num:
            return True

        if time_cmp(self.dur, other.dur) <= 0:
            return False
        return True

    def __le__(self, other):
        """!
        Оператор сравнения <=

        Сравнение по полям:
        дата отправления, время отправления, номер поезда, время в пути (по убыванию приоритета)
        """
        if not isinstance(other, (int, Schedule)):
            raise TypeError("Операнд справа должен иметь тип Scedule")

        temp = date_cmp(self.date, other.date)
        if temp > 0:
            return False
        if temp < 0:
            return True

        temp = time_cmp(self.time, other.time)
        if temp > 0:
            return False
        if temp < 0:
            return True

        if self.num > other.num:
            return False
        if self.num < other.num:
            return True

        if time_cmp(self.dur, other.dur) > 0:
            return False
        return True

    def __ge__(self, other):
        """!
        Оператор сравнения >=

        Сравнение по полям:
        дата отправления, время отправления, номер поезда, время в пути (по убыванию приоритета)
        """
        if not isinstance(other, (int, Schedule)):
            raise TypeError("Операнд справа должен иметь тип Scedule ")

        temp = date_cmp(self.date, other.date)
        if temp < 0:
            return False
        if temp > 0:
            return True

        temp = time_cmp(self.time, other.time)
        if temp < 0:
            return False
        if temp > 0:
            return True

        if self.num < other.num:
            return False
        if self.num > other.num:
            return True

        if time_cmp(self.dur, other.dur) < 0:
            return False
        return True

    def __ne__(self, other):
        """!
        Оператор сравнения !=

        Сравнение по полям:
        дата отправления, время отправления, номер поезда, время в пути (по убыванию приоритета)
        """
        return not __eq__(self, other)

    def __str__(self):
        """!
        Метод преобразования в строку
        """
        return ' '.join((str(self.num), self.date, self.typ, self.time, self.dur))

