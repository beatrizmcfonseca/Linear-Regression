class Rlinear():
    def __init__(self,n_iteracoes=1000,min_error=0.001,min_delta=0.001,learning_rate=0.1):
        self.n_iteracoes=n_iteracoes
        self.min_error=min_error
        self.min_delta=min_delta
        self.learning_rate=learning_rate
        
    def treino(self, X, Y):
        n_individuos, n_variaveis=X.shape
        self.pesos=np.random.rand(n_variaveis,1)
        for e in range(self.n_iteracoes):
            for i in range(n_individuos):
                y_prev=X[i,:].dot(self.pesos)
                error=y_prev-Y[i]
                self.pesos=self.pesos-self.learning_rate*(2*error*X[i,:].reshape(n_variaveis,1))
                
    def predict(self,X):
        previsao=X.dot(self.pesos)
        return previsao
