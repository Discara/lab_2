#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data = ['a', 'A', 'b', 'B']
data2 = gen_random(1, 3, 10)

print(*list(Unique(data, ignore_case=True)))
print(*list(Unique(data)))

# Реализация задания 2