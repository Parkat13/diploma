# -*- coding: utf-8 -*-
import sys
import codecs
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
reload(sys)
sys.setdefaultencoding('utf-8')
f_ph = codecs.open('second_phrases.txt', 'r', 'utf8')
f_group = codecs.open('substitute.txt', 'r', 'utf8')
f_mera = codecs.open('SubstituteCubicMIForAllPh.txt', 'r', 'utf8')
f_res = open('SubstituteCubicMISumRes5.txt', 'w')
number = 5
a = f_mera.read().split()
dict_sinonim = {}
dict_ph = {}
dict_res = {}
for i in range(len(a)/3):
    dict_ph[a[i*3] + ' ' + a[i*3+1]] = a[i*3+2]
a = f_group.read().split()
for i in range(len(a)/11):
    dict_sinonim[a[i*11]] = [[a[i*11+1],a[i*11+2]],[a[i*11+3],a[i*11+4]],[a[i*11+5],a[i*11+6]],[a[i*11+7],a[i*11+8]],[a[i*11+9],a[i*11+10]]]
a = f_ph.read().split()
for i in range(len(a)/4):
    s = 0.0
    for j in range(number):
        s += float(dict_sinonim[a[i*4+1]][j][1])*float(dict_ph[dict_sinonim[a[i*4+1]][j][0] + ' ' + a[i*4+2]])
    for j in range(number):
        s += float(dict_sinonim[a[i * 4 + 2]][j][1]) * float(dict_ph[a[i * 4 + 1] + ' ' + dict_sinonim[a[i * 4 + 2]][j][0]])
    dict_res[a[i*4+1] + ' ' + a[i*4+2]] = 1.0*s/(2.0*number)
for i in sorted(dict_res, key=dict_res.__getitem__, reverse=False):
    f_res.write(str(i) + ' ' + str(dict_res[i]) + '\n')
f_ph.close()
f_group.close()
f_mera.close()
f_res.close()

