import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('Datasets\startup.csv')
real_x = data.iloc[:, 0:4].values
real_y = data.iloc[:, 4].values

# Encoding the cities to dummy variable
le = LabelEncoder()
# Encode 3rd column of real_x and store in itself
real_x[:, 3] = le.fit_transform(real_x[:, 3])
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(), [3])], remainder='passthrough')
real_x = ct.fit_transform(real_x)

training_x, testing_x, training_y, testing_y = train_test_split(
    real_x, real_y, test_size=0.2, random_state=0)


Lin = LinearRegression()
Lin.fit(training_x, training_y)  # Trains the model
Pred_y = Lin.predict(testing_x)
