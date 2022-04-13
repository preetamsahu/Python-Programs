import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('pulsedata.csv')
x=df['Calories']
plt.hist(x)
plt.show()
print(x)