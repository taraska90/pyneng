# -*- coding: utf-8 -*-
'''
Задание 5.1a

Сделать копию скрипта задания 5.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'
'''
ip_address = raw_input('Enter ip address in decimal-dot fromat (10.1.1.0): ')
ip_address_list=ip_address.split('.') #сделаю список по октетам
first_octet=int(ip_address_list[0])
for position, octet in enumerate(ip_address_list, 1):                 
    try:    
        int(octet)            
    except ValueError:
        print 'введите число'
for position, octet in enumerate(ip_address_list, 1):
    if int(octet) > 255 or int(octet) < 0 or int(position) != 4:
        print 'Incorrect IPv4 address'
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
