# Linear-Regression
Repository of Linear Regression paper from programming class in data science and business analytics course 2020

## Breve resumo do código
==========================

Calculo de uma regressao linear, em que o user pode definir o número de variáveis com um gradiente descendente, ou seja, um algoritmo de otimização que tem como objetivo fazer o ajuste de parâmetros de forma iterativa.
Inicialmente, de modo a trabalhar mais facilmente com o modelo, foram definidos os máximos e mínimos dos parâmetros, mas estes podem ser ajustados pelo utilizador. 
De seguida, definimos a função de treino, tendo em conta a definição do output do modelo de previsao (Y_prev) e o erro. Depois, é definido o ponto em que a função termina de calcular e determina que o minimo erro foi encontrado.
Por fim, é definido o modelo de previsão e é chamado o modelo criado para o utilizador ver o output.


##codigos escritos para plottar o grafico de dispersao: 
import RL
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\beatr\OneDrive\Documentos\data science\programming\trabalho\insurance.csv")
data.head()
X = np.array(pd.DataFrame (data.iloc [:,:-1]))
Y = np.array(pd.DataFrame (data.iloc [:,:-1]))
Model = RL.Rlinear()
Model.min_error
plt.scatter(X,Y,color="red")
plt.title('bmi vs age')
plt.xlabel('bmi')
plt.ylabel('age')
plt.show()


#
