# Курс основы программирования на Python
# Задание по программированию: Количество слов
# 27.04.2019
#
# Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.
#
# Формат ввода
#
# Вводится строка.
#
# Формат вывода
#
# Выведите ответ на задачу.

a = str(input())
i = a.count(' ') + 1
print(i)
