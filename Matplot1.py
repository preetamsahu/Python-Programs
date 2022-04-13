import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# df=pd.read_csv('pulsedata.csv')
# df['Cat']=['High' if df.loc [i,'Calories']>=400 else 'Medium' for i in df.index]
# df['Cat']=['Low' if df.loc [i , 'Calories']<=200 else df.loc[i ,'Cat'] for i in df.index]
# x=df['Cat']
# y=df['Calories']
# plt.bar(x,y,color=(0.2, 0.4, 0.6, 0.6))
# plt.show()
# print(df)
arr=np.array([3,8,1,10])
plt.plot(arr,'t--r')
plt.show()