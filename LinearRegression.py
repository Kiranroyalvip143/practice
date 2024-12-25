from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Data
z= np.array([1, 2, 3, 4])
print(z)
X = np.array([1, 2, 3, 4]).reshape(-1, 1)
print("X Points:",X)  # Input feature
y = np.array([2, 3, 4, 5])  # Target variable

# Model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Plotting
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Best Fit Line')
plt.legend()
plt.show()
