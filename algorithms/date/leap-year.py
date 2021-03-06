# -*- encoding: utf-8 -*-
"""
Bissexto
Autor:
    ?
Colaborador:
    Bruno Lara Tavares <bruno.exz . at . gmail . com>
Tipo:
    date
Descrição:
    Calcula os próximos anos bissextos
Complexidade:
    ?
Dificuldade:
    facil
Referências:
    http://pt.wikipedia.org/wiki/Ano_bissexto#Calend.C3.A1rio_Gregoriano
Comment:
    判断是否闰年
    http://zh.wikipedia.org/wiki/%E9%97%B0%E5%B9%B4
"""

from datetime import datetime

def anoBissexto(anos):
	anoAtual = datetime.now().year
	proximoAno = anoAtual + anos
	for ano in range(anoAtual,proximoAno):
		if ano % 4 == 0 and (ano % 100 or ano % 400 == 0):
			yield ano

for ano in anoBissexto(100): print ano
