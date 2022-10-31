import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn

df = pd.read_csv('manipulated_datas.csv')

df.plot(kind = 'scatter', x = 'price', y = 'district')

plt.show()