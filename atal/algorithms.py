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
	print valor, tipos_moedas

	resultado = backtracking(tipos_moedas, valor)

	if resultado == sys.maxint:
		return -1
	else:
		return resultado

def backtracking(tipos_moedas, valor):
	return retorna_min_moedas(tipos_moedas, valor, [])

def retorna_min_moedas(tipos_moedas, valor, chute):
	tam_aux = -1
	if(ehsolution(chute, valor)):
		return len(chute)
	else:
		for i in range(len(tipos_moedas)):
			chute.append(tipos_moedas[i])
			if(promissor(chute, valor)):
				tamanho = retorna_min_moedasBT(tipos_moedas, valor, chute)
				if(tam_aux == -1):
					tam_aux = tamanho
				else:
					if(tam_aux >= tamanho):
						tam_aux = tamanho
			chute.pop()
	return tam_aux
def ehsolucao(chute, valor):
	soma = valor
	for moeda in chute:
		soma = valor - moeda
	return  soma == 0

def promissor(chute, valor):
	soma = 0
	for moeda in chute:
		soma = soma + moeda
	return soma <= valor
