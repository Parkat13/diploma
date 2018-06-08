# -*- coding: utf-8 -*-
from gensim.models.keyedvectors import KeyedVectors
model = KeyedVectors.load_word2vec_format('text_output.txt', binary=False)
import codecs
f_ph = codecs.open('second_phrases.txt', 'r', 'utf8')
f_pff = codecs.open('phrases(200,250).txt', 'r', 'utf8')
f_res = open('min_resSinonim(only_T).txt', 'w')
f_data = codecs.open('text_output.txt', 'r', 'utf8')
f_tes = codecs.open('tesaurus.txt', 'r', 'utf8')
a = f_data.readline().split()
d = {}
while len(a) > 0:
    d[a[0]] = 0
    a = f_data.readline().split()
print('1\n')
group = f_ph.read().split()
tes_dict = {}
for i in range(len(group)//4):
    if group[4*i] == 'T' and int(group[4*i+3]) > 250:
        tes_dict[group[4*i+1] + '_' + group[4*i+2]] = group[4*i]
tes_word = {}
tes = f_tes.readline().lower().split()
while len(tes) > 0:
    if len(tes) == 1:
        tes_word[tes[0]] = 'T'
    tes = f_tes.readline().lower().split()
dict = {}
group = f_pff.read().split()
for i in range(len(group)//4):
    most_sim = model.wv.most_similar(positive=[group[4 * i + 1] + '_' + group[4 * i + 2]], negative=[], topn=1)
    k, j = 1, 0
    ##mas = most_sim[j][0].split('_')
    ##ob = []
    ##flag = 0
    ##if len(mas) > 1:
        ##flag = 0
        ##if group[4*i+1] == mas[0]:
          ##  flag = 1
            ##ob = [group[4*i+2], mas[1]]
        ##if group[4 * i + 2] == mas[0]:
          ##  flag = 1
            ##ob = [group[4 * i + 1], mas[1]]
        ##if group[4 * i + 1] == mas[1]:
          ##  flag = 1
            ##ob = [group[4 * i + 2], mas[0]]
        ##if group[4 * i + 2] == mas[1]:
          ##  flag = 1
            ##ob = [group[4 * i + 1], mas[0]]


    while (not ('_' in most_sim[j][0]) and not (most_sim[j][0] in tes_word)) or (group[4 * i + 1] == most_sim[j][0]) or (group[4 * i + 2] == most_sim[j][0]) or (('_' in most_sim[j][0]) and not (most_sim[j][0] in tes_dict)):
        if k == (j + 1):
            k += 5
            most_sim = model.wv.most_similar(positive=[group[4 * i + 1] + '_' + group[4 * i + 2]], negative=[], topn=k)
        j += 1
        ##mas = most_sim[j][0].split('_')
        ##ob = []
        ##if len(mas) > 1:
          ##  flag = 0
            ##if group[4 * i + 1] == mas[0]:
              ##  flag = 1
                ##ob = [group[4 * i + 2], mas[1]]
            ##if group[4 * i + 2] == mas[0]:
              ##  flag = 1
                ##ob = [group[4 * i + 1], mas[1]]
            ##if group[4 * i + 1] == mas[1]:
              ##  flag = 1
                ##ob = [group[4 * i + 2], mas[0]]
            ##if group[4 * i + 2] == mas[1]:
              ##  flag = 1
                ##ob = [group[4 * i + 1], mas[0]]
    dict[group[4*i] + ' ' + group[4 * i + 1] + '_' + group[4 * i + 2] + ' ' + most_sim[j][0]] = most_sim[j][1]
    
print('2\n')
for i in sorted(dict, key=dict.__getitem__, reverse=True):
    f_res.write(str(i) + ' ' + str(dict[i]) + '\n')
f_ph.close()
f_res.close()
f_data.close()
