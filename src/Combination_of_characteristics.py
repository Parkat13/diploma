# -*- coding: utf-8 -*-
import codecs
t1 = 'C-Value'
t2 = 'WordsWord2vec'
f_1 = [codecs.open('TRang' + t1 + '.txt', 'r', 'utf8'), codecs.open('NRang' + t1 + '.txt', 'r', 'utf8')]
f_2 = [codecs.open('TRang' + t2 + '.txt', 'r', 'utf8'), codecs.open('NRang' + t2 + '.txt', 'r', 'utf8')]
f_3 = [codecs.open('TRangSinonim.txt', 'r', 'utf8'), codecs.open('NRangSinonim.txt', 'r', 'utf8')]
#f_res12 = open('resWord2vec+WordsWord2vec.txt', 'w')
f_res13 = open('resSumRang' + t1 + '+Sinonim.txt', 'w')
f_res23 = open('resSumRang' + t2 + '+Sinonim.txt', 'w')
#f_res123 = open('resWord2vec+WordsWord2vec+Sinonim.txt', 'w')
fl = ['T', 'N']
dict = [{}, {}, {}]
for i in range(2):
    k = 0
    for f in [f_1, f_2, f_3]:
        data = f[i].read().split()
        for j in range(len(data)//4):
            dict[k][fl[i] + ' ' + data[j * 4] + ' ' + data[j * 4 + 1]] = int(data[j * 4 + 2])
        k += 1
res = [{}, {}, {}]
res_all = {}
for i in dict[0]:
    res[0][i] = dict[0][i] + dict[1][i]
    res[1][i] = dict[0][i] + dict[2][i]
    res[2][i] = dict[1][i] + dict[2][i]
    res_all[i] = dict[0][i] + dict[1][i] + dict[2][i]
#for i in sorted(res[0], key=res[0].__getitem__, reverse=False):
#    f_res12.write(str(i) + ' ' + str(res[0][i]) + '\n')
for i in sorted(res[1], key=res[1].__getitem__, reverse=False):
    f_res13.write(str(i) + ' ' + str(res[1][i]) + '\n')
for i in sorted(res[2], key=res[2].__getitem__, reverse=False):
    f_res23.write(str(i) + ' ' + str(res[2][i]) + '\n')
#for i in sorted(res_all, key=res_all.__getitem__, reverse=False):
#    f_res123.write(str(i) + ' ' + str(res_all[i]) + '\n')
f_1[0].close()
f_1[1].close()
f_2[0].close()
f_2[1].close()
f_3[0].close()
f_3[1].close()
#f_res12.close()
f_res13.close()
f_res23.close()
#f_res123.close()