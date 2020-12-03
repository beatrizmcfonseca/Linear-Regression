import numpy as np
class Rlinear():
    def __init__(self,n_iteracoes=1000,min_error=0.001,min_delta=0.001,learning_rate=0.1):
        self.n_iteracoes=n_iteracoes
        self.min_error=min_error
        self.min_delta=min_delta
        self.learning_rate=learning_rate
        
    def treino(self, X, Y):
        n_individuos, n_variaveis=X.shape
        self.pesos=np.random.rand()

#desenhar variáveis
var_x = []
nr_var_x = len(var_x)
var_y = []

#Calculate means
#mean of x
def mean(var_x):
    for x in var_x:
        mean_x = sum(var_x) / len (var_x)
print ("The mean for variable x is {mean_x}")

#mean of y
def mean_y(var_y):
    for y in var_y:
        mean_y = sum(var_y) / len (var_y)
print ("The mean for variable y is {mean_y}")

#calculate distance to the mean
#distance of variable x
def distance_x(var_x):
    for x in var_x:
        distance_x = sum(var_x - mean_x)
print ("The sum of distances to the mean for variable x is {distance_x}")

#distance of squares of variable x:
def square_distance(var_x):
    for x in var_x:
        square_distance = sum (var_x - mean_x)**2

#distance of variable y
def distance_x(var_y):
    for y in var_y:
        distance_y = sum(var_y - mean_y)
print ("The sum of distances to the mean for variable y is {distance_y}")

#calculate multiplication of distance to the mean
def multiplication(var_x,var_y):
    for distance in distance_x:
        multiplication = distance_x * distance_y

#calculate slope of the regression (b1)
def slope(multiplication):
    for x,y in multiplication:
        slope = multiplication / square_distance
print ("The slope of the linear regression is {slope}")
