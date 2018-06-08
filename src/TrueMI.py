# -*- coding: utf-8 -*-
import codecs
import math
w = 446134717
f_freq = codecs.open('phrases(200,250).txt', 'r', 'utf8')
f_tf = codecs.open('secondTFWords.txt', 'r', 'utf8')
f_res = open('min_resTrueMI.txt', 'w')
a = f_freq.read().split()
tf = f_tf.read().split()
dict = {}
for i in range(len(a) // 4):
    dict[a[i * 4] + ' ' + a[i * 4 + 1] + ' ' + a[i * 4 + 2]] = float(a[i * 4 + 3]) * math.log(1.0 * w * float(a[i * 4 + 3]) / (float(tf[i * 4 + 2]) * float (tf[i * 4 + 3])))
for i in sorted(dict, key=dict.__getitem__, reverse=True):
    f_res.write(str(i) + ' ' + str(dict[i]) + '\n')
f_freq.close()
f_tf.close()
f_res.close()