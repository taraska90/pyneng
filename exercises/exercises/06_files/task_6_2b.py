# -*- coding: utf-8 -*-
'''
Задание 6.2b

Дополнить скрипт из задания 6.2a:
* вместо вывода на стандартный поток вывода, скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.

Строки, которые начинаются на '!' отфильтровывать не нужно.
'''

ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv
#file_name = argv[1]
ignore = ['duplex', 'alias', 'Current configuration']
file_name='config_sw1.txt'

with open(file_name, 'r') as f:
    for line in f:#проходим по тексту
        line=line.split(' ')#формируем из строки список
        for l in line:#перебираю элементы списка line
            for i in ignore:  #перебираю элементы списка ignore
                if l == i:# если элементы совпадают
                    line = ' '#то делаем строку пустой
        line=' '.join(line)#для всего остального собираем список в строку по пробелам
        if line.startswith('!') | line.startswith(ignore[2]):# если строка начинается с ! или Current configuration
            don=line#обнуляю строку
        else:
             with open('config_sw1_cleared.txt', 'a+') as f2:                                                
                f2.write(line)        
        line=list(line)
