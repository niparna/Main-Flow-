# -*- coding: utf-8 -*-
"""Task3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jIBX8YiJLKacSqxz8laisw9pFoIRz3SC
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/householdtask3.csv')

data.head(10)

plt.scatter(data['year'], data['own'])
plt.title('Scatter Plot')
plt.xlabel('year')
plt.ylabel('own')
plt.show()

plt.plot(data['year'])
plt.plot(data['own'])
plt.title('Line Chart')
plt.xlabel('year')
plt.ylabel('own')
plt.show()

plt.bar(data['year'], data['own'])
plt.title('Bar Chart')
plt.xlabel('year')
plt.ylabel('own')
plt.show()

plt.hist(data['income'])
plt.title('Histogram')
plt.show()