# Курс основы программирования на Python
# Задание по программированию: Создание архива
# 12.05.2019
#
# Системный администратор вспомнил, что давно не делал архива
# пользовательских файлов. Однако, объем диска, куда он может
# поместить архив, может быть меньше чем суммарный объем
# архивируемых файлов. Известно, какой объем занимают
# файлы каждого пользователя.
#
# Напишите программу, которая по заданной информации о
# пользователях и свободному объему на архивном диске
# определит максимальное число пользователей, чьи данные
# можно поместить в архив.
#
# Формат ввода
#
# Программа получает на вход в одной строке число S – размер
# свободного места на диске (натуральное, не превышает 10000),
# и число N – количество пользователей (натуральное, не превышает 100),
# после этого идет N чисел - объем данных каждого пользователя
# (натуральное, не превышает 1000), записанных каждое в отдельной строке.
#
# Формат вывода
#
# Выведите наибольшее количество пользователей,
# чьи данные могут быть помешены в архив.

# ввод данных

setList = list(map(int, input().split()))

# Цикл для записи чисел объема данных каждого пользователя
# в список userList
# userCount - количество пользователей

i = 1
userCount = setList[1]
userList = []
while i <= userCount:
    userList.append(int(input()))
    i += 1

# Сортировка списка userList по возрастанию

userList.sort()

# Цикл для определения максимального количества пользователей
# s - размер свободной памяти
# sSum - память архива
# j - счетчик для списка userList
# countRar - количество пользователей для ответа

s = setList[0]
sSum = 0
j = 0
countRar = 0
while sSum <= s and j < len(userList):
    sSum = sSum + userList[j]
    if sSum >= s:
        break
    countRar += 1
    j += 1

print(countRar)
