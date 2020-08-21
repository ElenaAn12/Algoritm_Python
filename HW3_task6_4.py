# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
import timeit
import cProfile


def summa_(list_2):
    """
    Формирование списка случайных 10 чисел в диапазоне от 0 до 100
    """
    def list_(list_2):
        """
        Поиск максимальноги и минимального числа и формирование нового списка из стоящих между ними чисел.
        """
        max_ = max(list_2)
        min_ = min(list_2)
        min_id = 0
        max_id = 0
        for i in range(len(list_2)):
            if list_2[i] < min_:
                min_ = list_2[i]
                min_id = i
            if list_2[i] >= max_:
                max_ = list_2[i]
                max_id = i
        # print(min_id, max_id)
        if min_id < max_id:
            return list_2[min_id + 1:max_id]
        else:
            return list_2[max_id + 1:min_id]
        # print(max_id, min_id)

    def sum_(l):
        """
        Нахождение суммы чисел в сформированном списке чисел между максимальным и минимальным элементом.
        """
        summ = 0
        # return l
        # print(f'Числа между max и min: {l}')
        for i in range(len(l)):
            summ += l[i]
        return summ
    # print(f'Список: {list_2}')
    return sum_(list_(list_2))


# print(f'Сумма чисел равна: {summa_(random.sample(range(100), 10))}')


# ----------------- Список из 10 чисел в диапазоне [0, 100]

# print(timeit.timeit('summa_(random.sample(range(100), 10))', number=100, globals=globals()))

# 0.006215399999999996
# 0.002296200000000005
# 0.0026781000000000027
# 0.0036267999999999925
# 0.0025460999999999956


# ---------------- Слабые места

# cProfile.run('summa_(random.sample(range(100), 10))')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW3_task6_4.py:10(summa_)
#         1    0.000    0.000    0.000    0.000 HW3_task6_4.py:11(list_)
#         1    0.000    0.000    0.000    0.000 HW3_task6_4.py:32(sum_)
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
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#        10    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        10    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# ------------------ Список из 10 чисел в диапазоне [0, 5000]

# print(timeit.timeit('summa_(random.sample(range(5000), 10))', number=100, globals=globals()))

# 0.003063099999999999
# 0.004186099999999998
# 0.004227800000000004
# 0.0027722000000000024
# 0.002701000000000002

# ---------------- Слабые места

# cProfile.run('summa_(random.sample(range(5000), 10))')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW3_task6_4.py:10(summa_)
#         1    0.000    0.000    0.000    0.000 HW3_task6_4.py:11(list_)
#         1    0.000    0.000    0.000    0.000 HW3_task6_4.py:32(sum_)
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
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#        10    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# -------------------- Список из 100 чисел в диапазоне [0, 1000]

# print(timeit.timeit('summa_(random.sample(range(1000), 100))', number=100, globals=globals()))
#
# 0.0176235
# 0.0170296
# 0.0486516
# 0.016925300000000004
# 0.017657499999999993

# ---------------- Слабые места

# cProfile.run('summa_(random.sample(range(1000), 100))')

# objects} ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW3_task6_4.py:10(summa_)
#         1    0.000    0.000    0.000    0.000 HW3_task6_4.py:11(list_)
#         1    0.000    0.000    0.000    0.000 HW3_task6_4.py:32(sum_)
#         1    0.000    0.000    0.000    0.000 _collections_abc.py:302(__subclasshook__)
#         4    0.000    0.000    0.000    0.000 _collections_abc.py:392(__subclasshook__)
#       5/2    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)
#         2    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 random.py:315(sample)
#         2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
#       5/2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       108    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
