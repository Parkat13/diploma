# -*- coding: utf-8 -*-
import sys
from gensim.models.keyedvectors import KeyedVectors
model = KeyedVectors.load_word2vec_format('text_output.txt', binary=False)
import codecs
f_ph = codecs.open('second_phrases.txt', 'r', 'utf8')
f_res = open('second_resSinonim.txt', 'w')
print('1\n')
group = f_ph.read().split()
dict = {}
for i in range(int(len(group)/4)):
    most_sim = model.wv.most_similar(positive=[group[4 * i + 1] + '_' + group[4 * i + 2]], negative=[], topn=1)
    k, j = 1, 0
    while ('_' in most_sim[j][0]) or not(most_sim[j][0].isalpha()) or (group[4 * i + 1] == most_sim[j][0]) or (group[4 * i + 2] == most_sim[j][0]):
        if k == (j + 1):
            k += 5
            most_sim = model.wv.most_similar(positive=[group[4 * i + 1] + '_' + group[4 * i + 2]], negative=[], topn=k)
        j += 1
    dict[group[4*i] + ' ' + group[4 * i + 1] + '_' + group[4 * i + 2] + ' ' + most_sim[j][0]] = most_sim[j][1]
    
print('2\n')
for i in sorted(dict, key=dict.__getitem__, reverse=True):
    f_res.write(str(i) + ' ' + str(dict[i]) + '\n')
f_ph.close()
f_res.close()
