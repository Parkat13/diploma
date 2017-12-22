# -*- coding: utf-8 -*-
import sys
import codecs
import math
reload(sys)
sys.setdefaultencoding('utf-8')
w = 446134717
f_freq = codecs.open('second_phrases.txt', 'r', 'utf8')
f_tf = codecs.open('secondTFWords.txt', 'r', 'utf8')
f_res = open('second_resChi-Square.txt', 'w')
a = f_freq.read().split()
tf = f_tf.read().split()
dict = {}
for i in range(len(a) / 4):
    dict[a[i * 4] + ' ' + a[i * 4 + 1] + ' ' + a[i * 4 + 2]] = (1.0 * float(a[i * 4 + 3]) - 1.0 * float(tf[i * 4 + 2]) * float (tf[i * 4 + 3]) / w)**2 / (float(tf[i * 4 + 2]) * float (tf[i * 4 + 3]))
for i in sorted(dict, key=dict.__getitem__, reverse=True):
    f_res.write(str(i) + ' ' + str(dict[i]) + '\n')
f_freq.close()
f_tf.close()
f_res.close()