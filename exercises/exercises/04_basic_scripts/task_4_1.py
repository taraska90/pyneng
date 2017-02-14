# -*- coding: utf-8 -*-
"""
Задание 4.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.
"""
net = raw_input('Enter ip network in this format: 10.1.1.0/24: ')
#После ввода префикса мне нужно выделить саму сеть и маску
prefix_and_mask=net.split('/') #разделитель по слешу
'''
тогда вывод будет такой:
prefix_and_mask
['10.10.10.0', '24']
'''
#Префикс будет такой:
prefix=prefix_and_mask[0]
prefix_dec=prefix.split('.') #сделаю список по октетам
prefix_bin_1=bin(int(str(prefix_dec[0])))[2:].zfill(8) #переведу каждый октет в двоичный вид [2:] - пропущу первые два символа, они не информативны
prefix_bin_2=bin(int(str(prefix_dec[1])))[2:].zfill(8)
prefix_bin_3=bin(int(str(prefix_dec[2])))[2:].zfill(8)
prefix_bin_4=bin(int(str(prefix_dec[3])))[2:].zfill(8)
print "Network: "
print '{0:10} {1:10} {2:10} {3:10} \n{4:10} {5:10} {6:10} {7:10}'.format(prefix_dec[0], prefix_dec[1], prefix_dec[2], prefix_dec[3], prefix_bin_1, prefix_bin_2, prefix_bin_3, prefix_bin_4) #{1}-позиция переменной с номером, а число после двоеточия это видимо заполнение
#а маска будет такой:
mask=prefix_and_mask[1]
mask_dec=''
mask=int(mask)#переведу в целочисл
for t in range(4):
        if mask > 7: #если маска больше 7
            mask_dec += '255.'#то значит это 255
        else:
            dec = 255 - (2**(8 - mask) - 1)#иначе вычесть из 255 2 в степени маска - 8 и минус один
            mask_dec += str(dec) + '.'
        mask -= 8
        if mask < 0:
            mask = 0       
prefix_mask_dec=mask_dec.split('.') #сделаю список по октетам
mask_bin_octet_1=bin(int(str(prefix_mask_dec[0])))[2:].zfill(8)
mask_bin_octet_2=bin(int(str(prefix_mask_dec[1])))[2:].zfill(8)
mask_bin_octet_3=bin(int(str(prefix_mask_dec[2])))[2:].zfill(8)
mask_bin_octet_4=bin(int(str(prefix_mask_dec[3])))[2:].zfill(8)
print "Mask:"
print prefix_and_mask[1]
print '{0:10} {1:10} {2:10} {3:10} \n{4:10} {5:10} {6:10} {7:10}'.format(prefix_mask_dec[0], prefix_mask_dec[1], prefix_mask_dec[2], prefix_mask_dec[3], mask_bin_octet_1, mask_bin_octet_2, mask_bin_octet_3, mask_bin_octet_4)



