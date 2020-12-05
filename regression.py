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
