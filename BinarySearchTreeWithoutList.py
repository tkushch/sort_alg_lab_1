"""!
Binary Search Tree

класс Бинарного дерева поиска (ассоциативный контейнер: ключ+значение)

одинаковые ключи хранятся в разных узлах
"""


class TreeNode:
    """!
    Класс узла дерева
    узел содержит ключ, значение, ссылки на левого и правого потомка
    """

    def __init__(self, key, value):
        """!
         Конструктор класса узла дерева
        @param key: ключ
        @param value: значение
        """
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTreeWithoutList:
    """!
    Класс Бинарного дерева поиска
    содержит конструктор, метода вставки
    """

    def __init__(self):
        self.root = None

    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)

    def _insert(self, root, key, value):
        if root is None:
            return TreeNode(key, value)

        if key < root.key:
            root.left = self._insert(root.left, key, value)
        else:
            root.right = self._insert(root.right, key, value)

        return root

    def in_order_traversal(self, root):
        result = []
        if root:
            result.extend(self.in_order_traversal(root.left))
            result.append((root.key, root.value))
            result.extend(self.in_order_traversal(root.right))
        return result

    def get(self, key):
        """!
        Метод получения списка значений по ключу
        @param key: ключ
        """
        result = []
        self._search_nodes_by_key(self.root, key, result)
        return result

    def _search_nodes_by_key(self, root, key, result):
        """!
        Приватный рекурсивный метод поиска значений по ключу
        @param root: корень дерева
        @param key: ключ для поиска
        @param result: список результатов
        @return: ничего не возвращает
        """
        if root is None:
            return

        if key == root.key:
            result.append(root.value)

        if key < root.key:
            self._search_nodes_by_key(root.left, key, result)
        else:
            self._search_nodes_by_key(root.right, key, result)

    def print_binary_tree(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + f"{root.key}")
            if root.left is not None or root.right is not None:
                self.print_binary_tree(root.left, level + 1, "L--- ")
                self.print_binary_tree(root.right, level + 1, "R--- ")
