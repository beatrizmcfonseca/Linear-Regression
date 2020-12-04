#definir valores max e minimos e definir parametros
class Rlinear():
    def __init__(self,n_iteracoes=1000,min_error=0.001,min_delta=0.001,learning_rate=0.1):
        self.n_iteracoes=n_iteracoes
        self.min_error=min_error
        self.min_delta=min_delta
        self.learning_rate=learning_rate
        
#definir função de treino 
#inicializar parametros da função de treino
    def treino(self, X, Y):
        n_individuos, n_variaveis=X.shape
        self.pesos=np.random.rand(n_variaveis,1) 
        for e in range(self.n_iteracoes): #definir como gradiente descente 
            for i in range(n_individuos): #definir restricoes do modelo
                y_prev=X[i,:].dot(self.pesos) #calcular o y em função do peso que ela tem na funcao (o "slope")
                error=y_prev-Y[i] #calcular o erro (Y previsto - Y verdadeiro)
                self.pesos=self.pesos-self.learning_rate*(2*error*X[i,:].reshape(n_variaveis,1)) #calcular o peso da variavel tendo em conta o erro do modelo
         
 #parar o modelo de treino
    If error < self.min_error
        break
                
 #definir funcao de previsao 
    def predict(self,X):
        previsao=X.dot(self.pesos)
        return previsao #testar funcao previsao 
