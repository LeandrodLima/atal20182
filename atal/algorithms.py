#coding: utf-8

import sys

# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas
def retorna_matriculas_decrescente(alist):
	for j in xrange(len(alist)):
		for i in xrange(len(alist)-1):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	return alist

# Esse metodo recebe e valor para ser dado o troco e uma lista com os tipos de moedas possiveis
# e retorna o numero minimo de moedas possiveis em que o troco pode ser dado

# Caso o valor não possa ser alcançado pela combinação de moedas o valor -1 é retornado Ex: valor = 11  moedas = {5, 10, 25}
# Assuma que existe uma quantidade infinita de cada tipo de moeda
def retorna_minimo_moedas(valor, tipos_moedas):
	resultado = guloso(tipos_moedas, valor)
	return resultado

def guloso( moedas, valor):
	total = 0
	cont = 0
	for moeda in reversed(moedas):
		while ((moeda+total)<= valor):
			total += moeda
			cont += 1
		pass
	if(total > valor):
		return -1
	else:
		return cont
