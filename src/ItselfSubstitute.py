# -*- coding: utf-8 -*-
import codecs
number = 5
f_sub = codecs.open('substitute.txt', 'r', 'utf8')
f_vec = codecs.open('text_output_substitute.txt', 'r', 'utf8')
f_ph = codecs.open('second_phrases.txt', 'r', 'utf8')
f_res = open('second_resSubstitute_' + str(number) + '.txt', 'w')

a = f_sub.read().split()
sub = {}
for i in range(len(a)//11):
    sub[a[11 * i]] = []
    for j in range(number):
        sub[a[11*i]].append(a[11 * i + j + 1])
print('1\n')

vec = {}
a = f_vec.readline().split()
while a:
    if '_' in a[0]:
        vec[a[0]] = a[1:]
    a = f_vec.readline().split()
print('2\n')

a = f_ph.read().split()
ph0 = {}
ph = {}
for i in range(len(a)//4):
    fl = list(0 for j in range(2 * number))
    cos = list(0 for j in range(2 * number))
    vs = list([] for j in range(2 * number))
    v = vec[a[4 * i + 1] + '_' + a[4 * i + 2]]
    for j in range(number):
        if not(a[4 * i + 1] + '_' + sub[a[4 * i + 2]][j] in vec):
            cos[2 * j] = -1
            fl[2 * j] = 1
        else:
            vs[2 * j] = vec[a[4 * i + 1] + '_' + sub[a[4 * i + 2]][j]]
        if not(sub[a[4 * i + 1]][j] + '_' + a[4 * i + 2] in vec):
            cos[2 * j + 1] = -1
            fl[2 * j + 1] = 1
        else:
            vs[2 * j + 1] = vec[sub[a[4 * i + 1]][j] + '_' + a[4 * i + 2]]
    sq = 0
    sqs = list(0 for j in range(2 * number))
    mul = list(0 for j in range(2 * number))
    for j in range(len(v)):
        sq += float(v[j]) * float(v[j])
        for k in range(2 * number):
            if not(fl[k]):
                sqs[k] += float(vs[k][j]) * float(vs[k][j])
                mul[k] += float(v[j]) * float(vs[k][j])
    for j in range(2 * number):
        if not(fl[j]):
            cos[j] = mul[j] / (sq * sqs[j])
    maximum = max(cos)
    if maximum == -1:
        ph0[a[4 * i] + ' ' + a[4 * i + 1] + ' ' + a[4 * i + 2]] = int(a[4 * i + 3])
    else:
        ph[a[4 * i] + ' ' + a[4 * i + 1] + ' ' + a[4 * i + 2]] = maximum
print('3\n')

for i in sorted(ph0, key=ph0.__getitem__, reverse=True):
    f_res.write(str(i) + ' -1\n')
for i in sorted(ph, key=ph.__getitem__, reverse=False):
    f_res.write(str(i) + ' ' + str(ph[i]) + '\n')
f_sub.close()
f_vec.close()
f_ph.close()
f_res.close()