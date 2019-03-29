#!/usr/bin/env python3

import random
import datetime

random.seed()

f = open('test.csv', 'a+')
for i in range(100):
    w = 152 + random.uniform(-2.0, 2.0)
    r = 250 + random.randint(-100, 100)
    y = 600 + random.randint(-100, 100)
    g = 250 + random.randint(-50, 50)
    t = r + y + g
    d = datetime.datetime.now().strftime('%Y%m%d%H%M') + str(i)
    f.write(d + ',' + str(r) + ',' + str(y) + ',' + str(g) + ',' + 
            str(t) + ',' + str(w) + '\r\n')
f.close
