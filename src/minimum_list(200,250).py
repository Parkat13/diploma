# -*- coding: utf-8 -*-
import codecs
f_t = codecs.open('second_phrases.txt', 'r', 'utf8')
f = open('phrases(200,250).txt', 'w')
a = f_t.readline().split()
while len(a) > 0:
    if (int(a[3]) >= 200) and (int(a[3]) <= 250):
        f.write(a[0] + ' ' + a[1] + ' ' + a[2] + ' ' + a[3] + '\n')
    a = f_t.readline().split()
f.close()
f_t.close()