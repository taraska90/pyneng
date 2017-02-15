# -*- coding: utf-8 -*-
'''
Задание 5.1

1. Запросить у пользователя ввод IP-адреса в десятично-точечном формате.
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239
'''

ip_address = raw_input('Enter ip address in decimal-dot fromat (10.1.1.0): ')
ip_address_list=ip_address.split('.') #сделаю список по октетам
first_octet=int(ip_address_list[0])
if first_octet == 0:
    print 'unassigned'
elif first_octet < 128:
    print 'unicast, class A'
elif first_octet < 192:
    print 'unicast, class B'
elif first_octet < 224:
    print 'unicast, class C'
elif first_octet < 240:
    print 'multicast, class D'
elif first_octet > 240:
    if ip_address == '255.255.255.255':
        print 'local broadcast'    
    else:    
        print 'unused'    
