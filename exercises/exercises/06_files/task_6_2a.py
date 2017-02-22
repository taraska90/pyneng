# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.
'''
from sys import argv
#file_name = argv[1]
ignore = ['duplex', 'alias', 'Current configuration']
file_name='config_sw1.txt'

with open(file_name, 'r') as f:
    for line in f:#проходим по тексту
        line=line.rstrip().split(' ')#формируем из строки список
        for l in line:#перебираю элементы списка line
            for i in ignore:  #перебираю элементы списка ignore
                if l == i:# если элементы совпадают
                    line = ' '#то делаем строку пустой
        line=' '.join(line)#для всего остального собираем список в строку по пробелам
        if line.startswith('!') | line.startswith(ignore[2]):# если строка начинается с ! или Current configuration
            don=line#обнуляю строку
        else:   
            print ''.join(line.split('\n'))#иначе собираю в список по какому символу?
        line=list(line)
       
