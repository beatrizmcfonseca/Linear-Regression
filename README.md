# Linear-Regression
Repository of Linear Regression paper from programming class in data science and business analytics course 2020

## Breve resumo do código
==========================

Calculo de uma regressao linear, em que o user pode definir o número de variáveis com um gradiente descendente, ou seja, um algoritmo de otimização que tem como objetivo fazer o ajuste de parâmetros de forma iterativa.
Inicialmente, de modo a trabalhar mais facilmente com o modelo, foram definidos os máximos e mínimos dos parâmetros, mas estes podem ser ajustados pelo utilizador. 
De seguida, definimos a função de treino, tendo em conta a definição do output do modelo de previsao (Y_prev) e o erro. Depois, é definido o ponto em que a função termina de calcular e determina que o minimo erro foi encontrado.
Por fim, é definido o modelo de previsão e é chamado o modelo criado para o utilizador ver o output.


###
import numpy as np
import panda as pd
import matplolib.pyplot as plt
from
