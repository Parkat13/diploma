# -*- coding: utf-8 -*-
import codecs
import math
f_data = codecs.open('second_phrases.txt', 'r', 'utf8')
dict = {}
a = f_data.read().split()
for i in range(len(a)//4):
    dict[a[4 * i] + ' ' + a[4 * i + 1] + ' ' + a[4 * i + 2]] = a[4 * i + 3]
for str0 in ['']:
    f = codecs.open('second_resSinonimFinish(only_T)' + str0 + '.txt', 'r', 'utf8')
    f_t = open('second_reslogTF+Sinonim(only_T)' + str0 + '.txt', 'w')
    a = f.read().split()
    res = {}
    for i in range(len(a)//4):
        res[a[4 * i] + ' ' + a[4 * i + 1] + ' ' + a[4 * i + 2]] = math.log(float(dict[a[4 * i] + ' ' + a[4 * i + 1] + ' ' + a[4 * i + 2]])) * float(a[4 * i + 3])
    for i in sorted(res, key=res.__getitem__, reverse=True):
        f_t.write(str(i) + ' ' + str(res[i]) + '\n')
    f.close()
    f_t.close()
f_data.close()