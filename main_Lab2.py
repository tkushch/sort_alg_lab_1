"""!
Сравнение скоростей работы четырех классов (RedBlackTree, BinarySearchTree, HashTable, Multimap)
"""


from schedule import read_schedule
from HashTable import HashTable
# from BinarySearchTreeWithoutList import BinarySearchTreeWithoutList
from BinarySearchTree import BinarySearchTree
from RedBlackTree import RedBlackTree
from time import time
from Multimap import Multimap
import matplotlib.pyplot as plt
import numpy as np


MAX_SIZE = 150010

def time_test(collection, times, a, size_limit, collis=None):
    """!
    Функция для замера времени поиска элементов (ищем по 10 разных объектов)
    :param collection: дерево/хэш-таблица (должна отвечать интерфейсу insert и get)
    :param times: куда записать результаты замеров времени
    :param a: массив с данными для заполнения коллекции
    :param size_limit: размер коллекции
    :return: ничего не возвращает
    """
    # заполнение коллекцию
    for i in range(size_limit):
        collection.insert(a[i].date, a[i])
    # засекаем время
    start = time()
    # 100 раз ищем элемент(ы) по ключу---------------------------------------------
    for row_index in range(100):
        collection.get(a[row_index].date)
    times.append(time() - start)  # добавляем время в список в соответствии с текущим размером дерева
    if collis is not None:
        collis.append(collection.collisions_count)


sizes = [100, 1000, 5000, 10000, 20000, 50000, 70000, 100000, 120000, 150000]
arr = read_schedule('in.txt', MAX_SIZE)

"""
№1. Тестирование BSTree
"""
bst_times = []
for size in sizes:
    bst = BinarySearchTree()
    time_test(bst, bst_times, arr, size)
print(bst_times)

"""
№2. Тестирование RBTree
"""
rbt_times = []
for size in sizes:
    rbt = RedBlackTree()
    time_test(rbt, rbt_times, arr, size)
print(rbt_times)

"""
№3. Тестирование HashTable
"""
hsht_times = []
collis = []
for size in sizes:
    hsht = HashTable(size=size, load_factor=1)
    time_test(hsht, hsht_times, arr, size, collis)
print(hsht_times)
print(collis)

"""
№4. Тестирование Multimap (SortedDict)
"""
multimap_times = []
for size in sizes:
    multimap = Multimap()
    time_test(multimap, multimap_times, arr, size)
print(multimap_times)

# результаты (для каждого размера делаем get() сто раз
# [9.322166442871094e-05, 0.00011181831359863281, 0.00012612342834472656, 0.00013399124145507812, 0.00014495849609375, 0.0001671314239501953, 0.0001888275146484375, 0.0002002716064453125, 0.00018024444580078125, 0.0002040863037109375]
# [9.322166442871094e-05, 0.0001220703125, 0.00015211105346679688, 0.00015211105346679688, 0.00015878677368164062, 0.00018095970153808594, 0.00019025802612304688, 0.00020313262939453125, 0.00021195411682128906, 0.0002219676971435547]
# [0.00025391578674316406, 0.0002677440643310547, 0.00026702880859375, 0.00026702880859375, 0.0002701282501220703, 0.0002911090850830078, 0.0003058910369873047, 0.0003058910369873047, 0.0003120899200439453, 0.000335693359375]
# [37, 328, 1002, 1262, 1862, 285, 1440, 189, 566, 96] - число коллизий
# [1.1920928955078125e-05, 1.0013580322265625e-05, 1.0967254638671875e-05, 1.0967254638671875e-05, 1.3113021850585938e-05, 1.4066696166992188e-05, 1.3113021850585938e-05, 1.4066696166992188e-05, 1.4781951904296875e-05, 1.4066696166992188e-05]


plt.figure(figsize=(10, 6))
plt.plot(sizes, collis, label='Число коллизий')

plt.xlabel('Размер массива')
plt.ylabel('Число коллизий')
plt.title('Число коллизий / размер')
plt.legend()
plt.savefig('collis.png')

plt.figure(figsize=(10, 6))
plt.plot(sizes, bst_times, label='BSTree')
plt.plot(sizes, rbt_times, label='RBTree')
plt.plot(sizes, hsht_times, label='HashTable')
plt.plot(sizes, multimap_times, label='Multimap')

plt.xlabel('Размер массива')
plt.ylabel('Время работы')
plt.title('Сравнение времени работы')
plt.legend()
plt.savefig('times.png')