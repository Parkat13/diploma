# -*- coding: utf-8 -*-
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
f = codecs.open('resC-Value.txt', 'r', 'utf8')
f_g = codecs.open('second_phrases.txt', 'r', 'utf8')
f_t = open('TRangC-Value.txt', 'w')
f_n = open('NRangC-Value.txt', 'w')
a = f.read().split()
b = f_g.read().split()
dict = {}
for i in range(len(b)/4):
    dict[b[i*4 +1] + ' ' + b[i*4 + 2]] = b[i*4]
n = 1
for i in range(len(a)/3):
    if dict[a[i*3] + ' ' + a[i*3 + 1]] == 'T':
        f_t.write(a[i * 3] + ' ' + a[i * 3 + 1] + ' ' + str(n) + ' ' + 'C-Value' + '\n')
    else:
        f_n.write(a[i * 3] + ' ' + a[i * 3 + 1] + ' ' + str(n) + ' ' + 'C-Value' + '\n')
    n += 1
f.close()
f_g.close()
f_n.close()
f_t.close()