# -*- coding: utf-8 -*-
import codecs
for str0 in ['']:
    f = codecs.open('min_resSinonimFinish(only_T)' + str0 + '.txt', 'r', 'utf8')
#f_g = codecs.open('second_phrases.txt', 'r', 'utf8')
    f_t = open('min_TMapSinonim(only_T)' + str0 + '.txt', 'w')
    f_n = open('min_NMapSinonim(only_T)' + str0 + '.txt', 'w')
    a = f.read().split()
#b = f_g.read().split()
#dict = {}

#for i in range(len(b)/4):
 #   dict[b[i*4 +1] + ' ' + b[i*4 + 2]] = b[i*4]
    map = 0.0
    n = 0
    for i in range(200):
        if a[i*4] == 'T':
            n += 1
            map += 1.0 * n / (i + 1)
            f_t.write(a[i * 4+1] + ' ' + a[i * 4 + 2] + ' ' + str(1.0 * map/n) + '\n')
        else:
            if n==0:
                f_n.write(a[i * 4+1] + ' ' + a[i * 4 + 2] + ' ' + '1.0\n')
            else:
                f_n.write(a[i * 4+1] + ' ' + a[i * 4 + 2] + ' ' + str(1.0 * map/n) + '\n')
    for i in range(200, len(a)//4):
        if a[i * 4] == 'T':
            n += 1
            map += 1.0 * n/(i+1)
    #if 1.0 * map/n >= 0.0:
        if a[i*4] == 'T':
            f_t.write(a[i * 4+1] + ' ' + a[i * 4 + 2] + ' ' + str(1.0 * map/n) + '\n')
        else:
            f_n.write(a[i * 4+1] + ' ' + a[i * 4 + 2] + ' ' + str(1.0 * map / n) + '\n')
    #else:
     #   while i < len(a)/4:
      #      if a[i*4] == 'T':
       #         f_t.write(a[i * 4 + 1] + ' ' + a[i * 4 + 2] + ' ' + '0.0\n')
        #    else:
         #       f_n.write(a[i * 4 + 1] + ' ' + a[i * 4 + 2] + ' ' + '0.0\n')
          #  i += 1
        #break
    f.close()
#f_g.close()
    f_n.close()
    f_t.close()