#!/usr/bin/python3
"""Dupla-dict összevonások módszere.

Erdős-Rényi gráfok tesztelése - darabok
"""

import sys
from cd_test import test_pieces
from graph import ERGraph

N = int(sys.argv[1])        # csúcsok száma
PARTS = int(sys.argv[2])    # részek száma
MY_FILE = sys.argv[3]       # output fájl neve
REPEAT = int(sys.argv[4])   # ismétlések száma

f = open(MY_FILE, 'w')
f.write("#dcERp N={}, part={} \n".format(N, PARTS))
for i in range(REPEAT):
    GRAPH = ERGraph(N, 1.0, 0.0)
    test_pieces(GRAPH, N, PARTS, f)
    print(i+1 % 10, end='', flush=True)
print()
f.close()
