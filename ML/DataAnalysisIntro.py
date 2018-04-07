#Pandas        Data Analysis
#Numpy         Numerical Python - ndarray
#Matplotlib    Data Visualization
#Seaborn       Graphics for Data Visualization
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

arr_1 = np.array([12,34,561,2,4,5,67])
arr_2 = np.arange(0,20)

x = np.array([i for i in range(20)])
y = np.random.randint(100,1000,20)
z = np.random.randint(1,50,20)

fig = plt.figure(figsize=(12,6))
ax = Axes3D(fig)
ax.scatter(x,y,z,color='red')
plt.show()

#Pandas
#- Series       1D
#- DataFrame    2D

dataset = pd.read_csv('matches.csv')
dataset.shape

obs_1 = dataset.head()

plt.hist(dataset['season'], rwidth=0.8)

sns.countplot(x = dataset['season'], data=dataset)




