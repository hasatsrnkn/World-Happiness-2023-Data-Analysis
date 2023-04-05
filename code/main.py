import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('data/WHR2023.csv')

plt.plot(df['Ladder score'])
plt.show()

plt.plot(df['Social support'])
plt.show()