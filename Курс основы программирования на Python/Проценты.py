# Курс основы программирования на Python
# Задание по программированию: Проценты
# 27.04.2019
#
# Процентная ставка по вкладу составляет P процентов годовых, которые
# прибавляются к сумме вклада. Вклад составляет X рублей Y копеек.
# Определите размер вклада через год. При решении этой задачи нельзя
# пользоваться условными инструкциями и циклами.
#
# Формат ввода
#
# Программа получает на вход целые числа P, X, Y.
#
# Формат вывода
#
# Программа должна вывести два числа: величину вклада через год в рублях и
# копейках. Дробная часть копеек отбрасывается.

p = int(input())
x = int(input())
y = int(input())

r = (x * 100) + y
r = r + ((r * p) / 100)
rub = int(r // 100)
kop = int(r % 100)

print('{:.0f}'.format(rub), '{:.0f}'.format(kop))
