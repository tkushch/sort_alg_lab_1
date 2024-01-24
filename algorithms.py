def insert_sort(arr):
    """!
    Функция сортировки массива 'Вставками'
    @return Ничего не возвращает
    """
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp


def quick_sort(arr):
    """!
    Функция сортировки массива методом 'QuickSort'
    @return Ничего не возвращает
    """

