# -*- coding: utf-8 -*-
'''
Задание 6.3a

Сделать копию скрипта задания 6.3.

Дополнить скрипт:
  Отсортировать вывод по номеру VLAN
'''

with open('CAM_table.txt', 'r') as mac_list:
    for mac in mac_list:
        mac=mac.split(' ')
        for m in mac:
            if m == 'aabb.cc80.7000':
               mac_list=[mac  ]
               #mac_str=mac_str.rstrip()     
               print mac_str
#if mac[5]=='aabb.cc80.7000':
#            mac_list=''.join(mac)
#            print mac_list
        
