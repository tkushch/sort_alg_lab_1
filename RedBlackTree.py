"""!
Класс красно-черного дерева
Реализация структуры RB-дерева со всеми его свойствами
"""

# всегда листа всегда есть потомок 'NULL' узел
# корень и листья всегда черные
# у каждого красного узла оба потомка черные
# одинаковая черная высота - количество черных узлов от корня до любого 'NULL'
# каждый новый узел красный, после вставки - балансируем (fix - несколько случаев, описаны ниже)

# Крайние случаи
# 0 случай: родитель черный - балансировка не нужна
# 1 случай: родителя нет (узел – корень) => просто перекрашиваем в черный

# Если дядя красный
# 2 случай: дед не корень => перекрашиваем родителя и дядю в черный, а деда - в красный
# 3 случай: дед корень => перекрашиваем родителя и дядю в черный (корень не считается в высоте, все осталось ок)

# Если дядя черный
# 4 случай: "зиг-заг" (дед и отец не на одной линии) => левый поворот относительно отца
# 5 случай: дед и отец на одной линии => отца красим в черный, деда - в красный, правый поворот относительно деда

class Node:
    """!
    Класс красно-черного дерева
    Реализация структуры RB-дерева со всеми его свойствами
    """
    def __init__(self, key, value, color, parent, left, right):
        self.key = key
        self.value = [value]
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


class RedBlackTree:
    """!
    Класс красно-черного дерева
    Реализация структуры RB-дерева со всеми его свойствами
    """
    def __init__(self):
        self.NIL = Node(None, None, 'black', None, None, None)
        self.root = self.NIL

    def insert(self, key, value=None):
        """!
        Добавление узла в дерево
        @param key - ключ узла
        @param value - значение узла
        """
        current = self.root
        parent = None

        while current != self.NIL and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current.key == key and current != self.NIL:
            current.value.append(value)
        else:
            new_node = Node(key, value, 'red', parent, self.NIL, self.NIL)
            if parent is None:
                self.root = new_node
            elif new_node.key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node
            self._fix_insert(new_node)

    def _fix_insert(self, node):
        """!
        Балансировка дерева после вставки
        @param node: проверяемый узел
        @return: ничего не возвращает
        """

        while node.parent is not None and node.parent.color == 'red':  # случай 0
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                inverse = False
            else:
                uncle = node.parent.parent.left
                inverse = True

            if uncle.color == 'red':  # случаи 2-3
                node.parent.color = 'black'
                uncle.color = 'black'
                node.parent.parent.color = 'red'
                node = node.parent.parent
            else:  # случаи 4-5
                if node == node.parent.right and not inverse or node == node.parent.left and inverse:
                    node = node.parent
                    self._left_rotate(node, inverse)
                node.parent.color = 'black'
                node.parent.parent.color = 'red'
                self._right_rotate(node.parent.parent, inverse)
        self.root.color = 'black'  # случай 1

    def _left_rotate(self, x, inverse=False):
        if inverse:
            self._right_rotate(x)
            return
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y, inverse=False):
        if inverse:
            self._left_rotate(y)
            return
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

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
        if root == self.NIL:
            return

        if key == root.key:
            result.extend(root.value)

        if key < root.key:
            self._search_nodes_by_key(root.left, key, result)
        else:
            self._search_nodes_by_key(root.right, key, result)

    def in_order_traversal(self, root):

        result = []
        if root is not None and root != self.NIL:
            result.extend(self.in_order_traversal(root.left))
            result.append((root.key, root.value))
            result.extend(self.in_order_traversal(root.right))
        return result

    def print_binary_tree(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + f"{root.key} ({root.color})")
            if root.left is not None or root.right is not None:
                self.print_binary_tree(root.left, level + 1, "L--- ")
                self.print_binary_tree(root.right, level + 1, "R--- ")
