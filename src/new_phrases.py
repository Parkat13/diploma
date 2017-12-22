# -*- coding: utf-8 -*-
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
f = codecs.open('phrases_corrected.txt', 'r', 'utf8')
f_w = open('new_phrases.txt', 'w')
a = f.read().split()
for i in range(len(a)/4):
    f_w.write(a[i*4] + ' ' + a[i*4+1] + ' ' + a[i*4+2] + '\n')
f.close()
f_w.close()