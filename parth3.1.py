import pandas as pd
import numpy as np
data=np.arange(1,10).reshape(3,3)
cname=['c1','c2','c3']
rname=['r1','r2','r3']
df=pd.DataFrame(data,index=rname,columns=cname)
print(df)
print(df.apply(np.mean,axis=1))
def f1(arr):
    tmp=[]
    for n in arr:
        if n%2==0:
            tmp.append(1)
        else:
            tmp.append(0)
print(df.apply(f1))