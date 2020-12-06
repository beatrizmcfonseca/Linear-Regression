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

X=[[1,0.7,0.9],[1,0.7,0.8],[1,1.2,1.4],[1,1.3,1]]
Y=[1,1,2,2]
X=np.array(X)
Y=np.array(Y)

import URL

Model = RL.Rlinear()

Model
<RL.Rlinear at 0x159974ff670>

Model.min_error
0.001

Y[0]
1

Model.treino(X,Y)

X[:]
Y[:]

array(1, 1, 2, 2])

Model.pesos
array([-1.20960003],
      [ 1.00460275],
      [-0.16675039]])
      
print(X.shape) # Vewing the shape of X
print(Y.shape) # Vewing the shape of y
(4, 3)
(4, )

y_prev=X.dot(Model.pesos)
y_prev

array([[-1.74319865, -1.74319865, -2.74319865, -2.74319865],
       [-1.71688526, -1.71688526, -2.71688526, -2.71688526],
       [-1.37246424, -1.37246424, -2.37246424, -2.16675039]])
       
Model.pesos=Model.pesos-0.1*(2*2*X[1,:].reshape(3,1))

Model.predict(X)
array([[-0.74319865],
      [-0.71688526],
      [-0.37246424],
      [-0.16675039]])
      
previsao = X.dot(Model.pesos)

previsao

plt.scatter(X,Y)
plt.plot(X,y_prev, color='red')
plt.show

--------------------------------------------------------------------------------------------------------------------------------------------
                                                                                           Traceback (most recent call last)
 Value error
 <ipython-input-68-739ac65a1f55> in <module>
  ----> 1 plt.scatter(X,Y)
        2 plt.scatter(X,y_prev,color='red')
        3 plt.show()
  
  
  ~\anaconda3\envs\RL\site-packages\matplotlib\pyplot.py in scatter(x, y, s, c, marker, cmap,norm, vm, in, vmax, alpha, linewidths, verts, edgecolors, plotnonfinite, data, **kwargs)
  2888        verts=cbook.deprecation_deprecated_parameter,
  2889            edgecolors=None, *, plotnonfinite=False, data=None, **Kwargs):
->2890         _ret = gca().scatter(
  2891            x,y, s=s, c=c, marker=marker, cmap=cmap, norm=norm,
  2892           vmin=vmin, vmax=vmax, alpha=alpha, linewidths=linewidths,
            
 ~\anaconda3\envs\RL\lib\site-packages\matplotlib\_init_.py in inner(ax, data, *args, **kwargs)
  1445        def inner(ax, *args, data=None, **kwargs):
  1446                if data is None:
->1447                    return func(ax, *map(sanitize_sequence, args), **kwargs)
  1448
  1449                bound=new_sig.bind(ax, *args, **kwargs)
  
  ~\anaconda3\envs\RL\site-packages\matplotlib\cbook\deprecation.py in wrapper(*inner_args, **inner_kwargs)
      409                     else deprecation_addendum,
      410               **kwargs)
   -->411         return_func(**inner_args, **inner_kwargs)
   
   ~\anaconda3\envs\RL\site-packages\matplotlib\axes\axes.py in scatter(x, y, s, c, marker, cmap,norm, vm, in, vmax, alpha, linewidths, verts, edgecolors, plotnonfinite, data, **kwargs)
   4439         y =np.ma.ravel(y)
   4440         if x.size != y.size:
-> 4441             raise ValueError("x and y must be the same size")
   4442
   4443         if s is None:
  
ValueError: x and y must be the same size

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from IPython.display import set_matplotlib_formats

data = pd.read_csv(r"C:\Users\beatr\OneDrive\Documentos\data science\programming\trabalho\insurance.csv"
data.head()


data.plot.scatter(x='age',
                y='bmi'
               ylim=(18,5,24.9)); #bmi saudavel
               
               
 Y = data.bmi
 Y
 
0        0
1        1
2        3
3        0
4        0
        ..
1333     3
1334       0

import RL

Model = RL.Rlinear()

Model

<RL.Rlinear at 0x20470316520>

Model.min_error
0.001

Y[3]
22.705

Model.treino(X,Y)

-------------------------------------------------------------------------------------------------------
                                                  Traceback (most recent call last)
 ValueError
 <ipython-input-74-1a04583fd429> in <module>
 ----> 1 Model.treino(X,Y)
  
 ~\OneDrive\Documentos\data science\programming\trabalho\datascience-programming-regression\RL.py in treino(self, X, Y)
    9
    10    def treino(self, X, Y):
--->11        n_individuos, n_variaveis=X.shape
    12        self.pesos=np.random.rand(n_variaveis,1)
    13        for e in range(self.n_iteracoes):
 
 ValueError: not enough values to unpack (expected 2, got 1)
 
 print(X.shape) # Vewing the shape of X
 print(Y.shape) # Vewing the shape of y
 
 (1338,)
 (1338,)
    



  
      
      



###

#
