# -*- coding: utf-8 -*-
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
f_t = codecs.open('tesaurus.txt', 'r', 'utf8')
f_extract = codecs.open('freq_last.txt', 'r', 'utf8')
f_f = open('tes_nottes.txt', 'w')
a = f_t.readline().lower().split()
dict = {}
while len(a):
    if len(a) == 2:
        dict[a[0] + ' '+ a[1]] = 1
    a = f_t.readline().lower().split()
ext = f_extract.read().split()
for i in range(len(ext)/3):
    if (ext[i*3] + ' ' + ext[i*3 + 1]) in dict:
        f_f.write('T ' + ext[i*3] + ' ' + ext [i*3 + 1] + ' ' + ext[i*3 + 2] + '\n')
    else:
        f_f.write('N ' + ext[i * 3] + ' ' + ext[i * 3 + 1] + ' ' + ext[i * 3 + 2] + '\n')
f_f.close()
f_extract.close()
f_t.close()