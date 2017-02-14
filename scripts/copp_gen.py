#!/usr/bin/python
# -*- coding: utf-8 -*-

acl_name
border_ip = '109.230.128.2'
#меняю access-list на ip access-list
acl=acl.replace('access-list', 'ip access-list')
#Вставляю адрес роутера
acl=acl.replace('<router receive block>', border_ip)
