# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
f_t = open('phrases.txt', 'r')
f = open('tesaurus.txt', 'w')
a = f_t.read()
a = a.decode('cp1251').encode('utf8')
f.write(a)
f.close()
f_t.close()