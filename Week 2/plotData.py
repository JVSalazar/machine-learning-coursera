import pandas as pd
import matplotlib.pyplot as plt

plotData = pd.read_csv('ex1data1.txt', header=None)
population = plotData[0]
profit = plotData[1]

plt.plot(population, profit, 'ro')
plt.xlabel("Population of City in 10,000s")
plt.ylabel("Profit in $10,000s")
plt.title('Population vs Profit')
plt.grid(True)

plt.show()