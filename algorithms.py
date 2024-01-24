import random


def insert_sort(arr):
    """!
    Функция сортировки массива 'Вставками'
    @param arr: сортируемый список
    @return Ничего не возвращает
    """
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp


def quick_sort(arr, start, end):
    """!
    Функция сортировки массива методом 'QuickSort'
    @param arr: сортируемый список
    @param start: индекс начала сортировки
    @param end: индекс конца сортировки
    @return Ничего не возвращает
    """
    if end <= start:
        return
    pivot = arr[(start + end) // 2]
    left = start
    right = end
    while left <= right:
        while arr[left] < pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        if right >= left:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    quick_sort(arr, start, right)
    quick_sort(arr, left, end)


def merge_sort(arr):
    """!
    Функция сортировки массива методом слияния
    @param arr: сортируемый список
    @return Ничего не возвращает
    """


a = [int(random.random() * 1000) for i in range(1000000)]
quick_sort(a, 0, len(a) - 1)
print(a == sorted(a))
