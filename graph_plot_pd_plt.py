# -*- coding: utf-8 -*-
"""Graph Plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YhtXlVH7iOUHktlz4x6dPDWzh472d3gA
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [20.00, 10.00]
plt.rcParams["figure.autolayout"] = True

headers = ['date', 'sensor0']

df = pd.read_csv('plants.csv', names=headers)

df.set_index('date').plot()
plt.xlabel('Date')
plt.ylabel('Moisture')
plt.grid()
plt.show()