"""
Treinando uma rede que aprenda a tabela AND, e a tabela OR, porém não consegue
aprender a tabela XOR.
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
        print(f"Total de erros: {erro_total}")


# Entradas
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Tabela AND
saidas = np.array([0, 0, 0, 1])
# Tabela OR
# saidas = np.array([0, 1, 1, 1])
# Tabela XOR
# saidas = np.array([0, 1, 1, 0])

pesos = np.array([0.0, 0.0])
taxa_aprendizagem = 0.1

treinar()
print("Rede neural treinada")
print(calcula_saida(entradas[0]))
print(calcula_saida(entradas[1]))
print(calcula_saida(entradas[2]))
print(calcula_saida(entradas[3]))
