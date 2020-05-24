import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('Datasets\company.csv')

# All rows of 0th column and convert to array
real_x = data.iloc[:, 0].values.reshape(-1, 1)
real_y = data.iloc[:, 1].values.reshape(-1, 1)

training_x, testing_x, training_y, testing_y = train_test_split(
    real_x, real_y, test_size=0.3, random_state=0)

Lin = LinearRegression()
Lin.fit(training_x, training_y)  # Trains the model
Pred_y = Lin.predict(testing_x)

plt.subplot(3, 1, 1)
plt.scatter(training_x, training_y, color='green')
plt.plot(training_x, Lin.predict(training_x), color='blue')
plt.title('Salary & Experience Training Plot')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')

plt.subplot(3, 1, 3)
plt.scatter(testing_x, testing_y, color='green')
plt.plot(training_x, Lin.predict(training_x), color='blue')
plt.title('Salary & Experience Testing Plot')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
