# -*- coding: utf-8 -*-
import codecs
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
from gensim.models.keyedvectors import KeyedVectors
model = KeyedVectors.load_word2vec_format('text_output_standard.txt', binary=False)
f_phrases = codecs.open('second_phrases.txt', 'r', 'utf8')
f_words = open('substitute.txt', 'w')
list_f = ['Abbr', 'Name', 'Surn', 'Patr', 'Geox', 'Orgn', 'Trad', 'Erro', 'Init']
#f_new_phrases = open('substitute_phrases' ,'w')
a = f_phrases.read().split()
dict = {}
for i in range(int(len(a)/4)):
    if a[i*4+1] not in dict:
        dict[a[i*4+1]] = []
    if a[i*4+2] not in dict:
        dict[a[i*4+2]] = []
n = 0
for i in dict:
    most_sim = model.wv.most_similar(positive=[i], negative=[], topn=10)
    p1 = morph.parse(i)[0]
    m = []
    ind = 0
    while len(m) != 5:
        if len(most_sim) == ind:
            most_sim = most_sim = model.wv.most_similar(positive=[i], negative=[], topn=ind+5)
        p2 = morph.parse(most_sim[ind][0])[0]
        if p1.tag.POS == p2.tag.POS and str(p2.methods_stack[0][0]) != '<FakeDictionary>' and (len(p2.methods_stack) == 1 or str(p2.methods_stack[1][0]) != '<UnknownPrefixAnalyzer>'):
            for j in list_f:
                if j in p2.tag:
                    break
            else:
                if i[0:3] == most_sim[ind][0][0:3]:
                    ind += 1
                    continue
                else:
                    m.append(most_sim[ind])
                    ind += 1
                    continue
            ind += 1
            continue
        else:
            ind += 1
            continue
    dict[i] = m
    print(n)
    n += 1

for i in dict:
    f_words.write(str(i) + ' ')
    for j in range(5):
        f_words.write(str(dict[i][j][0]) + ' ' + str(dict[i][j][1]) + ' ')
    f_words.write('\n')
f_phrases.close()
f_words.close()
#f_new_phrases.close()
