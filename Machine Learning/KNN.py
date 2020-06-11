import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap

data = pd.read_csv('Datasets/Ads.csv')

real_x = data.iloc[:, [2, 3]].values
real_y = data.iloc[:, 4].values

trainig_x, test_x, training_y, test_y = train_test_split(
    real_x, real_y, test_size=0.25, random_state=0)

s_c = StandardScaler()
trainig_x = s_c.fit_transform(trainig_x)
test_x = s_c.fit_transform(test_x)

knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
knn.fit(trainig_x, training_y)

y_pred = knn.predict(test_x)

# In Confusion Matrix, addition of left diagonal gives correct results and addition of right matrix gives the incorrecr results
c_m = confusion_matrix(test_y, y_pred)
