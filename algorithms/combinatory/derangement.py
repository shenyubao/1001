#!usr/bin/python
# encoding: utf-8

"""
Desarranjo
Autor:
    Pierre Raymond de Montmort
Colaborador:
    Carlos Rodrigues c11a10r9l8o7s6f5e4l3i2x1@yahoo.com.br
Tipo:
    math
Descrição:
    Algoritmo que calcula permutação caótica
Dificuldade:
    facil
Complexidade:
    ?
Referência:
    http://pt.wikipedia.org/wiki/Desarranjo
Comment:
    错排数计算，用于计算有几种全错的排列组合。
    http://zh.wikipedia.org/wiki/%E9%94%99%E6%8E%92%E9%97%AE%E9%A2%98
"""

from __future__ import division

def fatorial(x):
    if x <= 1:
        return 1
    else:
        return x * fatorial(x-1)

n = 5
d = 0
for i in range(0, n):
    d = d + ((-1) ** i / fatorial(i))
print fatorial(n) * d
