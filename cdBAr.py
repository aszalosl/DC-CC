#!/usr/bin/python3
"""Dupla-dict összevonások módszere.

Barabási Albert gráfok tesztelése - rekurzív
"""

import sys
from cd_test import test_recursive
from graph import BAGraph

N = int(sys.argv[1])        # csúcsok száma
LIMIT = int(sys.argv[2])    # min. hossz
MY_FILE = sys.argv[3]       # output fájl neve
REPEAT = int(sys.argv[4])   # ismétlések száma

f = open(MY_FILE, 'w')
f.write("#dcBAr N={}, limit={} \n".format(N, LIMIT))
for i in range(REPEAT):
    GRAPH = BAGraph(N, 0.0)
    test_recursive(GRAPH, N, LIMIT, f)
    print(i+1 % 10, end='', flush=True)
print()
f.close()
