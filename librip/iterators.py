import itertools


# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False

        self.ignore_case = kwargs.get("ignore_case", False)
        self.items = list(dict.fromkeys(items))
        self.index = -1

        if self.ignore_case:
            index = 1
            for first_element in self.items:
                if type(first_element) is not str:
                    break
                for second_element in self.items[index:]:
                    if type(second_element) is not str:
                        break
                    if first_element.lower() == second_element.lower():
                        self.items.remove(second_element)
                index += 1

    def __next__(self):
        # Нужно реализовать __next__
        self.index += 1
        if self.index == len(self.items):
            raise StopIteration

        return self.items[self.index]

    def __iter__(self):
        return self
