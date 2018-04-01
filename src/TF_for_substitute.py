# -*- coding: utf-8 -*-
import time
import codecs
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
f_obuch = codecs.open('text.txt', 'r', 'utf8')
f_ph = codecs.open('second_phrases.txt', 'r', 'utf8')
f_finish = open('TF_substitute_words.txt', 'w')
f_f = open('TF_substitute_phrases.txt', 'w')
f_group = codecs.open('substitute.txt', 'r', 'utf8')
words_group_normal = f_group.read().split()
dict = {}
dict_TF = {}
dict_ph = {}
for i in range(len(words_group_normal)//11):
    dict[words_group_normal[i*11]] = set()
    dict_TF[words_group_normal[i * 11]]= 0
    for j in range(5):
        dict[words_group_normal[i*11]].add(words_group_normal[i*11+j*2+1])
        dict_TF[words_group_normal[i*11+2*j+1]] = 0

a = f_ph.readline().split()
while len(a)!=0:
    dict_ph[a[1] + ' ' + a[2]] = 0
    for j in dict[a[1]]:
        dict_ph[j + ' ' + a[2]] = 0
    for j in dict[a[2]]:
        dict_ph[a[1] + ' ' + j] = 0
    a = f_ph.readline().split()

words_str = f_obuch.read(100000000)
flag_last_word = 0
if words_str[-1] == ' ':
    flag_last_word = 1
words = words_str.split()
str_nul = ''
if len(words) == 1:
    words.append(' ')
k = 0
while len(words) != 0:
    start_time = time.time()
    for j in range(len(words)-1):
        words[j] = words[j].lower()
        if (str_nul + ' ' + words[j]) in dict_ph:
            dict_ph[str_nul + ' ' + words[j]] += 1
        if words[j] in dict_TF:
            dict_TF[words[j]] += 1
        str_nul = words[j]
    print (k, "--- %s seconds ---" % (time.time() - start_time))
    k += 1
    if flag_last_word == 1:
        words_str = (words[-1] + ' ' + f_obuch.read(100000000).strip())
    else:
        words_str = (words[-1] + f_obuch.read(100000000).strip())
    flag_last_word = 0
    if (words_str == '  ') or (words_str == ' '):
        break
    if words_str[-1] == ' ':
        flag_last_word = 1
    words = words_str.split()
    if len(words) == 1:
        words.append(' ')
for i in sorted(dict_TF, key=dict_TF.__getitem__, reverse=True):
    f_finish.write(str(i) + ' ' + str(dict_TF[i]) + '\n')
for i in sorted(dict_ph, key=dict_ph.__getitem__, reverse=True):
    f_f.write(str(i) + ' ' + str(dict_ph[i]) + '\n')
f_obuch.close()
f_finish.close()
f_group.close()
f_ph.close()
f_f.close()
