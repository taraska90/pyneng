# -*- coding: utf-8 -*-
'''
Задание 6.3

Скрипт должен обрабатывать записи в файле CAM_table.txt таким образом чтобы:
- считывались строки, в которых указаны MAC-адреса
- каждая строка, где есть MAC-адрес, должна обрабатываться таким образом,
  чтобы на стандартный поток вывода была выведена таблица вида:

 100    aabb.cc80.7000     Gi0/1
 200    aabb.cc80.7000     Gi0/2
 300    aabb.cc80.7000     Gi0/3
 100    aabb.cc80.7000     Gi0/4
 500    aabb.cc80.7000     Gi0/5
 200    aabb.cc80.7000     Gi0/6
 300    aabb.cc80.7000     Gi0/7

'''

with open('CAM_table.txt', 'r') as mac_list:
    for mac in mac_list:
        mac=mac.split(' ')
        for m in mac:
            if m == 'aabb.cc80.7000':
               mac_str=' '.join(mac)
               mac_str=mac_str.rstrip()     
               print mac_str
#if mac[5]=='aabb.cc80.7000':
#            mac_list=''.join(mac)
#            print mac_list
        
