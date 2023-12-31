# Курс основы программирования на Python
# Задание по программированию: Минимум 4 чисел
# 08.05.2019
#
# Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел,
# которая не содержит инструкции if, а использует стандартную функцию min
# от двух чисел. Считайте четыре целых числа и выведите их минимум.
#
# Формат ввода
#
# Вводятся четыре целых числа.
#
# Формат вывода
#
# Выведите ответ на задачу.

def min4(a, b, c, d):
    """Выводятся минимум из 4 чисел"""

    return min((min(a, b), min(c, d)))

a, b, c, d = int(input()), int(input()), int(input()), int(input())

print(min4(a, b, c, d))
