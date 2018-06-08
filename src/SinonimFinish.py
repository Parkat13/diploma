# -*- coding: utf-8 -*-
import codecs
f = codecs.open('min_resSinonim(only_T).txt', 'r', 'utf8')
f_t = open('min_resSinonimFinish(only_T).txt', 'w')
a = f.read().split()

for i in range(len(a)//4):
    b = a[i*4 + 1].split('_')
    f_t.write(a[i * 4] + ' ' + b[0] + ' ' + b[1] + ' ' + a[i*4 + 3] + '\n')
f.close()
f_t.close()