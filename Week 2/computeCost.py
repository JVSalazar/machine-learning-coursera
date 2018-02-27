import pandas as pd
import numpy as np

# Extract data from assignment file
plotData = pd.read_csv('ex1data1.txt', header=None)
m = len(plotData)
population = plotData[0]
profit = plotData[1]
unitVector = np.ones(m)

# Initialize parameters
iterations = 1500
alpha = 0.01
thetas = np.zeros(2)

# # Perform gradient descent
# for i in range(0, iterations):
#     thetas = thetas[0] - alpha*1/m*((np.matmul(thetas[0], population) - profit) * population

thetas = np.array([thetas])
cost = np.matmul(thetas.transpose(), np.column_stack((unitVector, population))) - profit
print(cost)
# for i in range(0, m):
#     #ost = np.matmul(thetas, np.column_stack(unitVector, population)) - profit

# cost = 1/2*m*cost**2
# print(cost)