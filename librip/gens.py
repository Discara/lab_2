import random

# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать
# {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        for dictionary in items:
           if dictionary.get(args[0]) != None:
            yield(dictionary[args[0]])

    else:
        for dictionary in items:
            d = {}
            for key in args:
                 if dictionary.get(key) != None:
                    d.update({key:dictionary[key]})
            yield(d)

    # Необходимо реализовать генератор


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for i in range(num_count):
        yield(random.randint(begin, end))

    # Необходимо реализовать генератор
