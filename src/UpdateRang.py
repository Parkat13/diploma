# -*- coding: utf-8 -*-
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
f = codecs.open('second_resT-Score.txt', 'r', 'utf8')
f_t = open('TUpdateRangT-Score.txt', 'w')
f_n = open('NUpdateRangT-Score.txt', 'w')
a = f.read().split()
n = 0
m = -1.0
for i in range(len(a)/4):
    if m != float(a[i * 4 + 3]):
        n += 1
        m = float(a[i * 4 + 3])
    if a[i*4] == 'T':
        f_t.write(a[i * 4 + 1] + ' ' + a[i * 4 + 2] + ' ' + str(n) + ' ' + 'T-Score' + '\n')
    else:
        f_n.write(a[i * 4 + 1] + ' ' + a[i * 4 + 2] + ' ' + str(n) + ' ' + 'T-Score' + '\n')
f.close()
f_n.close()
f_t.close()