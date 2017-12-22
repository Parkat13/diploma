# -*- coding: utf-8 -*-
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
f_ph = codecs.open('second_resCubicMI2.txt', 'r', 'utf8')
f_data = codecs.open('SubstituteCubicMISumRes5.txt', 'r', 'utf8')
f_res = open('resSubstituteCubicMI5.txt', 'w')
a = f_data.read().split()
dict = {}
dict_res = {}
for i in range(len(a)/3):
    dict[a[i*3] + ' ' + a[i*3+1]] = a[i*3+2]
a = f_ph.read().split()
for i in range(len(a)/4):
    dict_res[a[i*4] + ' ' + a[i*4+1] + ' ' + a[i*4+2]] = float(a[i*4+3]) - float(dict[a[i*4+1] + ' ' + a[i*4+2]])
for i in sorted(dict_res, key=dict_res.__getitem__, reverse=True):
    f_res.write(str(i) + ' ' + str(dict_res[i]) + '\n')
f_ph.close()
f_data.close()
f_res.close()

