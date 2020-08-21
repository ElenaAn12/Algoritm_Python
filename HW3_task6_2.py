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
        if list_[i] <= min_:
            min_ = list_[i]
            min_id = i
        if list_[i] >= max_:
            max_ = list_[i]
            max_id = i

    if min_id < max_id:
        start_ = min_id
        stop_ = max_id
    else:
        start_ = max_id
        stop_ = min_id
    sum_ = 0
    for j in range(abs(stop_ - start_ - 1)):
        sum_ += list_[start_ + 1 + j]
    # print(f'Сумма чисел {list_[start_:stop_]} = {sum_}')


# summa_(random.sample(range(100), 10))


# ----------------- Список из 10 чисел в диапазоне [0, 100]

# print(timeit.timeit('summa_(random.sample(range(100), 10))', number=100, globals=globals()))
# 0.002120900000000002
# 0.002962400000000004
# 0.0022818999999999964
# 0.002102800000000002
# 0.003100599999999995


# --------------- Слабые места

# cProfile.run('summa_(random.sample(range(100), 10))')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW3_task6_2.py:10(summa_)
#         1    0.000    0.000    0.000    0.000 _collections_abc.py:302(__subclasshook__)
#         4    0.000    0.000    0.000    0.000 _collections_abc.py:392(__subclasshook__)
#       5/2    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)
#         2    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 random.py:315(sample)
#         2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
#       5/2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#        10    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# ------------------ Список из 10 чисел в диапазоне [0, 5000]

# print(timeit.timeit('summa_(random.sample(range(5000), 10))', number=100, globals=globals()))

# 0.002294399999999995
# 0.0028248000000000023
# 0.002773499999999998
# 0.00238
# 0.0026645


# ---------------- Слабые места

# cProfile.run('summa_(random.sample(range(5000), 10))')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW3_task6_2.py:10(summa_)
#         1    0.000    0.000    0.000    0.000 _collections_abc.py:302(__subclasshook__)
#         4    0.000    0.000    0.000    0.000 _collections_abc.py:392(__subclasshook__)
#       5/2    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)
#         2    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 random.py:315(sample)
#         2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
#       5/2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#        10    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        15    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# -------------------- Список из 100 чисел в диапазоне [0, 1000]

# print(timeit.timeit('summa_(random.sample(range(1000), 100))', number=100, globals=globals()))

# 0.0188788
# 0.016172199999999998
# 0.017554700000000006
# 0.018648199999999997
# 0.016535

# ---------------- Слабые места

# cProfile.run('summa_(random.sample(range(1000), 100))')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW3_task6_2.py:10(summa_)
#         1    0.000    0.000    0.000    0.000 _collections_abc.py:302(__subclasshook__)
#         4    0.000    0.000    0.000    0.000 _collections_abc.py:392(__subclasshook__)
#       5/2    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)
#         2    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 random.py:315(sample)
#         2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
#       5/2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       111    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# Вывод: самое слабое место - {method 'getrandbits' of '_random.Random' objects}
