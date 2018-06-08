# -*- coding: utf-8 -*-
import codecs
f_w = codecs.open('second_resSinonimFinish(only_T).txt', 'r', 'utf8')
#f_f = codecs.open('second_resWordsWord2vec.txt', 'r', 'utf8')
dict = {}
a = f_w.read().split()
for i in range(int(len(a)/4)):
    dict[a[4 * i] + ' ' + a[4 * i + 1] + ' ' + a[4 * i + 2]] = float(a[4 * i + 3])
f_w1 = codecs.open('second_resWord2vec.txt', 'r', 'utf8')
a = f_w1.read().split()
for i in range(int(len(a)/4)):
    dict[a[4 * i] + ' ' + a[4 * i + 1] + ' ' + a[4 * i + 2]] *= float(a[4 * i + 3])
f_w2 = codecs.open('second_resWordsWord2vec.txt', 'r', 'utf8')
a = f_w2.read().split()
for i in range(int(len(a)/4)):
    dict[a[4 * i] + ' ' + a[4 * i + 1] + ' ' + a[4 * i + 2]] *= float(a[4 * i + 3])
#a = f_f.read().split()
#for i in range(int(len(a)/4)):
#    dict[a[4 * i] + ' ' + a[4 * i + 1] + ' ' + a[4 * i + 2]] *= float(a[4 * i + 3])
for s in ['C-Value']:
    f_c = codecs.open('second_res' + s + '.txt', 'r', 'utf8')
    f_res = open('second_resSinonim(only_T)+Word2vec+WordsWord2vec+' + s + '.txt', 'w')
    a = f_c.read().split()
    res = {}
    for i in range(int(len(a)/3)):
        if 'T ' + a[3 * i] + ' ' + a[3 * i + 1] in dict:
            res['T ' + a[3 * i] + ' ' + a[3 * i + 1]] = dict['T ' + a[3 * i] + ' ' + a[3 * i + 1]] * float(a[3 * i + 2])
        else:
            res['N ' + a[3 * i] + ' ' + a[3 * i + 1]] = dict['N ' + a[3 * i] + ' ' + a[3 * i + 1]] * float(a[3 * i + 2])
    for i in sorted(res, key=res.__getitem__, reverse=True):
        f_res.write(str(i) + ' ' + str(res[i]) + '\n')
    f_c.close()
    f_res.close()
f_w.close()
f_w1.close()
f_w2.close()
#f_f.close()