import numpy as np
import pandas as pd

print("Masking & query")

df=pd.DataFrame(np.random.rand(5,2),columns=["A","B"])
print(df,"\n")

print(df[(df['A']<0.5)&(df['B']>0.3)])

print(df.query("A<0.5 and B>0.3"))