# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
import timeit
import cProfile


def summa_(list_):
    # print(list_)
    min_ = list_[0]
    max_ = list_[0]
    min_id = 0
    max_id = 0

    for i in range(len(list_) - 1):
        list_2 = []
        summa = 0
        if list_[i] <= min_:
            min_ = list_[i]
            min_id = i
        if list_[i] >= max_:
            max_ = list_[i]
            max_id = i

        if min_id < max_id:
            list_2.append(list_[min_id + 1:max_id])
            for j in list_2[0]:
                summa += j

        elif min_id > max_id:
            list_2.append(list_[max_id + 1:min_id])
            for j in list_2[0]:
                summa += j

    list_[min_id] = max_
    list_[max_id] = min_
    # print(f'Сумма чисел {list_2[0]} = {summa}')


# ----------------- Список из 10 чисел в диапазоне [0, 100]

# print(timeit.timeit('summa_(random.sample(range(100), 10))', number=100, globals=globals()))

# 0.004389900000000002
# 0.0034008999999999984
# 0.004240900000000006
# 0.003361799999999998
# 0.0034343000000000012

# ---------------- Слабые места

# cProfile.run('summa_(random.sample(range(100), 10))')
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW3_task6_1.py:10(summa_)
#         1    0.000    0.000    0.000    0.000 _collections_abc.py:302(__subclasshook__)
#         4    0.000    0.000    0.000    0.000 _collections_abc.py:392(__subclasshook__)
#       5/2    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)
#         2    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 random.py:315(sample)
#         2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
#       5/2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#        10    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
#         8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        16    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# ------------------ Список из 10 чисел в диапазоне [0, 5000]

# print(timeit.timeit('summa_(random.sample(range(5000), 10))', number=100, globals=globals()))

# 0.0029910000000000006
# 0.0038257000000000013
# 0.004410299999999999
# 0.005033999999999997
# 0.003513499999999996

# ---------------- Слабые места

# cProfile.run('summa_(random.sample(range(5000), 10))')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW3_task6_1.py:10(summa_)
#         1    0.000    0.000    0.000    0.000 _collections_abc.py:302(__subclasshook__)
#         4    0.000    0.000    0.000    0.000 _collections_abc.py:392(__subclasshook__)
#       5/2    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)
#         2    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 random.py:315(sample)
#         2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
#       5/2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#        10    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
#         8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# -------------------- Список из 100 чисел в диапазоне [0, 1000]

# print(timeit.timeit('summa_(random.sample(range(1000), 100))', number=100, globals=globals()))

# 0.034127899999999996
# 0.0396275
# 0.036365299999999996
# 0.0347885
# 0.036527500000000004

# ---------------- Слабые места

# cProfile.run('summa_(random.sample(range(1000), 100))')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW3_task6_1.py:10(summa_)
#         1    0.000    0.000    0.000    0.000 _collections_abc.py:302(__subclasshook__)
#         4    0.000    0.000    0.000    0.000 _collections_abc.py:392(__subclasshook__)
#       5/2    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)
#         2    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 random.py:315(sample)
#         2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
#       5/2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#        98    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       112    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# Вывод: слабое место - {method 'append' of 'list' objects}, {method 'getrandbits' of '_random.Random' objects}
