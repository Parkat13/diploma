# -*- coding: utf-8 -*-
import sys
#import time
import codecs
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
reload(sys)
sys.setdefaultencoding('utf-8')
f_obuch = codecs.open('text.txt', 'r', 'utf8')
f_finish = open('res_C-Value.txt', 'w')
f_group = codecs.open('second_phrases.txt', 'r', 'utf8')
words_group_normal = f_group.read().split()
dict = {}
dict_TF = {}
for i in range(len(words_group_normal)/4):
    dict[words_group_normal[i*4+1] + ' ' + words_group_normal[i*4+2]] = {}
    dict_TF[words_group_normal[i * 4 + 1] + ' ' + words_group_normal[i * 4 + 2]] = words_group_normal[i*4 + 3]
words_str = f_obuch.read(1000)
flag_last_word = 0
if words_str[-1] == ' ':
    flag_last_word = 1
words = words_str.lower().split()
word_1 = ''
word_2 = ''
word_3 = words[0]
word_4 = words[1]
sd = {}
if len(words) == 1:
    words.append(' ')
k = 0
# #f_slovosoch.close()
words = words[2:]
while len(words) != 0:
    #start_time = time.time()
    for j in range(len(words)-1):
        word_1,word_2,word_3,word_4 = word_2,word_3,word_4,words[j]
        if ( word_2 + ' ' + word_3) in dict:
            if (word_1 + ' ' + word_4) in dict[word_2 + ' ' + word_3]:
                dict[word_2 + ' ' + word_3][word_1 + ' ' + word_4] += 1
            else:
                if word_1 in sd:
                    if sd[word_1] not in ['NOUN', 'ADJF']:
                        word_1 = ''
                else:
                    p = morph.parse(word_1)[0].tag.POS
                    if p not in ['NOUN', 'ADJF']:
                        word_1 = ''
                    sd[word_1] = p
                if word_4 in sd:
                    if sd[word_4] not in ['NOUN', 'ADJF']:
                        word_4 = ''
                else:
                    p = morph.parse(word_4)[0].tag.POS
                    if p not in ['NOUN', 'ADJF']:
                        word_4 = ''
                    sd[word_4] = p
                if len(word_1.split()) == 0 and len(word_4.split()) == 0:
                    continue
                dict[word_2 + ' ' + word_3][word_1 + ' ' + word_4] = 1
    if k%100000 == 0:
        print k/100000
    #print k/100000, "--- %s seconds ---" % (time.time() - start_time)
    k += 1
    if flag_last_word == 1:
        words_str = (words[-1] + ' ' + f_obuch.read(1000).strip())
    else:
        words_str = (words[-1] + f_obuch.read(1000).strip())
    flag_last_word = 0
    if (words_str == '  ') or (words_str == ' '):
        break
    if words_str[-1] == ' ':
        flag_last_word = 1
    words = words_str.lower().split()
    if len(words) == 1:
        words.append(' ')
word_1,word_2,word_3 = word_2,word_3,word_4
if (word_2 + ' ' + word_3) in dict:
    if (word_1 + ' ') in dict[word_2 + ' ' + word_3]:
        dict[word_2 + ' ' + word_3][word_1 + ' '] += 1
    else:
        if word_1 in sd:
            if sd[word_1] not in ['NOUN', 'ADJF']:
                word_1 = ''
        else:
            p = morph.parse(word_1)[0].tag.POS
            if p not in ['NOUN', 'ADJF']:
                word_1 = ''
            sd[word_1] = p
        if len(word_1.split()) == 1:
            dict[word_2 + ' ' + word_3][word_1 + ' '] = 1
print 'end of file :)\n'
dict_res = {}
for i in dict:
    res = float(dict_TF[i])
    s = 0.0
    for j in dict[i]:
        s += float(dict[i][j])
    if len(dict[i]) == 0:
        dict_res[i] = res
    else:
        dict_res[i] = res - s/float(len(dict[i]))
for i in sorted(dict_res, key=dict_res.__getitem__, reverse=True):
    f_finish.write(str(i) + ' ' + str(dict_res[i]) + '\n')
f_obuch.close()
f_finish.close()
f_group.close()
