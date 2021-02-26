# redes-neurais-artificiais-python
Respositório de anotações e exemplos desenvolvidos em um curso de redes neurais com python, na Udemy.

> Link para o curso, [aqui](https://www.udemy.com/course/redes-neurais-artificiais-em-python/)

- Instalando as dependências
```
pip install -r requirements.txt
```

## Anotações

- Redes neurais se aplicam somente em casos onde você tem **muitos dados** e problemas **complexos**
- "Imitar" o sistema nervoso de humanos no processo de aprendizagem
- Inspirada em redes neurais biológicas, principalmente na troca de informações

## Neurônio

- **Neurônios:** O cérebro usa para processar informações
- **Axônio:** Transmite o sinal de um neurônio pra outro, conectando os neurônios
- **Substâncias químicas:** São lançadas das sinapses e entram pelos dentritos, aumentando ou baixando o potencial elétrico do corpo da célula
- **Funcionamento:** Neurônio dispara se a entrada é maior que um número definido

## Fluxo

- É fornecido um valor de **entrada**, a rede processa e retorna uma **resposta**
- O **neurônio** é ativado somente se o valor for maior que um limiar

## Neurônio artificial

![neurônio artificial](https://github.com/renanstd/redes-neurais-artificiais-python/blob/main/images/neuronio_artificial.png)

- Entradas, e pesos (weight)
- Função soma
- Função ativação

### Função soma:

![função soma](https://github.com/renanstd/redes-neurais-artificiais-python/blob/main/images/funcao_soma.png)

- `X` são entradas
- `W` são pesos
- Faz a soma da multiplicação de **xi** por **wi**
    - `(x1 * w1) + (x2 * w2) + (x3 * w3)`
- Step function (função degrau)
    - Retorna 1 caso soma seja maior que *N*
    - Retorna 0 caso contrário
- Step function é bem *tudo ou nada*, pequenas modificações podem mudar todo o resultado
- **Peso positivo:** sinapse excitadora: tem chandes de *ativar* o neurônio
- **Peso nevagito:** sinapse inibidora, tem chances de *desativar* o neurônio
- Pesos são as sinapses
- **O CONHECIMENTO DA REDE NEURAL, SÃO OS PESOS**

## Tipos de aprendizagem de máquina

| **Supervisionada** | **Não supervisionada** | **Reforço** |
|---|---|---|
| Classificação | Associação |   |
| Regressão | Agrupamento |   |
|   | Detecção de desvios |   |
|   | Padrões sequenciais |   |
|   | Sumarização |   |

## Cálculos de ajustes de pesos

- Algoritmo simples para encontrar valor de `erro`:
    - `erro = resposta_correta - resposta_calculada`
- Definições de novos pesos
    - `peso(n+1) = peso(n) + (taxa_aprendizagem * entrada * erro)`

## Limitações perceptron 1 camada

- Ele consegue resolver somente problemas lineramente separáveis (aula 17)
- Por isso ele conseguiu aprender a tabela `AND`, tabela `OR`, mas não a tabela `XOR`
- Para trabalharmos com problemas **não linearmente separáveis**, precisamos adicionar mais **camadas** a nossa rede

# Redes multicamadas

![rede multicamada](https://github.com/renanstd/redes-neurais-artificiais-python/blob/main/images/multicamadas.png)

- Fornece um valor de entrada, a rede processa e retorna uma resposta *(feed forward)*
- O neurônio é ativado somente se o valor for maior que um limiar

## Funções de ativação

- **Step (função degrau):** Retorna 0 ou 1
- **Sigmoid (função sigmoide):** Retorna entre 0 e 1 (não retorna valores negativos)
- **Hyperbolic tangent (função tangente hiperbólica):** Retorna entre -1 e 1

[Mais informações](https://en.wikipedia.org/wiki/Activation_function)

## Fluxo

![rede multicamada](https://github.com/renanstd/redes-neurais-artificiais-python/blob/main/images/fluxo.png)

- Inicializa os pesos com valores aleatórios
- Baseado nos dados (aprendizagem supervisionada), realiza os cálculos com os pesos e calcula o erro
- Calcula as mudanças nos pesos e os atualiza *(backpropagation)*
- O algoritmo termina quando o erro é **pequeno**
- Em outras literaturas, *Cost function* é a **função de erro**

## Descida do gradiente (gradient descent)

- Encontrar a combinação de pesos que o erro é o menor possível
    - Força bruta
    - Simmulated anealing
    - Algoritmos genéticos
- Gradiente é calculado para saber **quanto ajustar os pesos**
    - Mínimos locais
    - Mínimos globais
- Calcular o declive da curva com **derivadas parciais**
    - Cálculo de derivadas parciais: **y * (1 - y)**, onde y é o resultado da **sigmóide**

A **derivada** serve para descobrir para qual lado um peso deve "pender", afim de encontrar o **mínimo global**

![derivada parcial](https://github.com/renanstd/redes-neurais-artificiais-python/blob/main/images/derivada.png)

## Cálculo do delta

Fluxo de cálculos:
- Função ativação
- Derivada da função
- Delta
- Gradiente

É necessário calcular o delta da camada **oculta** e da camada de **saída**

Fórmula do delta para a camada de **saída**
```
delta_saida = erro * derivada_sigmoide
```

Fórmula do delta para a camada **oculta**
```
delta_oculta = derivada_sigmoide * peso_camada_seguinte * delta_saida
```

## Backpropagation

Fórmula
```
peso = (peso * momento) + (entrada * delta * taxa_de_aprendizagem)
```

### Parâmetros

- Taxa aprendizagem (learning rate)
    - Define o quão "rápido" um algoritmo vai aprender
    - **Alto:** A convergência é rápida, mas pode perder o mínimo global
    - **Baixo:** Será mais lento, mas tem mais chances de chegar no mínimo global
- Momento (momentum)
    - Escapar de mínimos locais (nem sempre funciona)
    - Define o quão confiável é a última alteração
    - **Alto:** Aumenta a velocidade da convergência
    - **Baixo:** Pode evitar mínimos locais

## Output rede_multicamada/exemplo_01

![output](https://github.com/renanstd/redes-neurais-artificiais-python/blob/main/images/result.png)

## Conceitos extras

### Bias

- Bias adiciona umm atributo a mais, em cada uma das camadas. Se a rede tem 2 inputs, com bias, ela vai passar a ter 3 inputs, e +1 neurônio na camada oculta.
- Bias geralmente é usado quando temos 2 inputs de valor zero, com *step function*.

### Erros

- Nas explicações, usamos somente o algoritmo simples: `resposta_correta - resposta_calculada`
- Média da diferença entre o esperado e o que foi previsto pela rede
- Erros maiores contam mais que erros menores
- Penaliza erros maiores

### Mean Square Error (MSE)

- Tem como valor de erro o resultado dessa fórmula:

![mse](https://github.com/renanstd/redes-neurais-artificiais-python/blob/main/images/mse.png)

- Exemplo:

![exemplo mse](https://github.com/renanstd/redes-neurais-artificiais-python/blob/main/images/mse_exemplo.png)


### Root Mean Square Error (RMSE)

- Tem como valor de erro a **raíz quadrada** do MSE

![rmse](https://github.com/renanstd/redes-neurais-artificiais-python/blob/main/images/rmse.png)

