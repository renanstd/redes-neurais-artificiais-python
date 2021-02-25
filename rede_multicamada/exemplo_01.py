"""
Rede neural multicamada que tentará aprender a tabela XOR.
"""
import random
import numpy as np


def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))


def sigmoide_derivada(sig):
    return sig * (1 - sig)


# Tabela XOR
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
saidas = np.array([[0], [1], [1], [0]])

# Pesos gerados manualmente
pesos_camada_0 = np.array([
    [-0.424, -0.740, -0.961],
    [0.358, -0.577, -0.469],
])
pesos_camada_1 = np.array([[-0.017], [-0.893], [0.148]])

# Pesos gerados aleatoriamente
# pesos_camada_0 = 2 * np.random.random((2, 3)) - 1
# pesos_camada_1 = 2 * np.random.random((3, 1)) - 1

epocas = 1000000  # Quantidade de vezes que os pesos serão ajustados
taxa_aprendizagem = 0.6
momento = 1

for i in range(epocas):
    camada_entrada = entradas
    # Primeira camada
    soma_sinapse_0 = np.dot(camada_entrada, pesos_camada_0)
    camada_oculta = sigmoid(soma_sinapse_0)
    # Segunda camada
    soma_sinapse_1 = np.dot(camada_oculta, pesos_camada_1)
    camada_saida = sigmoid(soma_sinapse_1)
    # Calculo do erro
    erro_camada_saida = saidas - camada_saida
    media_absoluta_erros = np.mean(np.abs(erro_camada_saida))
    print(f"Média de erros na época {i}: {media_absoluta_erros}")
    # Cálculos para encontrar os deltas
    derivada_saida = sigmoide_derivada(camada_saida)
    delta_saida = erro_camada_saida * derivada_saida
    pesos_camada_1_transposta = pesos_camada_1.T
    delta_saida_x_peso = delta_saida.dot(pesos_camada_1_transposta)
    delta_camada_oculta = delta_saida_x_peso * sigmoide_derivada(camada_oculta)
    # Cálculos de pesos via back propagation
    # Cálculos de pesos da camada oculta -> Camada saída
    camada_oculta_transposta = camada_oculta.T
    pesos_novos_1 = camada_oculta_transposta.dot(delta_saida)
    pesos_camada_1 = (pesos_camada_1 * momento) + (pesos_novos_1 * taxa_aprendizagem)
    # Cálculos de pesos da camada entrada -> Camada oculta
    camada_entrada_transposta = camada_entrada.T
    pesos_novos_0 = camada_entrada_transposta.dot(delta_camada_oculta)
    pesos_camada_0 = (pesos_camada_0 * momento) + (pesos_novos_0 * taxa_aprendizagem)
