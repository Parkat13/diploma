# -*- coding: utf-8 -*-
import sys
import codecs
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
reload(sys)
sys.setdefaultencoding('utf-8')
list_f = ['Abbr', 'Name', 'Surn', 'Patr', 'Geox', 'Orgn', 'Trad', 'Erro', 'Init']
f_freq = codecs.open('freq_last.txt', 'r', 'utf8')
f_finish = open('freq_last_per.txt', 'w')
freq = f_freq.read().lower().split()
for i in range(len(freq) / 3):
    if int(freq[3 * i + 2]) < 200:
        break
    p1 = morph.parse(freq[i * 3])[0]
    p2 = morph.parse(freq[i * 3 + 1])[0]
    if (p1.tag.POS == 'NOUN' and p2.tag.POS == 'NOUN') or (p1.tag.POS == 'ADJF' and p2.tag.POS == 'NOUN'):
        for j in list_f:
            if (j in p1.tag) or (j in p2.tag):
                break
            else:
                fl = 0
                for k in range(len(freq[3 * i])):
                    if freq[3 * i][k].isdigit():
                        fl = 1
                        break
                if fl:
                    break
                else:
                    for k in range(len(freq[3 * i + 1])):
                        if freq[3 * i + 1][k].isdigit():
                            fl = 1
                            break
                    if fl:
                        break
        else:
            f_finish.write(freq[3 * i] + ' ' + freq[3 * i + 1] + ' ' + freq[3 * i + 2] + '\n')
f_freq.close()
f_finish.close()
