"""
Treinando uma rede que aprenda a tabela AND, com ajustes automáticos
de pesos.
"""
import numpy as np


def step_function(soma):
    return soma >= 1


def calcula_saida(entrada):
    soma = entrada.dot(pesos)
    return step_function(soma)


def treinar():
    """
    Treina o algoritmo, com base nos valores corretos fornecidos em "entradas"
    e "saidas", até encontrar os valores de pesos que resultem em
    erro_total = 0
    """
    erro_total = 1
    while erro_total != 0:
        erro_total = 0
        for i in range(len(saidas)):
            saida_calculada = calcula_saida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saida_calculada)
            erro_total += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxa_aprendizagem * entradas[i][j] * erro)
                print("Peso atualizado: {}".format(str(pesos[j])))


entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Definir na saída os resultados da tabela AND para cada item de entrada
saidas = np.array([0, 0, 0, 1])
pesos = np.array([0.0, 0.0])
taxa_aprendizagem = 0.1


treinar()
