# -*- coding: utf-8 -*-
from sys import argv
'''
Задание 6.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
	- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного 
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.
'''
file_name = argv[1]
with open(file_name, 'r') as f:
    for line in f:
        if line.startswith('!'):
            don=line          
        else:        
            print ''.join(line.split('\n'))
	
