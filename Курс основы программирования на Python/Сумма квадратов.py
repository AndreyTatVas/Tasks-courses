# Курс основы программирования на Python
# Задание по программированию: Сумма квадратов
# 21.04.2019
#
# По данному натуральному n вычислите сумму 1²+2²+3²+...+n².
#
# Формат ввода
#
# Вводится натуральное число.
#
# Формат вывода
#
# Выведите ответ на задачу.

n = int(input())
i = 1
sum = 0
while i <= n:
    sum += i*i
    i += 1
print(sum)
