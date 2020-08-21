import timeit
import cProfile


def eratosthenes(n):
    """Решето Эратосфена"""
    x = 0
    y = 1
    z = x + y
    a = [x, y, z]
    i = 3
    while i != n:
        x = y
        y = z
        z = x + y
        a.append(z)
        i += 1
    # print(f'a: {a}')
    return a[3:]

# eratosthenes(10)


def nat_num(A):
    """Проверка числа - простое или составное"""
    A_2 = []
    N = 0
    for i in range(len(A)):
        i = A[i]
        for j in range(2, i):
            if i % j == 0:
                N = N + 1
                break
        else:
            A_2.append(i)

    # print(A_2)
    # print(f'A: {A}')


# nat_num(eratosthenes(10))

# print(timeit.timeit('nat_num(eratosthenes(10))', number=100, globals=globals()))     #0.0012676999999999966
# print(timeit.timeit('nat_num(eratosthenes(20))', number=100, globals=globals()))     #0.0206671
# print(timeit.timeit('nat_num(eratosthenes(25))', number=100, globals=globals()))     #0.39299429999999996
# print(timeit.timeit('nat_num(eratosthenes(29))', number=100, globals=globals()))     #0.4030922
# print(timeit.timeit('nat_num(eratosthenes(30))', number=100, globals=globals()))     #12.545197400000001


# Вывод: Время выполнения или O(n^2), или O(2^n)б ну или O(n!). Очень медленно.


# ---------------- Слабые места

# cProfile.run('nat_num(eratosthenes(10))')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW4_Eratosthenes.py:24(nat_num)
#         1    0.000    0.000    0.000    0.000 HW4_Eratosthenes.py:5(eratosthenes)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        11    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('nat_num(eratosthenes(20))')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW4_Eratosthenes.py:24(nat_num)
#         1    0.000    0.000    0.000    0.000 HW4_Eratosthenes.py:5(eratosthenes)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('nat_num(eratosthenes(25))')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.003    0.003    0.003    0.003 HW4_Eratosthenes.py:24(nat_num)
#         1    0.000    0.000    0.000    0.000 HW4_Eratosthenes.py:5(eratosthenes)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        30    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('nat_num(eratosthenes(29))')
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.005    0.005    0.005    0.005 HW4_Eratosthenes.py:24(nat_num)
#         1    0.000    0.000    0.000    0.000 HW4_Eratosthenes.py:5(eratosthenes)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        34    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('nat_num(eratosthenes(30))')
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.123    0.123 <string>:1(<module>)
#         1    0.123    0.123    0.123    0.123 HW4_Eratosthenes.py:24(nat_num)
#         1    0.000    0.000    0.000    0.000 HW4_Eratosthenes.py:5(eratosthenes)
#         1    0.000    0.000    0.123    0.123 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        36    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: самое слабое место - {method 'append' of 'list' objects}


