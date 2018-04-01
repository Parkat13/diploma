# -*- coding: utf-8 -*-
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
f_ph = codecs.open('SubstituteTFRes5.txt', 'r', 'utf8')
a  = f_ph.read().split()
mean = 0.0
n = 0
for i in range(len(a)/4):
    mean += float(a[i*4+3])
    n += 1
print(1.0*mean/n)
f_ph.close()

