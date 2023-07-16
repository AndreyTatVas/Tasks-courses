# Курс основы программирования на Python
# Задание по программированию: Количество четных элементов последовательности
# 21.04.2019
#
# Определите количество четных элементов в последовательности, завершающейся числом 0.
#
# Формат ввода
#
# Вводится последовательность целых чисел, оканчивающаяся числом 0
# (само число 0 в последовательность не входит, а служит как признак ее окончания).
#
# Формат вывода
#
# Выведите ответ на задачу.

a = int(input())
i = 0

while a != 0:
    if a % 2 == 0:
        i += 1
    a = int(input())

print(i)
