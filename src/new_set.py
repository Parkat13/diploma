# -*- coding: utf-8 -*-
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
f_freq = codecs.open('new_phrases.txt', 'r', 'utf8')
f_tf = codecs.open('TFWords.txt', 'r', 'utf8')
f_tes = codecs.open('tes_nottes.txt','r','utf8')
f_ph = open('second_phrases.txt', 'w')
f_ntf = open('secondTFWords.txt', 'w')
a = f_freq.read().split()
tf = f_tf.read().split()
tes = f_tes.read().split()
dict = {}
dict_tes = {}
for i in range(len(a)/3):
    dict[a[i*3 + 1] + ' ' + a[i*3 + 2]] = a[i*3]
for i in range(len(tes)/4):
    dict_tes[tes[i*4 + 1] + ' ' + tes[i*4 + 2]] = tes[i*4 + 3]
for i in range(len(tf)/4):
    if (tf[i*4] + ' ' + tf[i*4 + 1]) in dict:
        f_ph.write(dict[tf[i*4] + ' ' + tf[i*4 + 1]] + ' ' + tf[i*4] + ' ' + tf[i*4 + 1] + ' ' + dict_tes[tf[i*4] + ' ' + tf[i*4 + 1]] + '\n')
        f_ntf.write(tf[i*4] + ' ' + tf[i*4 + 1] + ' ' + tf[i*4 + 2] + ' ' + tf[i*4 + 3] + '\n')
f_freq.close()
f_tf.close()
f_tes.close()
f_ph.close()
f_ntf.close()