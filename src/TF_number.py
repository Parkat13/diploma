# -*- coding: utf-8 -*-
import sys
import codecs
import time
reload(sys)
sys.setdefaultencoding('utf-8')
s = 0
f_t = codecs.open('freq_last.txt', 'r', 'utf8')
f_obuch = codecs.open('text.txt', 'r', 'utf8')
f_f = open('TFWords.txt', 'w')
a = f_t.read().split()
dict = {}
for i in range(len(a) / 3):
    dict[a[i * 3]] = 0
    dict[a[i * 3 + 1]] = 0
words_str = f_obuch.read(100000000).strip()
flag_last_word = 0
if words_str[-1] == ' ':
    flag_last_word = 1
words = words_str.split()
if len(words) == 1:
    words.append(' ')
k = 0
while len(words) != 0:
    start_time = time.time()
    for word in words[0:-1]:
        word = word.lower()
        if word in dict:
            dict[word] += 1
        s += 1
    print k, "--- %s seconds ---" % (time.time() - start_time)
    k += 1
    if flag_last_word == 1:
        words_str = (words[-1] + ' ' + f_obuch.read(100000000).strip())
    else:
        words_str = (words[-1] + f_obuch.read(100000000).strip())
    flag_last_word = 0
    if (words_str == '  ') or (words_str == ' '):
        break
    if words_str[-1] == ' ':
        flag_last_word = 1
    words = words_str.split()
    if len(words) == 1:
        words.append(' ')
for i in range(len(a) / 3):
    f_f.write(a[i * 3] + ' ' + a[i * 3 + 1] + ' ' + str(dict[a[i * 3]]) + ' ' + str(dict[a[i * 3 + 1]]) + '\n')
print s
f_f.close()
f_obuch.close()
f_t.close()