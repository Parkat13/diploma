# -*- coding: utf-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import codecs
f_w = codecs.open('second_resSinonimFinish.txt', 'r', 'utf8')
#f_f = codecs.open('second_resWordsWord2vec.txt', 'r', 'utf8')
dict = {}
a = f_w.read().split()
for i in range(int(len(a)/4)):
    dict[a[4 * i] + ' ' + a[4 * i + 1] + ' ' + a[4 * i + 2]] = float(a[4 * i + 3])
#a = f_f.read().split()
#for i in range(int(len(a)/4)):
#    dict[a[4 * i] + ' ' + a[4 * i + 1] + ' ' + a[4 * i + 2]] *= float(a[4 * i + 3])
for s in ['Word2vec', 'WordsWord2vec']:
    f_c = codecs.open('second_res' + s + '.txt', 'r', 'utf8')
    f_res = open('second_resSinonim+' + s + '.txt', 'w')
    a = f_c.read().split()
    res = {}
    for i in range(int(len(a)/4)):
        res[a[4 * i] + ' ' + a[4 * i + 1] + ' ' + a[4 * i + 2]] = dict[a[4 * i] + ' ' + a[4 * i + 1] + ' ' + a[4 * i + 2]] * float(a[4 * i + 3])
    for i in sorted(res, key=res.__getitem__, reverse=True):
        f_res.write(str(i) + ' ' + str(res[i]) + '\n')
    f_c.close()
    f_res.close()
f_w.close()
#f_f.close()