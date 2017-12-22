# -*- coding: utf-8 -*-
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
f1 = codecs.open('NMapMI.txt', 'r', 'utf8')
f2 = codecs.open('NMapAugmentedMI.txt', 'r', 'utf8')
f3 = codecs.open('NMapNormalizedMI.txt', 'r', 'utf8')
f4 = codecs.open('NMapTrueMI.txt', 'r', 'utf8')
f5 = codecs.open('NMapCubicMI.txt', 'r', 'utf8')
f6 = codecs.open('NMapT-Score.txt', 'r', 'utf8')
f7 = codecs.open('NMapDC.txt', 'r', 'utf8')
f8 = codecs.open('NMapModifiedDC.txt', 'r', 'utf8')
f9 = codecs.open('NMapChi-Square.txt', 'r', 'utf8')
f10 = codecs.open('NMapLLR.txt', 'r', 'utf8')
f_max = open('NMaxMI2.txt', 'w')
f_mean = open('NMeanMI2.txt', 'w')
dict_max = {}
dict_mean = {}
for f in [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]:
    a = f.read().split()
    for i in range(len(a)/3):
        if (a[i*3] + ' ' + a[i*3 + 1]) in dict_max:
            if dict_max[a[i*3] + ' ' + a[i*3 + 1]] < float(a[i*3 + 2]):
                dict_max[a[i*3] + ' ' + a[i*3 + 1]] = float(a[i*3 + 2])
        else:
            dict_max[a[i*3] + ' ' + a[i*3 + 1]] = float(a[i*3 + 2])
        if (a[i*3] + ' ' + a[i*3 + 1]) in dict_mean:
            dict_mean[a[i*3] + ' ' + a[i*3 + 1]] += float(a[i*3 + 2])
        else:
            dict_mean[a[i * 3] + ' ' + a[i * 3 + 1]] = float(a[i * 3 + 2])
for i in sorted(dict_max, key=dict_max.__getitem__, reverse=True):
    f_max.write(str(i) + ' ' + str(dict_max[i]) + '\n')
for i in sorted(dict_mean, key=dict_mean.__getitem__, reverse=True):
    f_mean.write(str(i) + ' ' + str(1.0 * dict_mean[i]/10) + '\n')
f_max.close()
f_mean.close()