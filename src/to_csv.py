# -*- coding: utf-8 -*-
import codecs
import pandas as pd
f = list(None for i in range(14))
k = 0
for i in ['MI', 'AugmentedMI', 'NormalizedMI', 'TrueMI', 'CubicMI', 'DC', 'ModifiedDC', 'T-Score', 'Chi-Square', 'LLR', 'C-Value', 'Word2vec', 'WordsWord2vec', 'SinonimFinish']:
    f[k] = codecs.open('second_res' + i + '.txt', 'r', 'utf8')
    k += 1

a = f[0].read().split()
ph = []
cl = []
for i in range(len(a)//4):
    ph.append(a[4 * i + 1] + ' ' + a[4 * i + 2])
    if a[4 * i] == 'T':
        cl.append(1)
    else:
        cl.append(0)
table = pd.DataFrame(cl, index = ph, columns = ['Class'])
f[0].close()
f[0] = codecs.open('second_resMI.txt', 'r', 'utf8')
k = 0
for i in ['MI', 'AugmentedMI', 'NormalizedMI', 'TrueMI', 'CubicMI', 'DC', 'ModifiedDC', 'T-Score', 'Chi-Square', 'LLR']:
    table[i] = list(None for j in range(len(ph)))
    a = f[k].read().split()
    for l in range(len(a)//4):
        table.at[a[4 * l + 1] + ' ' + a[4 * l + 2], i] = float(a[4 * l + 3])
    k += 1

table['C-Value'] = list(None for j in range(len(ph)))
a = f[10].read().split()
for l in range(len(a)//3):
    table.at[a[3 * l] + ' ' + a[3 * l + 1], 'C-Value'] = float(a[3 * l + 2])

k = 11
for i in ['Word2vec', 'WordsWord2vec', 'Sinonim']:
    table[i] = list(None for j in range(len(ph)))
    a = f[k].read().split()
    for l in range(len(a)//4):
        table.at[a[4 * l + 1] + ' ' + a[4 * l + 2], i] = float(a[4 * l + 3])
    k += 1

table.to_csv('feature.csv')
for i in range(14):
    f[i].close()