# -*- coding: utf-8 -*-
import codecs
import math
w = 446134717
f_freq = codecs.open('TF_substitute_phrases.txt', 'r', 'utf8')
f_tf = codecs.open('TF_substitute_words.txt', 'r', 'utf8')
f_res = open('SubstituteCubicMIForAllPh.txt', 'w')
a = f_freq.read().split()
tf = f_tf.read().split()
dict = {}
dict_TF = {}
for i in range(len(tf)//2):
    dict_TF[tf[i*2]] = tf[i*2+1]
for i in range(len(a)//3):
    if float(a[i * 3 + 2]) == 0.0:
        dict[a[i * 3] + ' ' + a[i * 3 + 1]] = 0.0
    else:
        dict[a[i * 3] + ' ' + a[i * 3 + 1]] = math.log(1.0 + 1.0 * w * float(a[i * 3 + 2])**3 / ( float(dict_TF[a[i*3]]) * float (dict_TF[a[i*3+1]])))
for i in sorted(dict, key=dict.__getitem__, reverse=True):
    f_res.write(str(i) + ' ' + str(dict[i]) + '\n')
f_freq.close()
f_tf.close()
f_res.close()