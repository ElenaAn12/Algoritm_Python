# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
import timeit
import cProfile


def summa_(size, min_, max_):
    list_ = [random.randint(min_, max_) for i in range(size)]
    # print(list_)
    min_id = 0
    max_id = 0

    for i in range(1, len(list_)):
        if list_[i] < list_[min_id]:
            min_id = i
        elif list_[i] > list_[max_id]:
            max_id = i
    if min_id > max_id:
        min_id, max_id = max_id, min_id
    # print(f'Сумма чисел: {list_[min_id + 1:max_id]} = {sum(list_[min_id + 1:max_id])}')


# summa_(random.randint(0, 10), random.randint(0, 50), random.randint(50, 100))

# ----------------- Список из 10 чисел в диапазоне [0, 100]

# print(timeit.timeit('summa_(random.randint(0, 10), random.randint(0, 50), random.randint(50, 100))',
# number=100, globals=globals()))

# 0.0018193000000000029
# 0.002053100000000002
# 0.0021649000000000043
# 0.001974499999999997
# 0.001873799999999995


# ---------------- Слабые места

# cProfile.run('summa_(random.randint(0, 10), random.randint(0, 50), random.randint(50, 100))')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW3_task6_3.py:10(summa_)
#         1    0.000    0.000    0.000    0.000 HW3_task6_3.py:11(<listcomp>)
#         7    0.000    0.000    0.000    0.000 random.py:200(randrange)
#         7    0.000    0.000    0.000    0.000 random.py:244(randint)
#         7    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         7    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         9    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# ------------------ Список из 10 чисел в диапазоне [0, 5000]

# print(timeit.timeit('summa_(random.randint(0, 10), random.randint(0, 2500), random.randint(2500, 5000))',
# number=100, globals=globals()))

# 0.002153299999999997
# 0.0029061000000000017
# 0.002726300000000001
# 0.0024747999999999992
# 0.0021650000000000003

# ---------------- Слабые места

# cProfile.run('summa_(random.randint(0, 100), random.randint(0, 1000), random.randint(1000, 2000))')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW3_task6_3.py:10(summa_)
#         1    0.000    0.000    0.000    0.000 HW3_task6_3.py:11(<listcomp>)
#        16    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        16    0.000    0.000    0.000    0.000 random.py:244(randint)
#        16    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        16    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        23    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# -------------------- Список из 100 чисел в диапазоне [0, 1000]

# print(timeit.timeit('summa_(random.randint(0, 100), random.randint(0, 500), random.randint(500, 1000))',
# number=100, globals=globals()))

# 0.013627099999999996
# 0.012163400000000005
# 0.012276099999999998
# 0.012471899999999994
# 0.011437000000000003


# ---------------- Слабые места

# cProfile.run('summa_(random.randint(0, 100), random.randint(0, 500), random.randint(500, 1000))')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW3_task6_3.py:10(summa_)
#         1    0.000    0.000    0.000    0.000 HW3_task6_3.py:11(<listcomp>)
#        89    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        89    0.000    0.000    0.000    0.000 random.py:244(randint)
#        89    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        89    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        96    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# cProfile.run('summa_(100, 500, 1000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 HW3_task6_3.py:10(summa_)
#         1    0.000    0.000    0.000    0.000 HW3_task6_3.py:11(<listcomp>)
#       100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:244(randint)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       102    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# Вывод: самое слабое место -
