# Курс основы программирования на Python
# Задание по программированию: Сумма цифр трехзначного числа
# 06.04.2019
#
# Дано трехзначное число. Найдите сумму его цифр.
#
# Формат ввода
#
# Вводится целое положительное число. Гарантируется,
# что оно соответствует условию задачи.
#
# Формат вывода
#
# Выведите ответ на задачу.

number = (input())
number1 = int(number[0])
number2 = int(number[1])
number3 = int(number[2])
number = number1 + number2 + number3
print(number)