# -*- coding: utf-8 -*-
import codecs
f = codecs.open('second_resSinonimFinish(only_T).txt', 'r', 'utf8')
f_g = codecs.open('second_phrases.txt', 'r', 'utf8')
f_t = open('TRangSinonim(only_T).txt', 'w')
f_n = open('NRangSinonim(only_T).txt', 'w')
a = f.read().split()
b = f_g.read().split()
dict = {}
for i in range(len(b)//4):
    dict[b[i*4 +1] + ' ' + b[i*4 + 2]] = b[i*4]
n = 1
for i in range(len(a)//4):
    if dict[a[i*4+1] + ' ' + a[i*4 + 2]] == 'T':
        f_t.write(a[i * 4+1] + ' ' + a[i * 4 + 2] + ' ' + str(n) + ' ' + 'Sinonim(only_T)' + '\n')
    else:
        f_n.write(a[i * 4+1] + ' ' + a[i * 4 + 2] + ' ' + str(n) + ' ' + 'Sinonim(only_T)' + '\n')
    n += 1
f.close()
f_g.close()
f_n.close()
f_t.close()