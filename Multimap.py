"""!
   Класс наиболее похожий на std::multimap
   Использует SortedDict (реализован через сбалансированное дерево)
   """

from sortedcontainers import SortedDict


class Multimap:
    """!
    Класс наиболее похожий на std::multimap
    Использует SortedDict (реализован через сбалансированное дерево)
    """
    def __init__(self):
        self.v = SortedDict()

    def insert(self, key, value=None):
        if key in self.v:
            self.v[key].append(value)
        else:
            self.v[key] = [value]

    def get(self, key):
        return self.v[key]

    def __str__(self):
        return str(self.v)

