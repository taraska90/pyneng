# -*- coding: utf-8 -*-

'''
Задание 11.3

В прошлых заданиях мы добавляли информацию в пустую БД.
Теперь разберемся с ситуацией, когда в БД уже есть информация.

Попробуйте выполнить скрипт add_data.py повторно, на существующей БД.
У вас  должна возникнуть ошибка.

Когда мы создавали схему БД, мы явно указали, что поле MAC-адрес, должно быть уникальным.
Поэтому, когда мы пытаемся добавить записи с таким же MAC-адресом, возникает ошибка.

Но, нам нужно каким-то образом обновлять БД, чтобы в ней хранилась актуальная информация.

Например, можно каждый раз, когда мы записываем информацию,
предварительно просто удалять всё из таблицы dhcp.

Но, в принципе, старая информация тоже может пригодится.

Поэтому, мы будем делать немного по-другому.
Мы создадим новое поле active, которое будет указывать является ли запись актуальной.

Поле active должно принимать такие значения:
* 0 - означает False. И используется для того, чтобы отметить запись как неактивную
* 1 - True. Используется чтобы указать, что запись активна

Каждый раз, когда мы добавляем заново информацию из файлов с выводом DHCP snooping,
мы сначала помечаем все существующие записи (для данного коммутатора),
как неактивные (active = 0).
А затем начинаем обновлять информацию и помечаем новые записи, как активные (active = 1).


Таким образом, в БД останутся и старые записи, для MAC-адресов, которые сейчас не активны,
и появится обновленная информация для активных адресов.

Новая схема БД находится в файле dhcp_snooping_schema.sql

Измените скрипт add_data.py таким образом, чтобы выполнялись новые условия и заполнялось поле active.

> Не забывайте, что вы можете попробовать выполнить запросы SQL в командной строке, с помощью утилиты sqlite3.

'''
