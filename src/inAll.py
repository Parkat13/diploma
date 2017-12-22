# -*- coding: utf-8 -*-
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
f1 = codecs.open('NUpdateRangMI.txt', 'r', 'utf8')
f2 = codecs.open('NUpdateRangAugmentedMI.txt', 'r', 'utf8')
f3 = codecs.open('NUpdateRangNormalizedMI.txt', 'r', 'utf8')
f4 = codecs.open('NUpdateRangTrueMI.txt', 'r', 'utf8')
f5 = codecs.open('NUpdateRangCubicMI.txt', 'r', 'utf8')
f6 = codecs.open('NUpdateRangT-Score.txt', 'r', 'utf8')
f7 = codecs.open('NUpdateRangDC.txt', 'r', 'utf8')
f8 = codecs.open('NUpdateRangModifiedDC.txt', 'r', 'utf8')
f9 = codecs.open('NUpdateRangChi-Square.txt', 'r', 'utf8')
f10 = codecs.open('NUpdateRangLLR.txt', 'r', 'utf8')
f11 = codecs.open('NUpdateRangWord2vec.txt','r','utf8')
f12 = codecs.open('NUpdateRangWordsWord2vec.txt','r','utf8')
f13 = codecs.open('NUpdateRangC-Value.txt','r','utf8')
f_res = open('NUpdateRang.txt', 'w')
dict = {}
dict_met = {}
for f in [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13]:
    a = f.read().split()
    for i in range(len(a)/4):
        if (a[i*4] + ' ' + a[i*4 + 1]) in dict:
            if dict[a[i*4] + ' ' + a[i*4 + 1]] < float(a[i*4 + 2]):# отличается для T и N
                dict[a[i*4] + ' ' + a[i*4 + 1]] = float(a[i*4 + 2])
                dict_met[a[i*4] + ' ' + a[i*4 + 1]] = a[i*4 + 3]
        else:
            dict[a[i*4] + ' ' + a[i*4 + 1]] = float(a[i*4 + 2])
            dict_met[a[i*4] + ' ' + a[i*4 + 1]] = a[i*4 + 3]
for i in sorted(dict, key=dict.__getitem__, reverse=True):# отличается для T и N
    f_res.write(str(i) + ' ' + str(int(dict[i])) + ' ' + dict_met[i] + '\n')
f_res.close()
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
f10.close()
f11.close()
f12.close()
f13.close()
