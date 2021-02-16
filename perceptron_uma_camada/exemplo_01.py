def soma(entradas, pesos):
    soma = 0
    for i, j in zip(entradas, pesos):
        soma += i * j
    return soma


def step_function(soma):
    return soma >= 1


entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0]

soma = soma(entradas, pesos)
print("Resultado da soma:")
print(soma)
resultado = step_function(soma)
print("Resultado da função de ativação:")
print(resultado)
