# Курс основы программирования на Python
# Задание по программированию: Отсортировать список участников по алфавиту
# 14.05.2019
#
# Известно, что фамилии всех участников — различны. Сохраните в
# массивах список всех участников и выведите его, отсортировав по
# фамилии в лексикографическом порядке. При выводе указываете
# фамилию, имя участника и его балл.
#
# Используйте для ввода и вывода файлы input.txt и output.txt
# с указанием кодировки utf8. Например, для чтения откройте
# файл с помощью open('input.txt', 'r', encoding='utf8').
#
# Входные данные
#
# Строки вида "Фамилия Имя НомерШколы Балл".
#
# Выходные данные
#
# Строки вида "Фамилия Имя Балл", отсортированные по фамилии.
#
# Примечание
#
# Если у Вас Wrong Answer на первом тесте и в вердикте в качестве
# правильного ответа показываются знаки вопросов, это не значит,
# что их действительно нужно выводить. Это баг Курсеры – в вердикте
# кириллица не поддерживается. Курсера знает о проблеме с 25.10.2018
# и возможно починит.
#
# В итоге, при WA на первом тесте не стоит смотреть на вердикт,
# нужно искать ошибку в решении.


def sortLastName(pList):
    """Функция для сортировки по фамилии"""
    return pList[0]


# inFile - Файл с исходными данными
# onFile - Файл с конечнымии данными
# peopleInfo - массив для хранения данных из файла inFile

inFile = open('input.txt', 'r', encoding='utf8')
onFile = open('output.txt', 'w', encoding='utf8')
peopleInfo = []
for people in inFile:
    peopleInfo.append(people.split())

peopleInfo.sort(key=sortLastName)

for info in peopleInfo:
    print(info[0], info[1], info[3], file=onFile)

inFile.close()
onFile.close()
