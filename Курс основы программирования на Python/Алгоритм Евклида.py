# Курс основы программирования на Python
# Задание по программированию: Алгоритм Евклида
# 08.05.2019
#
# Для быстрого вычисления наибольшего общего делителя двух чисел используют
# алгоритм Евклида. Он построен на следующем соотношении: НОД(a,b)=НОД(b,a % b).
#
# Реализуйте рекурсивный алгоритм Евклида в виде функции gcd(a, b).
#
# Формат ввода
#
# Вводится два целых положительных числа.
#
# Формат вывода
#
# Выведите ответ на задачу.

def gcd(a, b):
    if a < b:
        if b % a == 0:
            return a
        result = gcd(a, b % a)
    else:
        if a % b == 0:
            return b
        result = gcd(a % b, b)
    return result

a, b = int(input()), int(input())
print(gcd(a, b))
