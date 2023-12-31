# Курс основы программирования на Python
# Задание по программированию: Угадай число
# 18.05.2019
#
# Август и Беатриса играют в игру. Август загадал
# натуральное число от 1 до n. Беатриса пытается
# угадать это число, для этого она называет некоторые
# множества натуральных чисел. Август отвечает Беатрисе
#
# YES, если среди названных ею чисел есть задуманное или
# NO в противном случае. После нескольких заданных вопросов
# Беатриса запуталась в том, какие вопросы она задавала и
# какие ответы получила и просит вас помочь ей определить,
# какие числа мог задумать Август.
#
# Формат ввода
#
# Первая строка входных данных содержит число n — наибольшее
# число, которое мог загадать Август. Далее идут строки,
# содержащие вопросы Беатрисы. Каждая строка представляет
# собой набор чисел, разделенных пробелами. После каждой строки
# с вопросом идет ответ Августа: YES или NO. Наконец, последняя
# строка входных данных содержит одно слово HELP.
#
# Формат вывода
#
# Вы должны вывести (через пробел, в порядке возрастания) все
# числа, которые мог задумать Август.
# inFile - Файл с исходными данными
# onFile - Файл с конечнымии данными
# inFileStr - строки из исходного файла
# ansSetNO - Список чисел, которые точно не загаданы
# ansSetYES - Список чисел, которые возможны
# ansSet - Список чисел, которые пока неопределены
#
inFile = open('input.txt', 'r', encoding='utf8')
onFile = open('output.txt', 'w', encoding='utf8')
maxNum = int(inFile.readline())
ansSet = set()
ansSetNO = set()
ansSetYES = set(range(1, maxNum + 1))
for inFileStr in inFile:
    if inFileStr == 'YES\n':
        ansSetYES &= ansSet
    elif inFileStr == 'NO\n':
        ansSetNO |= ansSet
    elif inFileStr == 'HELP\n':
        print(*sorted(ansSetYES - ansSetNO), file=onFile)
    else:
        ansSet = set(map(int, inFileStr.split()))

inFile.close()
onFile.close()
