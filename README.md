# redes-neurais-artificiais-python
Respositório dos exemplos desenvolvidos em um curso de redes neurais na Udemy.

- Instalando as dependências
```
pip install -r requirements.txt
```

## Anotações

- Parei na aula 15

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

![neurônio artificial]()

- Entradas, e pesos (weight)
- Função soma
- Função ativação

### Função soma:

![função soma]()

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
