# -*- coding: utf-8 -*-
import codecs
f_ph = codecs.open('second_phrases.txt', 'r', 'utf8')
f_sub = codecs.open('substitute.txt', 'r', 'utf8')
f_TF = codecs.open('TF_substitute_phrases.txt', 'r', 'utf8')
f_data = codecs.open('SubstituteCubicMIForAllPh.txt', 'r', 'utf8')
f_res = open('SubstituteFormattedOutput.txt', 'w')
a = f_data.read().split()
dict_sub = {}
dict_data = {}
dict_TF = {}
for i in range(len(a)//3):
    dict_data[a[i*3] + ' ' + a[i*3+1]] = a[i*3+2]
a = f_sub.read().split()
for i in range(len(a)//11):
    dict_sub[a[i*11]] = [[a[i*11+1],a[i*11+2]],[a[i*11+3],a[i*11+4]],[a[i*11+5],a[i*11+6]],[a[i*11+7],a[i*11+8]],[a[i*11+9],a[i*11+10]]]
a = f_TF.read().split()
for i in range(len(a)//3):
    dict_TF[a[i*3] + ' ' + a[i*3+1]] = a[i*3+2]
a = f_ph.read().split()
for i in range(len(a)//4):
    f_res.write(a[i*4] + ' ' + a[i*4+1] + ' ' + a[i*4+2] + ' TF = ' + a[i*4+3] + ' : ')
    for j in range(5):
        f_res.write(dict_sub[a[i*4+1]][j][0] + ' ' + a[i*4+2] + ' TF = ' + dict_TF[dict_sub[a[i*4+1]][j][0] + ' ' + a[i*4+2]] + ' MI = ' + dict_data[dict_sub[a[i*4+1]][j][0] + ' ' + a[i*4+2]] + ' ; ')
    for j in range(5):
        f_res.write(a[i * 4 + 1] + ' ' + dict_sub[a[i * 4 + 2]][j][0] + ' TF = ' + dict_TF[a[i * 4 + 1] + ' ' + dict_sub[a[i * 4 + 2]][j][0]] + ' MI = ' + dict_data[a[i * 4 + 1] + ' ' + dict_sub[a[i * 4 + 2]][j][0]] + ' ; ')
    f_res.write('\n')
f_ph.close()
f_data.close()
f_TF.close()
f_res.close()
