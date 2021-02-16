"""
Este segundo exemplo nada mais é que o primeiro, só que otimizado,
usando o array da lib numpy.
"""
import numpy as np


def soma(entradas, pesos):
    return entradas.dot(pesos)


def step_function(soma):
    return soma >= 1


entradas = np.array([-1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

soma = soma(entradas, pesos)
print("Resultado da soma:")
print(soma)
resultado = step_function(soma)
print("Resultado da função de ativação:")
print(resultado)
