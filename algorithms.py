"""!
algorithms.py

Файл с функциями сортировок
"""


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


def quick_sort(arr, start=0, end=-1):
    """!
    Функция сортировки массива методом 'QuickSort'
    @param arr: сортируемый список
    @param start: индекс начала сортировки
    @param end: индекс конца сортировки
    @return Ничего не возвращает
    """
    if end == -1:
        end = len(arr) - 1
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


def merge_sort(arr, start=0, end=-1):
    """!
    Функция сортировки массива методом слияния
    @param arr: сортируемый список
    @param start: индекс начала сортировки
    @param end: индекс конца сортировки
    @return Ничего не возвращает
    """
    if end == -1:
        end = len(arr) - 1
    if end <= start:
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    """!
    Функция слияния двух частей массива в одну для MergeSort
    @param arr: сортируемый список
    @param start: индекс начала
    @param mid: индекс середины
    @param end: индекс конца
    @return Ничего не возвращает
    """
    b = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            b.append(arr[i])
            i += 1
        else:
            b.append(arr[j])
            j += 1
    if i > mid:
        while j <= end:
            b.append(arr[j])
            j += 1
    else:
        while i <= mid:
            b.append(arr[i])
            i += 1

    for i in range(start, end + 1):
        arr[i] = b[i - start]
