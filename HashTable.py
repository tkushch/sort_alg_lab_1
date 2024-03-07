"""!
 Класс хэш-таблицы
 Для разрешения коллизий применяется метод цепочек (списки)
 """

class HashTable:
    """!
    Класс хэш-таблицы
    Для разрешения коллизий применяется метод цепочек (списки)
    """
    def __init__(self, size=100, load_factor=0.7):
        """!
        Инициализация хеш-таблицы.

        @param size: Размер массива (бакетов) хеш-таблицы.
        @param load_factor: Пороговое значение загрузки для реаллокации.
        """
        self.size = size
        self.load_factor = load_factor
        self.table = [None] * size
        self.elements_count = 0
        self.collisions_count = 0

    def _hash_function(self, key, size=None):
        """!
        Вычисление хеша полиномиальным методом.

        @param key: Ключ для вычисления хеша.
        @param size: Размер массива (бакетов) хеш-таблицы (используется для реаллокации).
        @return: Значение хеша.
        """
        size = size or self.size
        hash_value = 0
        prime = 31  # Выбор простого числа P (31)

        for char in str(key):
            hash_value = (hash_value * prime + ord(char)) % size

        return hash_value

    def insert(self, key, value):
        """!
        Вставка элемента в хеш-таблицу.

        @param key: Ключ элемента.
        @param value: Значение элемента.
        """
        index = self._hash_function(key)

        if self.table[index] is None:
            # Создаем новый список для цепочек, если ячейка пуста
            self.table[index] = [(key, [value])]
        else:
            # Добавляем элемент к существующей цепочке
            added = False
            for item in self.table[index]:
                if item[0] == key:
                    item[1].append(value)
                    added = True
                    break
            if not added:
                self.collisions_count += 1
                self.table[index].append((key, [value]))
        self.elements_count += 1

        # Проверяем загрузку и реаллоцируем массив при необходимости
        if (self.elements_count / self.size) > self.load_factor:
            self._reallocate()

    def _reallocate(self):
        """!
        Реаллокация массива при достижении порогового значения загрузки."""
        new_size = self.size * 4  # Увеличение размера массива

        new_table = [None] * new_size

        # Перехеширование элементов в новый массив
        for chain in self.table:
            if chain is not None:
                for key, value in chain:
                    new_index = self._hash_function(key, size=new_size)
                    if new_table[new_index] is None:
                        new_table[new_index] = [(key, value)]
                    else:
                        # new_table[new_index].append((key, value))
                        added = False
                        for item in self.table[new_index]:
                            if item[0] == key:
                                item[1].append(value)
                                added = True
                                break
                        if not added:
                            self.collisions_count += 1
                            self.table[new_index].append((key, [value]))

        self.table = new_table
        self.size = new_size

    def get(self, key):
        """!
        Получение значения по ключу из хеш-таблицы.

        @param key: Ключ элемента.
        @return: Значение элемента или None, если ключ отсутствует.
        """
        index = self._hash_function(key)
        res = []
        if self.table[index] is not None:
            # Ищем элемент в цепочке
            for stored_key, stored_value in self.table[index]:
                if stored_key == key:
                    res.extend(stored_value)
        return res

#
# hash_table = HashTable(size=1)
# # 2004-01-09 00:00:00 2010-02-10 00:00:00
# #
# hash_table.insert("name", "John")
# hash_table.insert("age", 25)
# hash_table.insert("name", "Alice")  # Добавление элемента с одинаковым ключом
# hash_table.insert("name", "Alice1")
# hash_table.insert("name", "Alice")
# print(hash_table.get("name"))  # Вывод: ['John', 'Alice'] (оба элемента с одинаковым ключом сохранены)
# print(hash_table.get("age"))   # Вывод: [25]
# print(hash_table.get("city"))  # Вывод: [] (ключ отсутствует)
# print(hash_table.table)