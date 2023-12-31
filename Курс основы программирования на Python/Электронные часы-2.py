# Курс основы программирования на Python
# Задание по программированию: Электронные часы-2
# 08.04.2019
#
# Электронные часы показывают время в формате h:mm:ss, то есть
# сначала записывается количество часов (число от 0 до 23), потом
# обязательно двузначное количество минут, затем обязательно двузначное
# количество секунд. Количество минут и секунд при необходимости дополняются
# до двузначного числа нулями.
#
# С начала суток прошло N секунд. Выведите, что покажут часы.
#
# Формат ввода
#
# Вводится число N — целое, неотрицательное.
#
# Формат вывода
#
# Выведите показания часов, соблюдая формат.
#
# Примечания
#
# Вывести числа можно поциферно.

a = int(input())
b = (a // 3600) % 24
b1 = ((a - (b * 3600)) // 600) % 6
b2 = ((a - (b * 3600) - (b1 * 600)) // 60) % 10
m1 = ((a - (b * 3600) - (b1 * 600) - (b2 * 60)) // 10) % 6
m2 = (a - (b * 3600) - (b1 * 600) - (b2 * 60) - (m1 * 10)) % 10
print(b, ':', b1, b2, ':', m1, m2, sep='')
